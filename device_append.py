from curses import *
import curses
from append import append
from Append_actuator import *
from Append_sensor import *
from menu import menu

class device_append(menu):
    list = ['Actuator','Sensor']

    def __init__(self,Room_name,window):
        self.Room_name = Room_name
        self.window = window
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()
        self.print_list()


    def go_next(self):
        if self.now == 0:
            actuator = Append_actuator(self.window)
            actuator.append_menu(self.Room_name)
        elif self.now == 1:
            sensor = Append_sensor(self.window)
            sensor.append_menu(self.Room_name)





