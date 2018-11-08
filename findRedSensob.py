from sensob import Sensob
from camera import Camera
from imager2 import Imager
from behavior import Behavior
from bbcon import BBCON

class FindRedSensob(Sensob):

    def __init__(self):
        self.camera = Camera()
        self.myBBCON = BBCON()
        self.find_and_follow_red_ball = Behavior(self.myBBCON,self,1)
        behaviours = [self.find_and_follow_red_ball]
        sensors = [self.camera]
        Sensob.__init__(self,sensors,behaviours)
        self.bilde = Imager('testingMagnus.jpg')
        self.delta = self.bilde.xmax//5
        self.red_list = [0,0,0,0,0]

    def update(self):
        self.bilde = Imager(self.camera.update())

    def is_red_pixel(self,x,y):
        pixel = self.bilde.get_pixel(x,y)
        if pixel[0] > pixel[1] and pixel[0] > pixel[2] and pixel[0] > 50:
            return True

    def make_image_wta(self):
        self.bilde = self.bilde.map_color_wta()

    #Must be run after make_image_wta
    def make_red_image(self):
        for i in range(self.bilde.xmax):
            for j in range(self.bilde.ymax):
                if self.is_red_pixel(i,j):
                    self.bilde.set_pixel(i,j,(255,0,0))
                else:
                    self.bilde.set_pixel(i,j,(0,0,0))

    #Mest be run after make_red_image
    def calculate_where_most_red(self):
        for i in range(self.bilde.xmax):
            for j in range(self.bilde.ymax):
                if self.is_red_pixel(i,j):
                    which_fifth = i//self.delta
                    self.red_list[which_fifth] += 1

    #Must be run after calculate_where_most_red
    def make_mr(self):
        if max(self.red_list < 500):
            which_fifth = max(self.red_list)
            degrees = 30-which_fifth*15
            if abs(degrees) > 10:
                mr = (('F',300),False)
            else:
                mr = (('S',degrees),False)

        else:
            mr = (('S'),60,False)
        return mr

test = FindRedSensob()
test.bilde.display()
test.make_image_wta()
test.bilde.display()
test.make_red_image()
test.bilde.display()
test.calculate_where_most_red()
print(test.red_list)
