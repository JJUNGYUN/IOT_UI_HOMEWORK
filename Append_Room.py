from Room_list import *
import Room_list
from append import append
class Append_room(append):
    defalut = {'Device': [], 'dcnt': '0'}

    def append_menu(self):
        self.window.addstr("Name : ")
        self.name = self.read_ch()
        self.list[self.name] = self.defalut
        self.save_json()
        Roomlist = Room_list.Room_list(self.window)
        Roomlist.print_list()


