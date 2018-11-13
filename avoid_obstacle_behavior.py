from behavior import Behavior
from motor_recommendation import Motor_recommendation

class AvoidObstacleBehavior(Behavior):

    def __init__(self, bbcon, priority):
        Behavior.__init__(self,bbcon,priority)

    def add_sensob(self, sensob):  # Adds sensob, as long as it is not already in the list
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)
            # Add this Behavior-object to the sensob's list, so that both points to each other
            sensob.add_behavior(self)

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        if self.sensobs[0].value > 5:
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        if self.sensobs[0].value <= 5:
            self.active_flag = True
            self.bbcon.activate_behaviour(self)

    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        print("behavior value: ", self.sensobs[0].value)
        self.match_degree = 5 / self.sensobs[0].value
        if self.active_flag and self.sensobs[0].value < 5:
            self.motor_recommendation = Motor_recommendation('B',300)
        else:
            self.motor_recommendation = Motor_recommendation('F',300)

        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation,halt_request)
