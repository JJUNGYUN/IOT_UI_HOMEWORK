from Print.menu import  menu
from Append.Sensor import Append_sensor
from Append.Actuator import Append_actuator
from Print.Sensor_list import Sensor_list
from Print.Actuator_list import Actuator_list
class device_append(menu):
    list = ['Actuator','Sensor','exit']

    def __init__(self,Room_name,window):
        self.Room_name = Room_name
        self.window = window
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()
        #self.print_list()



    def go_next(self):
        if self.now == 0:
            Actuator_list(self.window, self.Room_name).print_list()
            #actuator = Append_actuator(self.window)
            #actuator.append_menu(self.Room_name)
        elif self.now == 1:
            Sensor_list(self.window,self.Room_name).print_list()
            #sensor = Append_sensor(self.window)
            #sensor.append_menu(self.Room_name)
        elif self.now == 2:
            return True

