from behavior import Behavior
from findRedSensob import FindRedSensob
from camera import Camera
from imager2 import Imager
from behavior import Behavior
from bbcon import BBCON

class FindAndFollowRedBallBehavior(Behavior):

    def __init__(self,myBBCON,priority):
        myFindRedSensob = FindRedSensob()
        sensobs = [myFindRedSensob]
        Behavior.__init__(self,myBBCON,priority)
        print("Self.sensobs[0].get_value():",self.sensobs[0].get_value())
        self.sensobs[0].update()
        print("Self.sensobs[0].get_value():",self.sensobs[0].get_value())
        self.red_list = self.sensobs[0].get_value()

    def consider_deactivation(self):
        self.sensobs[0].update()
        if max(self.red_list) < 300:
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)


    def consider_activation(self):
        if max(self.red_list >= 300):
            self.active_flag = True
            self.bbcon.activate_behaviour(self)

    def sense_and_act(self):
        print("behavior value: ", self.sensobs[0].value)
        if max(self.red_list < 500):
            which_fifth = max(self.red_list)
            degrees = 30-which_fifth*15
            if abs(degrees) > 10:
                motor_recommendation = ('F',0.3)
            else:
                motor_recommendation = ('T',degrees)
        else:
            motor_recommendation = ('J',1)

        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation)
