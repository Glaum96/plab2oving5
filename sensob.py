

class Sensob:

    # Parameter sensors is a list of sensor objects,
    # behaviors a set of Behavior objects
    def __init__(self, sensors):
        self.sensors = sensors  # List of sensors that the Sensob-object operates on
        self.behaviors = []  # List of behaviors (no duplicates) that use the Sensob-object
        self.active_flag = True  # Used by BBCON to only update sensors when their sensor objects are active
        self.sensor_values = [None] * len(sensors)  # List of raw values collected from the sensors
        self.value = 0  # The preprocessed value that Behavior-objects will use

    def add_behavior(self, behavior):  # Adds behavior, as long as it is not already in the list
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)
            # Add this Sensob-object to the behavior's list, so that both points to each other
            behavior.add_sensob(self)

    # This is the method that calculates the value used by Behavior-objects,
    # will be overwritten in subclasses
    def update(self):
        # Sets flag false so Sensob-object will stay inactive if no behaviors activates it
        self.active_flag = False
        for behavior in self.behaviors:
            if behavior.active_flag:
                self.active_flag = True
        if self.active_flag:
            self.update_values()
        return self.active_flag
        # NOTE: Subclasses must call superclass update()-method
        # before they process data and update self.value
        # FORMAT OF update() IN SUBCLASS:
        # def update(self):
        #     if super(MySensobSubClass, self).update():
        #         ...
        #         *Your code here*
        #         ...

    def get_sensor_values(self):
        return self.sensor_values

    # Returns the computed value of the Sensob
    def get_value(self):
        return self.value

    # Help method for updating and retrieving values from each sensor
    def update_values(self):
        for i in range(0, len(self.sensors)):
            self.sensors[i].update()
            self.sensor_values[i] = self.sensors[i].get_value()

    # Method for resetting values
    def reset(self):
        if self.active_flag:
            for i in range(0, len(self.sensors)):
                self.sensors[i].reset()
                self.sensor_values[i] = None
            self.value = 0

    def __str__(self):
        s = str(self.__class__.__name__)[0:-1] + "Sensob["
        s += "value: "
        if isinstance(self.value, float):
            s += str("%.2f" % self.value)
        else:
            s += str(self.value)
        s += ", "
        s += "active: " + str(self.active_flag) + "]"
        return s
