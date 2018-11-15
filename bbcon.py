import time
from arbitrator import Arbitrator


class BBCON():

    def __init__(self):
        self.behaviors = []                                     # Stores all behaviors
        self.active_behaviors = []                              # Stores the active behaviors
        self.inactive_behaviors = []                            # Stores the inactive behaviors
        self.sensobs = []                                       # Stores the sensobs
        self.motobs = []                                        # Stores the motob
        self.arbitrator = Arbitrator(self,True)                 # Createas and stores a deterministic arbitrator
        self.current_timestep = 0                               # Timestep at start is 0

    def add_behavior(self,behavior):
        #Adds a behavior
        self.behaviors.append(behavior)
        # Adds to active instead of inactive
        self.active_behaviors.append(behavior)

    def add_sensob(self,sensob):
        #Adds a sensob
        self.sensobs.append(sensob)

    def activate_behavior(self,behavior):
        # Activates a behavior
        if behavior in self.inactive_behaviors:
            self.inactive_behaviors.remove(behavior)
            self.active_behaviors.append(behavior)
        else:
            print("behavior not known or already activated.")

    def deactivate_behavior(self,behavior):
        # Deactivates a behavior
        if behavior in self.active_behaviors:
            self.inactive_behaviors.append(behavior)
            self.active_behaviors.remove(behavior)
        else:
            print("behavior not known or already deactivated.")

    def run_one_timestep(self):
        #The main function of BBCON

        # Update all sensobs.
        for sensob in self.sensobs:
            sensob.update()
            print(sensob)

        # Update all behaviors
        for sensob in self.behaviors:
            sensob.update()

        # BBCON creates list of motor_recommendation objects from active_behaviors
        motor_recommendations = []
        for behavior in self.active_behaviors:
            print(behavior)
            motor_recommendations.append(behavior.motor_recommendation)

        # Receive actions for each motob object, and a flag for if the robot should halt.
        # Input argument was made above
        if len(motor_recommendations) is 0:
            print("\nNo recommendations, exiting...\n")
            return True
        which_actions, should_halt = self.arbitrator.choose_action(motor_recommendations)

        # This is commented out as there are only one motob
        # Updates the motobs with their corresponing action (MR) from the arbitrator.
        #for i in range(len(which_actions)):
            #self.motobs[i].update(which_actions[i])
        self.motobs[0].update((which_actions, should_halt))

        # Waits so that the motors can start. idk.
        #time.sleep(0.25)           I removed this sleep, as it was added in motob instead.

        # Reset all sensobs.
        for sensob in self.sensobs:
            sensob.reset()

        return should_halt