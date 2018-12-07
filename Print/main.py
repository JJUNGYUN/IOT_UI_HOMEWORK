from Print.menu import menu
from Print.Room import Room
from Print.Device import  Device
from Print.Search import Search
from curses import endwin

class main_menu(menu):
    list = ['Room', 'Device','search' ,'exit']
    def go_next(self):
        if self.now == 0:
            room = Room(self.window)
            room.print_list()
            self.print_list()
        elif self.now == 1:
            device = Device(self.window)
            device.print_list()
            self.print_list()
        elif self.now == 2:
            search = Search(self.window)
            search.print_list()
            self.print_list()
        elif self.now == 3:
            return False