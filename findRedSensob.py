from sensob import Sensob
from camera import Camera
from imager2 import Imager


class FindRedSensob(Sensob):

    def __init__(self):
        self.bilde = None
        self.red_list = [0,0,0,0,0]
        Sensob.__init__(self,[Camera()])


    def update(self):
        if super(FindRedSensob,self).update():
            self.take_picture()
            self.bilde = Imager('red_image.jpeg')
            self.red_list = [0, 0, 0, 0, 0]
            self.delta = self.bilde.xmax // 5
            self.make_image_wta()
            self.make_red_image()
            self.calculate_where_most_red()
            print(self.red_list)
            return self.red_list

    def take_picture(self):
        im = Imager(image=self.sensors[0].update()).scale(1,1)
        im.dump_image('red_image.jpeg')

    def reset(self):
        Sensob.reset(self)
        self.red_list = [0,0,0,0,0]

    def get_value(self):
        return self.red_list

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
