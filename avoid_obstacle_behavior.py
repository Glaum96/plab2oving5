from behavior import Behavior
from motor_recommendation import MotorRecommendation

class AvoidObstacleBehavior(Behavior):
    """This behavior prevents the robot from driving into an abstacle in front of it.
    The motor_recommendation from this behavior is always to stop, but the match degree changes depending
    on how close it is to the object."""
    def __init__(self, bbcon, priority):
        Behavior.__init__(self,bbcon,priority)

    def add_sensob(self, sensob):  # Adds sensob, as long as it is not already in the list
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)
            # Add this Behavior-object to the sensob's list, so that both points to each other
            sensob.add_behavior(self)

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        if 20 < self.sensobs[0].value < 3000:               #Deactivate if not any dangers
            self.active_flag = False
            self.bbcon.deactivate_behavior(self)

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        if (self.sensobs[0].value <= 20                     #Activate if danger
                or self.sensobs[0].value > 3000):
            self.active_flag = True
            self.bbcon.activate_behavior(self)

    # Performs the actual computations based on Sensob-values to produce
    # match degree and  potential halt request
    def sense_and_act(self):
        #Calculate match degreee
        self.match_degree = 5 / (self.sensobs[0].value + 0.01)
        if self.match_degree > 1:
            self.match_degree = 1
        elif self.match_degree < 0.8:
            self.match_degree = 0.01
        motor_recommendation = ('H',0.0)                    # Motor recommendation is always to stop

        if self.sensobs[0].value == 0:
            self.match_degree = 0                           # If we are reading a bogus value

        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation,
                                         self.motor_recommendation.halt_request)
