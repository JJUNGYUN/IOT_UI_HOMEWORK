from append import *
import Room_list

class Append_actuator(append):
    defalut = {"name":"","Kind":"Actuator","Condition":"OFF"}

    def append_menu(self,Room_name):
        self.window.addstr("Name : ")
        self.name = self.read_ch()
        self.defalut["name"] = self.name
        self.list[Room_name]['Device'].append(self.defalut)
        self.list[Room_name]['dcnt'] = len(self.list[Room_name]['Device'])
        self.save_json()
        Roomlist = Room_list.Room_list(window=self.window)
        Roomlist.print_list()