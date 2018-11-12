from motor_recommendation import MotorRecommendation
#from random import choices


class Arbitrator:

    def __init__(self, bbcon, deterministic):
        self.bbcon = bbcon                                                      #Points to bbcon
        self.deterministic = deterministic                                      #Deterministic?
        self.recommendations = []                                               #A list of motor_recommendations


    def choose_action(self, recommendations):
        """Should return a touple containing: motor recommendation (one pr. motob) and boolean indicating
        if the run should be halted or not"""
        #Fjern klammeparentes rundt recommendations
        self.recommendations = [recommendations]                                  #Fils the recommendations

        if(self.deterministic):
            return self.choose_action_deterministic()
        else:
            return self.choose_action_stochastic()


    def choose_action_deterministic(self):
        self.recommendations.sort(key=lambda x: x.weight, reverse=True)  # Sort the motor_recommendations by weight
        return (self.recommendations[0], self.recommendations[0].halt_request)


    def choose_action_stochastic(self):
        total_weight = 0                                                        #The total weight of all MR
        for x in self.recommendations:
            total_weight +=x.weight

        probability = []                                                        #Probability for each MR
        for x in self.recommendations:
            probability.append(x.weight/total_weight)

        #mr = choices(self.recommendations, weights = probability, k = 1)        #Returns list with 1 element
        return (mr[0].recommendation,mr[0].hold_flag)                           #Returns (MR, hold_flag)


