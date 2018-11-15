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
from findAndFollowRedBallBehavior import FindAndFollowRedBallBehavior
from findRedSensob import FindRedSensob
from zumo_button import ZumoButton

from ultrasonic import Ultrasonic
import time



def main():

    zumo_button = ZumoButton()  # Sets up pins and Zumobutton
    zumo_button.wait_for_press()

    bbcon1 = BBCON()                                            # Create BBCON

    #Motors
    motor1 = Motors()                                           # Create a Motor
    motob1 = Motob(motor1)                                      # Create a motob

    bbcon1.motobs = [motob1]                                    # Give Motor to BBCON

    # Collision avoidance
    ultra_sensor = ObstacleDetectionSensob()                    # Create obstacle sensob
    avoid_object = AvoidObstacleBehavior(bbcon1, 1.5)             # Create obstacle Behavior
    ultra_sensor.add_behavior(avoid_object)                     # Give sensob the behavior

    bbcon1.add_behavior(avoid_object)                           # Give BBCON the behavior
    bbcon1.add_sensob(ultra_sensor)                             # Give BBCON the sensor

    # Line follow
    line_sensor = IRSensob()                                    # Create IR sensob
    line_follow = FollowLineBehavior(bbcon1, 0.5)                 # Create linefollow behavior
    line_follow.add_sensob(line_sensor)                         # Give linefollow sin sensob

    bbcon1.add_behavior(line_follow)                            # Give BBCON the linefollow
    bbcon1.add_sensob(line_sensor)                              # Give BBCON the IR sensob

    # Add setup for camera, and add it to BBCON when we want to test everything together
    camera_sensor = FindRedSensob()  # Create obstacle sensob
    find_and_follow_behavior = FindAndFollowRedBallBehavior(bbcon1, 1)  # Create obstacle Behavior
    camera_sensor.add_behavior(find_and_follow_behavior)  # Give sensob the behavior

    bbcon1.add_behavior(find_and_follow_behavior)  # Give BBCON the behavior
    bbcon1.add_sensob(camera_sensor)

    motor1.stop()                                               # Stop all motors

    print("\nAll creation is done, entering main loop\n")
    q = input("Press 'q' to quit: ")

    while q is not 'q':
                                                                #Runs 100 timesteps. Stops if q is pressed.
        for i in range(0, 100):
            print("\nIteration " + str(i))
            if bbcon1.run_one_timestep():
                motor1.stop()
                exit()
        motor1.stop()
        q = input("Press 'q' to quit: ")
