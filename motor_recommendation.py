class Motor_recommendation():
    def __init__(self, weight, recommendation, hold_flag):
        self.weight = weight                                                #The weight of the MR
        self.hold_flag = hold_flag                                          #Hold flag
        self.recommendation = recommendation                                # The recommendation
        """
        ("S", x) = Rotate a little to the to either left or right, x > 0 rotate right, x < 0 rotate left
        ("L", x) = Turn left with difference x between the wheels
        ("R", x) = Turn left with difference x between the wheels
        ("F", x) = Drive straight forward with speed x
        ("B", x) = Drive straight backward with speed x
        """