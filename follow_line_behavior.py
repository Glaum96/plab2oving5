from behavior import Behavior
from motor_recommendation import MotorRecommendation

class FollowLineBehavior(Behavior):
    def __init__(self,bbcon, priority):
        super().__init__(bbcon, priority)
        #self.counter = 0            #Just for testing, stops the robot after a few seconds

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        pass

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        pass


    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        #self.counter = self.counter +1

        value = self.sensobs[0].get_value()
        self.match_degree = 0.4
        halt_request = False
        if value == -1:
            motor_recommendation = ("H", 0.0)
            halt_request = True
            self.priority = 100
        elif value == -2:                       #This means that all readings are outside the line
            motor_recommendation = ("R", 0.4)
            self.match_degree = 0.01
        elif value == 0:
            motor_recommendation = ("S", 1)
            self.match_degree = 1
        elif value == 5:
            motor_recommendation = ("S", -1)
            self.match_degree = 1
        elif value < 2:
            motor_recommendation = ("L", 0.4)
            self.match_degree = 0.6
        elif value > 3:
            motor_recommendation = ("R", 0.4)
            self.match_degree = 0.6
        else:
            motor_recommendation = ("F", 0.2)

        weight = self.priority * self.match_degree

        self.motor_recommendation.update(weight, motor_recommendation, halt_request)
