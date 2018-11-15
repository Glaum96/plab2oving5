from bbcon import BBCON
from behavior import Behavior
from sensob import Sensob
from motob import Motob
from motors import Motors
from arbitrator import Arbitrator
from zumo_button import ZumoButton
from findRedSensob import FindRedSensob
from findAndFollowRedBallBehavior import FindAndFollowRedBallBehavior
import time


def main():
    bbcon1 = BBCON()  # Create BBCON

    # Motors
    motor1 = Motors()  # Create a Motor
    motob1 = Motob(motor1)  # Create a motob
    bbcon1.motobs = [motob1]  # Give Motor to BBCON

    zumo_button = ZumoButton()  # Sets up pins and Zumobutton

    # Add setup for camera, and add it to BBCON when we want to test everything together
    camera_sensor = FindRedSensob()  # Create obstacle sensob
    find_and_follow_behavior = FindAndFollowRedBallBehavior(bbcon1, 3)  # Create obstacle Behavior
    camera_sensor.add_behavior(find_and_follow_behavior)  # Give sensob the behavior

    bbcon1.add_behavior(find_and_follow_behavior)  # Give BBCON the behavior
    bbcon1.add_sensob(camera_sensor)

    motor1.stop()  # Stop all motors

    print("\nAll creation is done, entering main loop\n")

    q = ""
    while q is not 'q':
        zumo_button.wait_for_press()

        for i in range(0, 100):
            bbcon1.run_one_timestep()
        motor1.stop()
        q = input("Press 'q' to quit: ")
