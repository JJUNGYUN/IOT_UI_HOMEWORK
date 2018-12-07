import threading, time ,datetime
from Print.list import _list
from curses import *

class Search(_list):


    def __init__(self,window):
        self.load_json()
        self.window= window
        init_pair(4, COLOR_CYAN, COLOR_BLACK)
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()
        self.now_svl = 0
        self.search_device =[]

    def enter_event(self):
        return True

    def append_event(self):
        self.print_list()

    def quit_event(self):
        return True

    def read_ch(self):
        #echo()
        #running = True
        #temp = []
        self.window.move(0,15)
        #while (running):
        key = self.window.getch()
        #if key == 10:
            #running = False
            #break
        if key == 8 and len(self.search_device) != 0:
            nowy, nowx = self.window.getyx()
            if len(self.search_device) == 0:
                self.window.move(nowy, nowx + 1)
                #continue
            self.window.addstr(" ")
            self.window.move(nowy, nowx)
            self.search_device.pop()
            self.window.refresh()
            #continue
        else:
            self.search_device.append(chr(key))
        if len(self.search_device) > 20:
            nowy, nowx = self.window.getyx()
            self.window.move(nowy, nowx-1)
            self.window.addstr(" ")
            self.window.move(nowy, nowx-1)
            self.window.refresh()
            self.search_device.pop()


    def move_curse(self):
        if self.key == 10:
            self.enter_event()
        else:
            self.read_ch()
            self.print_list()


    def print_list(self):
        t1 = threading.Thread(target=self.get_key, args=())
        self.window.erase()
        self.window.addstr('Search Name : ', color_pair(4))
        self.window.addstr(''.join(self.search_device), color_pair(2))
        for room in self.list:
            for device in self.list[room]["Device"]:
                if ''.join(self.search_device) in device['name']:
                    self.window.addstr("\n"+str(device), color_pair(2))
        self.window.refresh()
        t1.start()
        while (t1.isAlive()):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timewin = newwin(1, 20, 0, self.maxx - 21)
            timewin.addstr(str(now), A_BOLD + color_pair(3))
            explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
            explain.addstr(
                "↑,↓ : Move menu / Enter : Show Select Device / q , Q : Previous page ",
                A_BOLD + color_pair(3))

            timewin.refresh()
            explain.refresh()

        #self.move_curse()
        self.move_curse()
        return 0