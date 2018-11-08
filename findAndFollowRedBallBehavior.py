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
        pass

    def consider_activation(self):
        pass
