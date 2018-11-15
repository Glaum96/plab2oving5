from behavior import Behavior
from motor_recommendation import MotorRecommendation

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
        if self.sensobs[0].value > 20:
            self.active_flag = False
            self.bbcon.deactivate_behavior(self)

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        if self.sensobs[0].value <= 20:
            self.active_flag = True
            self.bbcon.activate_behavior(self)

    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        self.match_degree = 5 / (self.sensobs[0].value + 0.01)
        if self.match_degree > 1:
            self.match_degree = 1
        if self.active_flag and self.sensobs[0].value < 5.2:
            motor_recommendation = ('H',0.0)
        else:
            motor_recommendation = ('F',0.2)
           
        if self.sensobs[0].value == 0:
            motor_recomendation = ('H',0.0)
            self.match_degree = 0
        #if self.sensobs[0].value < 1:
        #    self.motor_recommendation.halt_request = True
        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation,
                                         self.motor_recommendation.halt_request)
