from Print.list import _list
from curses import *
import threading, time ,datetime
from Print.append import device_append
from Print import device_format
class Room_device(_list):

    def __init__(self, window,Room_name):
        self.load_json()
        self.window = window
        self.Room_name = Room_name
        init_pair(4, COLOR_CYAN, COLOR_BLACK)
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()
        self.now_svl = 0
        self.showTF = []
        for i in range(len(self.list[self.Room_name]['Device'])):
            self.showTF.append(False)

    def enter_event(self):
        if self.now == len(self.list[self.Room_name]['Device']):
            device_append(self.Room_name, self.window).print_list()
            self.load_json()
            self.showTF = []
            for i in range(len(self.list[self.Room_name]['Device'])):
                self.showTF.append(False)
        else:
            if self.showTF[self.now] == True:
                self.showTF[self.now] = False
            else:
                self.showTF[self.now] = True
        self.print_list()

    def append_event(self):
        #device_append(list(self.list.keys())[self.now],self.window)
        #self.load_json()
        self.print_list()

    def quit_event(self):
        return True

    def print_all(self,device):
        if 'Sensor' in device['Kind']:
            self.window.addstr(device_format.sensor(device), color_pair(3))
        elif 'TV' in device['Kind']:
            self.window.addstr(device_format.Tv(device), color_pair(3))
        elif 'Fan' in device['Kind']:
            self.window.addstr(device_format.Fan(device), color_pair(3))
        elif 'Light' in device['Kind']:
            self.window.addstr(device_format.Light(device), color_pair(3))

    def print_list(self):
        all_cnt = 0
        t1 = threading.Thread(target=self.get_key, args=())
        t1.start()
        v_len = self.now_svl - self.maxy + 5
        max_v_len = self.maxy - 5
        v_cnt = 0
        self.window.erase()
        self.window.addstr('No\tName \t\t Kind\n', color_pair(4))
        for i, device in enumerate(self.list[self.Room_name]['Device']):
            all_cnt += 1
            if v_len > 0:
                v_len -= 1
                continue
            if v_cnt > max_v_len + 1:
                continue
            if all_cnt - 1 == self.now:
                # No devicename Roomname Condition
                self.window.addstr("{0} {1} {2} \n".format(str(i + 1).rjust(3).ljust(8), device['name'].ljust(15),
                                                           device['Kind'].ljust(15)), color_pair(2))
                if self.showTF[i] == True:
                    self.print_all(device)
            else:
                self.window.addstr("{0} {1} {2} \n".format(str(i + 1).ljust(6), device['name'].ljust(15),device['Kind'].ljust(15))
                                   ,color_pair(1))
                if self.showTF[i] == True:
                    self.print_all(device)
            v_cnt += 1

        if len(self.list[self.Room_name]['Device']) == self.now:
            self.window.addstr("\t +Append Device+\n", color_pair(2))
        else:
            self.window.addstr("\t +Append Device+\n", color_pair(1))

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
        self.move_curse(len(self.list[self.Room_name]['Device']))
        return 0

