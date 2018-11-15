from sensob import Sensob
from behavior import Behavior
from bbcon import BBCON
import time
from ultrasonic import Ultrasonic


class ObstacleDetectionSensob(Sensob):

    # Parameter sensors is a list of sensor objects,
    # behaviors a set of Behavior objects
    def __init__(self):
        Sensob.__init__(self, [Ultrasonic()])

    #Updates teh sensor values in the super-update. Updates its own value and returns it.
    def update(self):
        if super(ObstacleDetectionSensob,self).update():
            self.value = self.sensor_values[0]
            return self.value


