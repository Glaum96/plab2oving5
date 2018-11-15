from motor_recommendation import MotorRecommendation
#from random import choices


class Arbitrator:
    """This is the arbitrator. It choses one of the recommendations it receives. The choise can
    be stochastic or deterministic."""
    def __init__(self, bbcon, deterministic):
        self.bbcon = bbcon                                                      # Points to bbcon
        self.deterministic = deterministic                                      # Deterministic?
        self.recommendations = []                                               # A list of motor_recommendations


    def choose_action(self, recommendations):
        """Is called from the BBCON. Cals a help function which choses a recommendation, either deterministic or
        stochastic."""
        self.recommendations = recommendations                                  # Stores the recommendations

        if(self.deterministic):                                                 # Chose correct help-method
            return self.choose_action_deterministic()
        else:
            return self.choose_action_stochastic()


    def choose_action_deterministic(self):
        """Choses a motor_recommendations deterministic
        Sorts all recomendations in decreasing order, depending on their weight and returns the first element"""
        self.recommendations.sort(key=lambda x: x.weight, reverse=True)  # Sort the motor_recommendations by weight

        return (self.recommendations[0].recommendation, self.recommendations[0].halt_request)


    def choose_action_stochastic(self):
        """Choses a motor_recommendation stochasticly.
        Creates a list of probabilities depending on each recomendations weight, and chooses one, given the matching
        probability"""
        total_weight = 0                                                        #The total weight of all MR
        for x in self.recommendations:
            total_weight +=x.weight

        probability = []                                                        #Probability for each MR
        for x in self.recommendations:
            probability.append(x.weight/total_weight)

        #mr = choices(self.recommendations, weights = probability, k = 1)        #Returns list with 1 element
        #return (mr[0].recommendation,mr[0].hold_flag)                           #Returns (MR, hold_flag)


