from motor_recommendation import Motor_recommendation
from random import choices
class Arbitrator:
    def __init__(self, bbcon, deterministic):
        self.bbcon = bbcon                                                      #Points to bbcon
        self.deterministic = deterministic                                      #Deterministic or stochastick?
        self.recommendations = []                                               #Fills with MR


    def choose_action(self, weights):
        """Should return a touple containing: motor recommendation (one pr. motob) and boolean indicating
        if the run should be halted or not"""
        self.recommendations.clear()                                            #Clears old recommendations

        for x in self.bbcon.active_behaviours:                                  #Fils the recommendations
            self.recommendations.append(x)

        if(self.deterministic):
            return self.choose_action_deterministic()
        else:
            return self.choose_action_stochastic()


    def choose_action_deterministic(self):
        self.recommendations.sort(key=lambda x: x.weight, reverse=True)  # Sort the recommendations in decreasing order
        return (self.recommendations[0], self.recommendations[0].hold_flag)


    def choose_action_stochastic(self):
        total_weight = 0                                                        #The total weight of all MR
        for x in self.recommendations:
            total_weight +=x.weight

        probability = []                                                        #Probability for each MR
        for x in self.recommendations:
            probability.append(x.weight/total_weight)

        mr = choices(self.recommendations, weights = probability, k = 1)        #Returns list with 1 element
        return (mr[0],mr[0].hold_flag)                                          #Returns (MR, hold_flag)


