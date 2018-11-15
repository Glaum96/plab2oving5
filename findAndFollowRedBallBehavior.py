from behavior import Behavior
from findRedSensob import FindRedSensob
from camera import Camera
from imager2 import Imager
from behavior import Behavior
from bbcon import BBCON

class FindAndFollowRedBallBehavior(Behavior):

    def __init__(self,myBBCON,priority):
        #myFindRedSensob = FindRedSensob()
        #self.sensobs = [myFindRedSensob]
        Behavior.__init__(self,myBBCON,priority)
        #print("Self.sensobs: ",self.sensobs)
        #self.sensobs[0].update()
        #print("Self.sensobs[0].get_value():",self.sensobs[0].get_value())
        self.sensobs[0].value = [0] * 5

    def consider_deactivation(self):
        #self.sensobs[0].update()
        print(self.sensobs[0].value)
        print("Max: ", max(self.sensobs[0].value))
        if max(self.sensobs[0].value) < 150:
            print("deactivating")
            self.active_flag = False
            self.bbcon.deactivate_behavior(self)


    def consider_activation(self):
        print("Max: ", max(self.sensobs[0].value))
        if max(self.sensobs[0].value) >= 150:
            print("activating")
            self.active_flag = True
            self.bbcon.activate_behavior(self)

    def sense_and_act(self):
        print("behavior value: ", self.sensobs[0].value)
        print("Now in sense_and_act-function")
        print("Red list:",self.sensobs[0].value)
        print("Max: ", max(self.sensobs[0].value))
        if max(self.sensobs[0].value) < 150:
            which_fifth = max(self.sensobs[0].value)
            degrees = 30-which_fifth*15
            if abs(degrees) > 10:
                motor_recommendation = ('F',0.3)
            else:
                motor_recommendation = ('T',degrees)
        else:
            motor_recommendation = ('J',1)

        self.motor_recommendation.update(self.priority * self.match_degree,motor_recommendation)
