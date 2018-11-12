from curses import *
import curses
from append import append
from Append_actuator import *
from Append_sensor import *
from menu import menu

class device_append(menu):
    list = ['Actuator','Sensor']
    def __init__(self,Room_name):
        self.curses_init()
        self.Room_name = Room_name
    def go_next(self):
        if self.now == 0:
            actuator = Append_actuator()
            actuator.append_menu(self.Room_name)
        elif self.now == 1:
            sensor = Append_sensor()
            sensor.append_menu(self.Room_name)





