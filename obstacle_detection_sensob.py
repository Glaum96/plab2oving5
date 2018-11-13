from sensob import Sensob
from behavior import Behavior
from bbcon import BBCON
import time
from ultrasonic import Ultrasonic


class ObstacleDetectionSensob(Sensob):

    # Parameter sensors is a list of sensor objects,
    # behaviors a set of Behavior objects
    def __init__(self):
        Sensob.__init__(self, [Ultrasonic()])

    # This is the method that calculates the value used by Behavior-objects,
    # will be overwritten in subclasses
    def update(self):
        if super(ObstacleDetectionSensob,self).update():
            print("ultrasonic sensor val: ", self.sensor_values[0])
            self.value = self.sensor_values[0]
            return self.value


def main():
    for i in range(0, 10):
        u_sens = ObstacleDetectionSensob()
        u_sens.update()
        time.sleep(0.5)
