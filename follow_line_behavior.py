from behavior import Behavior
from motor_recommendation import MotorRecommendation

class FollowLineBehavior(Behavior):
    def __init__(self,bbcon, priority):
        super().__init__(bbcon, priority)
        self.counter = 0            #Just for testing, stops the robot after a few seconds

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        pass

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        pass


    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        self.counter = self.counter +1

        value = self.sensobs[0].get_value()
        self.match_degree = 1
        recommendation = 0
        if value < 2:
            motor_recommendation = ("L", 0.2)
        elif value > 4:
            motor_recommendation = ("R", 0.2)
        else:
            motor_recommendation = ("F", 0.2)

        weight = self.priority * self.match_degree

        #Stops after 8 times
        if self.counter == 8:
            self.motor_recommendation.update(weight, motor_recommendation, True)
        else:
            self.motor_recommendation.update(weight,motor_recommendation, False)