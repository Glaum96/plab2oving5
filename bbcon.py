import time
from arbitrator import Arbitrator


class BBCON():

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self,True)
        self.current_timestep = 0
        # self.currentRobot = 0

    def add_behavior(self,behavior):
        self.behaviors.append(behavior)
        # Adds to active instead of inact   ive
        self.active_behaviors.append(behavior)

    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self,behavior):
        if behavior in self.inactive_behaviors:
            self.inactive_behaviors.remove(behavior)
            self.active_behaviors.append(behavior)
        else:
            print("behavior not known or already activated.")

    def deactivate_behavior(self,behavior):
        if behavior in self.active_behaviors:
            self.inactive_behaviors.append(behavior)
            self.active_behaviors.remove(behavior)
        else:
            print("behavior not known or already deactivated.")

    def run_one_timestep(self):
        # Update all sensobs.
        for i in self.sensobs:
            i.update()

        # Update all behaviors
        for i in self.behaviors:
            i.update()

        # BBCON creates list of motor_recommendation objects from active_behaviors
        motor_recommendations = []
        for rec in self.active_behaviors:
            print(rec.__class__.__name__, " weight: ", rec.motor_recommendation.weight)
            motor_recommendations.append(rec.motor_recommendation)

        # Receive actions for each motob object, and a flag for if the robot should halt.
        # Input argument was made above
        if len(motor_recommendations) is 0:
            print("\nNo recomendations, exiting...\n")
            exit()
        which_actions, should_halt = self.arbitrator.choose_action(motor_recommendations)

        # This is commented out as there are only one motob
        # Updates the motobs with their corresponing action (MR) from the arbitrator.
        #for i in range(len(which_actions)):
            #self.motobs[i].update(which_actions[i])
        self.motobs[0].update((which_actions, should_halt))

        # Waits so that the motors can start. idk.
        time.sleep(0.25)

        # Reset all sensobs.
        for i in self.sensobs:
            i.reset()

        return should_halt
