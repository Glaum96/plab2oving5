

class MotorRecommendation:

    def __init__(self):
        self.weight = 0.0                                           # The weight of the MR (float)
        self.halt_request = False                                   # Halt flag (terminates code run)
        self.recommendation = None                                  # The recommendation tuple: (str, int) (see below)
        """
        ("S", x) = Rotate a little to the to either left or right, x > 0 rotate right, x < 0 rotate left
        ("L", x) = Turn left with difference x between the wheels
        ("R", x) = Turn left with difference x between the wheels
        ("F", x) = Drive straight forward with speed x
        ("B", x) = Drive straight backward with speed x
        """

    def update(self, weight, recommendation, halt_request=False):
        # Used when updating the values
        self.weight = weight
        self.halt_request = halt_request
        self.recommendation = recommendation
