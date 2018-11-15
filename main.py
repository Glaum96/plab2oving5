from bbcon import BBCON
from behavior import Behavior
from sensob import Sensob
from motob import Motob
from motors import Motors
from obstacle_detection_sensob import ObstacleDetectionSensob
from avoid_obstacle_behavior import AvoidObstacleBehavior
from ir_sensob import IRSensob
from follow_line_behavior import FollowLineBehavior
from arbitrator import Arbitrator
from zumo_button import ZumoButton

from ultrasonic import Ultrasonic
import time



def main():
    bbcon1 = BBCON()                                            # Create BBCON

    #Motors
    motor1 = Motors()                                           # Create a Motor
    motob1 = Motob(motor1)                                      # Create a motob

    bbcon1.motobs = [motob1]                                    # Give Motor to BBCON

    # Collision avoidance
    ultra_sensor = ObstacleDetectionSensob()                    # Create obstacle sensob
    avoid_object = AvoidObstacleBehavior(bbcon1, 1)             # Create obstacle Behavior
    ultra_sensor.add_behavior(avoid_object)                     # Give sensob the behavior

    bbcon1.add_behavior(avoid_object)                           # Give BBCON the behavior
    bbcon1.add_sensob(ultra_sensor)                             # Give BBCON the sensor

    # Line follow
    line_sensor = IRSensob()                                    # Create IR sensob
    line_follow = FollowLineBehavior(bbcon1, 1)                 # Create linefollow behavior
    line_follow.add_sensob(line_sensor)                         # Give linefollow sin sensob

    bbcon1.add_behavior(line_follow)                            # Give BBCON the linefollow
    bbcon1.add_sensob(line_sensor)                              # Give BBCON the IR sensob

    print("\nAll creation is done, entering main loop\n")

    q = ""
    while q is not 'q':
        zumo_button = ZumoButton()
        zumo_button.wait_for_press()

        for i in range(0, 100):
            bbcon1.run_one_timestep()
        motor1.stop()
        q = input("Press 'q' to quit: ")
