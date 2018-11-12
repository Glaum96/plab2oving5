from motor_recommendation import MotorRecommendation


class Behavior:

    def __init__(self, bbcon, priority):
        self.bbcon = bbcon
        self.sensobs = []  # Set of sensobs that the Behavior object updates based on
        self.motor_recommendation = MotorRecommendation()  # MR object: contains MR,
        self.active_flag = True  # Indicates whether Behavior is active or not
        self.priority = priority  # Given constant indicating how much this Behavior-object should be prioritized
        self.match_degree = 0.0  # Float in the range [0.0, 1.0] indicating how much situation matches behavior

    def add_sensob(self, sensob):  # Adds sensob, as long as it is not already in the list
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)
            # Add this Behavior-object to the sensob's list, so that both points to each other
            sensob.add_behavior(self)

    # Sets active_flag to False given certain conditions (OPTIONAL to define)
    def consider_deactivation(self):
        pass

    # Sets active_flag to True given certain conditions (OPTIONAL to define)
    def consider_activation(self):
        pass

    # Updates all the values of the Sensobs that the Behavior points to
    # NOTE: DO NOT REDEFINE update()-method in subclasses
    def update(self):
        # Performs tests first to see whether object should (de)activate or not
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        # And then performs updates if Behavior is active
        if self.active_flag and len(self.sensobs) != 0:
            self.sense_and_act()
            # match_degree must be calculated by sense_and_act()
            if not (0.0 <= self.match_degree <= 1.0):
                raise ValueError("Match_degree must be a float between 0 and 1, was ",
                                 self.match_degree)

    # Performs the actual computations based on Sensob-values to produce
    # motor_recommendations (MRs), potential halt request and match_degree
    def sense_and_act(self):
        raise NotImplementedError
        # REDEFINITION FORMAT:
        # def sense_and_act(self):
        #     ...
        #     Your code here - remember to define local variables
        #     motor_recommendation and halt_request (last one is optional)
        #     ...
        # self.motor_recommendation.update(self.priority * self.match_degree,
        #                                  motor_recommendation,
        #                                  halt_request)
        # NOTE: halt_request argument above can be left out from method call
