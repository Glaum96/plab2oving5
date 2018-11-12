from behavior import Behavior
from motor_recommendation import MotorRecommendation

class FollowLineBehavior(Behavior):
    def __init__(self,bbcon, priority):
        super().__init__(bbcon, priority)

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        pass

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        pass


    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        print("behavior value: ", self.sensobs[0].value)
        self.match_degree =
        self.motor_recommendation.weight = self.priority * self.match_degree              #Set the weight
        #Set hold_flag
        #Set MS


