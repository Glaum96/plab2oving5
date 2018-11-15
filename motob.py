from motors import Motors
from motor_recommendation import MotorRecommendation

class Motob:
    def __init__(self, motors):
        #Motors is a list of motors whose settings will be determined by moton
        self.motors = motors
        self.command = None
        self.degree = None
        self.halt_request = False
        """self.motor_dict = {
            "S" : self.motors.set_value(self.degree),     #Rotate a little to the way given, -minus is left
            "L" : self.motors.left(self.degree),
            "R" : self.motors.right(self.degree),
            "F" : self.motors.forward(self.degree),
            "B" : self.motors.backward(self.degree)
            "H" : self.motors.stop()
        }

        (S,x) = Rotate a little to the to either left or right, x > 0 rotate right, x< 0 rotate left
        (L,x) = Turn left with difference x between the wheels
        (R,x) = Turn right with difference x between the wh
        (F,x) = Drive straight forward with speed x
        (B,x) = Drive straight backward with speed x
        (T,x) = Rotate in place for 0.5 sec to right or left, depending on x. x<0 rotates clockwise
        (H,x) = Hold still
        """

    def update(self, mr_touple):
        #mr is motor_(recommendation, hold_flag)
        (recommendation , flag) = mr_touple
        self.halt_request = flag
        print("Recommendation: ", recommendation)
        (self.command,self.degree) = recommendation
        self.operationalize()

    def operationalize(self):
        #Convert a motor recommendation into one or more motor settings, and sends to motor(s) using motor_dict or elseif
        if self.halt_request:
            self.motors.stop()
            exit()
        elif self.command == "H":
            self.motors.stop()
        elif self.command == "S":              #What about timing?
            if self.degree < 0:
                self.motors.set_value([0.4, -0.4])
            else:
                self.motors.set_value([-0.4, 0.4])
        elif self.command == "L":
            self.motors.left(self.degree)
        elif self.command == "R":
            self.motors.right(self.degree)
        elif self.command == "F":
            self.motors.forward(self.degree)
        elif self.command == "B":
            self.motors.backward(self.degree)
        elif self.command == "T":
            """
            rep = abs(self.degree / 15)         #Hvor mange ganger man skal rotere
            rotate = rep * 0.18                 #Antall ganger ganget med 0.18
            if self.degree > 0:
                self.motors.set_value([0.5, -0.5],rotate)
            else:
                self.motors.set_value([0.5, -0.5], rotate)
            """

            if self.degree > 0:
                self.motors.set_value([0.5, -0.5], 0.5)
            else:
                self.motors.set_value([0.5, -0.5], 0.5)
        else:
            print("\n*********** ERROR: Illegal MR given to Motob **********\n")
            exit()
