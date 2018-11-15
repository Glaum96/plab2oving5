from bbcon import BBCON
from behavior import Behavior
from sensob import Sensob
from motob import Motob
from motors import Motors
from findRedSensob import FindRedSensob
from findAndFollowRedBallBehavior import FindAndFollowRedBallBehaviour
from arbitrator import Arbitrator
from zumo_button import ZumoButton

def main():

    bbcon1 = BBCON()

    motor1 = Motors()
    #motob1 = Motob(motor1)
    #bbcon1.motobs = [motob1]

    cam_sensor = FindRedSensob
    find_ball = FindAndFollowRedBallBehaviour(bbcon1, 1)
    find_ball.add_sensob(cam_sensor)
    bbcon1.add_behavior(find_ball)
    bbcon1.add_sensob(cam_sensor)
    """
    line_sensor = IRSensob()
    line_follow = FollowLineBehavior(bbcon1, 1)
    line_follow.add_sensob(line_sensor)
    bbcon1.add_behavior(line_follow)
    bbcon1.add_sensob(line_sensor)
    """
    zumo_button = ZumoButton()
    zumo_button.wait_for_press()

    #motob1.update((("T", 1),False))
    for i in range(0, 300):
        bbcon1.run_one_timestep()
        print("Iteration ", i)
    motor1.stop()

