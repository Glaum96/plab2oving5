import time
from arbitrator import Arbitrator

class BBCON():

    def __init__(self):
        self.behaviours = []
        self.active_behaviours = []
        self.inactive_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self,True)
        self.current_timestep = 0
        # self.currentRobot = 0

    def add_behaviour(self,behaviour):
        self.behaviours.append(behaviour)
        self.inactive_behaviours.append(behaviour)

    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

    def activate_behaviour(self,behaviour):
        if behaviour in self.behaviours and behaviour in self.inactive_behaviours:
            self.inactive_behaviours.remove(behaviour)
            self.active_behaviours.append(behaviour)
        else:
            print("Behaviour not known or already activated.")

    def deactivate_behaviour(self,behaviour):
        if behaviour in self.behaviours and behaviour in self.active_behaviours:
            self.inactive_behaviours.append(behaviour)
            self.active_behaviours.remove(behaviour)
        else:
            print("Behaviour not known or already deactivated.")

    def run_one_timestep(self):
        #Update all sensobs.
        for i in self.sensobs:
            if i.active_flag:
                i.update()

        #Update all behaviours
        for i in self.behaviours:
            i.update()

        #Receive actions for each motob object, and a flag for if the robot should halt.
        which_actions,should_halt = self.arbitrator.choose_action()

        #Updates the motobs with their corresponing action (MR) from the arbitrator.
        for i in range(len(which_actions)):
            self.motobs[i].update(which_actions[i])

        #Waits so that the motors can start. idk.
        time.sleep(0.5)

        #Reset all sensobs.
        for i in self.sensobs:
            i.reset()
