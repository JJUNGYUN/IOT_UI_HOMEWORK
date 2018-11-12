import curses
from curses import *
from menu import menu
import sub_menu
import Room_list
from Device_list import Device_list
class main_menu(menu):
    list = ['Room', 'Device', 'exit']
    def go_next(self):
        if self.now == 0:
            room = Room_list.Room_list(self.window)
            room.print_list()
        elif self.now == 1:
            device = Device_list(self.window)
            device.print_list()
        elif self.now == 2:
            return False
