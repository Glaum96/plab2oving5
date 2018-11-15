from behavior import Behavior
from findRedSensob import FindRedSensob
from camera import Camera
from imager2 import Imager
from behavior import Behavior
from bbcon import BBCON

class FindAndFollowRedBallBehavior(Behavior):
    """This is the bahavior which finds and follows the red item"""
    def __init__(self,myBBCON,priority):
        Behavior.__init__(self,myBBCON,priority)

    def consider_deactivation(self):
        # Check if we should activate
        if max(self.sensobs[0].value) < 0:  # CHANGE LATER
            self.active_flag = False
            self.bbcon.deactivate_behavior(self)


    def consider_activation(self):
        # Checks if we should deactivate
        if max(self.sensobs[0].value) >= 100:
            self.active_flag = True
            self.bbcon.activate_behavior(self)

    def sense_and_act(self):
        # This method creates the match degree and the motor_recommendation
        which_fifth = 0                                         # Is the fift of the view containg most read
        # Finds out where the most red is
        maximum = self.sensobs[0].value[0]
        for i in range(1,len(self.sensobs[0].value)):
            if self.sensobs[0].value[i] > maximum:
                maximum = self.sensobs[0].value[i]
                which_fifth = i

        self.match_degree = maximum / 500                       # Match degree is the max amount of red pixels / 500
        if self.match_degree > 1:                               # if we get more than 1, we set match_degree to 1
            self.match_degree = 1

        # Decides what the motor_recommendation should be, given where we found most red
        if max(self.sensobs[0].value) > 100:           # If we saw a lot of red
            if which_fifth == 2 or (self.sensobs[0].value[2]-self.sensobs[0].value[1] < 50) \
                    or (self.sensobs[0].value[2]-self.sensobs[0].value[3] < 50):
                motor_recommendation = ('F',0.3)       # The most red was in front of us or, it was close to equally red
            elif which_fifth == 0 or which_fifth == 1:
                motor_recommendation = ('T', -1)       # We Locate the most red to the right of front
            else:
                motor_recommendation = ('T', 1)        # We located the most red to the left
        else:
            motor_recommendation = ('J', 1)            # We have not found  a lot of red, so we rotate a lot

        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation)
