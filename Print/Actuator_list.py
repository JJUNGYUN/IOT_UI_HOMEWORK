from Print.list import _list
import threading, time ,datetime
from curses import *
import json
from Append.Actuator import Append_actuator
class Actuator_list(_list):

    def __init__(self,window,Room_name):
        super(Actuator_list, self).__init__(window)
        self.Room_name = Room_name

    def load_json(self):
        with open("device_default.json", 'r') as f:
            self.default = json.load(f)
        self.list = list(self.default['Actuator'].keys())

    def enter_event(self):
        if self.now == len(self.list):
            return True
        else:
            Append_actuator(self.window).append_menu(self.Room_name,self.list[self.now])

    def append_event(self):
        pass


    def quit_event(self):
        pass

    def print_list(self):
        t1 = threading.Thread(target=self.get_key, args=())
        t1.start()
        self.window.erase()
        for i ,j in enumerate(self.list):
            if self.now == i:
                # No devicename Roomname Condition
                self.window.addstr(
                    "{0}\t{1} \n".format(i+1 , j),
                    color_pair(2))
            else:
                self.window.addstr(
                    "{0}\t{1} \n".format(i+1, j),
                    color_pair(1))

        if len(self.list) == self.now:
            self.window.addstr("{0}\t{1} \n".format(i+2,"exit"), color_pair(2))
        else:
            self.window.addstr("{0}\t{1} \n".format(i+2,"exit"), color_pair(1))

        self.window.refresh()
        while (t1.isAlive()):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timewin = newwin(1, 20, 0, self.maxx - 21)
            timewin.addstr(str(now), A_BOLD + color_pair(3))
            explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
            explain.addstr(
                "↑,↓ : Move menu / Enter : Show Select Device / q , Q : Previous page / p, P : Append device",
                A_BOLD + color_pair(3))

            timewin.refresh()
            explain.refresh()

        # self.move_curse()
        self.move_curse(len(self.list))
