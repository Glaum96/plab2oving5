from sensob import Sensob
from camera import Camera
from imager2 import Imager


class FindRedSensob(Sensob):

    def __init__(self):
        self.bilde = None
        self.value = [0,0,0,0,0]                    #Makes the list with red pixels
        Sensob.__init__(self,[Camera()])            #Super-constructor with the camera-sensor.


    def update(self):
        if super(FindRedSensob,self).update():      #Run the super-update, to update the sensor values.  
            self.take_picture()                     #Takes the picture and stores it on the rpi.
            self.bilde = Imager('red_image.jpeg')   #Accesses the picture.
            self.value = [0, 0, 0, 0, 0]            #Resets the list.
            self.delta = self.bilde.xmax // 5       #Divides the picture into 5 equal columns.
            self.make_image_wta()                   #Performs a winner-take-all-function to make every pixel only red, green or blue.
            self.make_red_image()                   #Makes all green and blue pixels black, and maximizes the red in the red pixels.
            self.calculate_where_most_red()         #Calculates wich fith has the most red, and returns the list as the self.value.
            
            return self.value

    def take_picture(self):
        im = Imager(image=self.sensors[0].update()).scale(1,1)  #Takes the picture.
        im.dump_image('red_image.jpeg')                         #Stores the picture.

    def reset(self):
        Sensob.reset(self)
        self.value = [0,0,0,0,0]

    def get_value(self):
        return self.value

    def is_red_pixel(self,x,y):
        pixel = self.bilde.get_pixel(x,y)
        if pixel[0] > pixel[1] and pixel[0] > pixel[2] and pixel[0] > 50:
            return True

    def make_image_wta(self):                       #Performs a winner-take-all-function to make every pixel only red, green or blue.
        self.bilde = self.bilde.map_color_wta()

    def make_red_image(self):                       #Makes all green and blue pixels black, and maximizes the red in the red pixels.
        for i in range(self.bilde.xmax):
            for j in range(self.bilde.ymax):
                if self.is_red_pixel(i,j):
                    self.bilde.set_pixel(i,j,(255,0,0))
                else:
                    self.bilde.set_pixel(i,j,(0,0,0))
                                                              
    def calculate_where_most_red(self):             #Calculates wich fith has the most red, and returns the list as the self.value
        for i in range(self.bilde.xmax):
            for j in range(self.bilde.ymax):
                if self.is_red_pixel(i,j):
                    which_fifth = i//self.delta
                    #print("which fifth: ", which_fifth)
                    self.value[which_fifth - 1] += 1
