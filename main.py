from bbcon import BBCON
from behavior import Behavior
from sensob import Sensob
from motob import Motob
from motors import Motors
from ir_sensob import IRSensob
from follow_line_behavior import FollowLineBehavior
from arbitrator import Arbitrator
from zumo_button import ZumoButton

def main():

    bbcon1 = BBCON()

    line_sensor = IRSensob()
    line_follow = FollowLineBehavior(bbcon1, 1)
    line_follow.add_sensob(line_sensor)
    bbcon1.add_behavior(line_follow)
    bbcon1.add_sensob(line_sensor)

    motor1 = Motors()
    motob1 = Motob(motor1)
    bbcon1.motobs = [motob1]
    zumo_button = ZumoButton()
    zumo_button.wait_for_press()
    for i in range(0, 50):
        bbcon1.run_one_timestep()
        print("Iteration ", i)
    motor1.stop()




