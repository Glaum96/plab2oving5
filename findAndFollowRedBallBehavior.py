from behavior import Behavior
from findRedSensob import FindRedSensob
from camera import Camera
from imager2 import Imager
from behavior import Behavior
from bbcon import BBCON

class FindAndFollowRedBallBehaviour(Behavior):
    def __init__(self):
        myBBCON = BBCON()
        myFindRedSensob = FindRedSensob()
        sensobs = [myFindRedSensob]
        priority = 1
        Behavior.__init__(myBBCON,sensobs,priority)

    def consider_deactivation(self):
        self.sensobs[0].update()
        if max(self.sensobs[0].get_value() < 500):
            self.sensobs[0].update()
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)


    def consider_activation(self):
        if max(self.red_list >= 500):
            self.active_flag = True
            self.bbcon.activate_behaviour(self)

    def sense_and_act(self):
        print("behavior value: ", self.sensobs[0].value)
        #KODE
        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation,halt_request)
