import curses
from curses import *
from abc import *
import threading, time ,datetime
class menu(object,metaclass=ABCMeta):
    list = []

    def __init__(self,window):
        self.window = window
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()
        self.print_list()


    @classmethod
    def menu(cls):
        return cls()

    @abstractmethod
    def go_next(self):
        pass

    def get_key(self):
        self.print = 2
        self.key = self.window.getch()
    def move_curse(self):
        if self.key == KEY_DOWN:
            if self.now<len(self.list)-1:
                self.now += 1
            self.print_list()
        elif self.key == KEY_UP:
            if self.now > 0:
                self.now -= 1
            self.print_list()
        elif self.key == 10:
            self.go_next()
        else:
            self.print_list()

    def print_list(self):
        t1 = threading.Thread(target=self.get_key, args=())
        t1.start()
        self.window.erase()
        for i, j in enumerate(self.list):
            if i == self.now:
                self.window.addstr(str(i + 1) + ". " + j + "\n", color_pair(2))
            else:
                self.window.addstr(str(i + 1) + ". " + j + "\n", color_pair(1))

        self.window.refresh()


        while(t1.isAlive()):

            explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
            explain.addstr("↑,↓ : Move menu / Enter : Select", A_BOLD + color_pair(3))
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timewin = newwin(1, 20, 0, self.maxx - 21)
            timewin.addstr(str(now), A_BOLD + color_pair(3))
            timewin.refresh()
            explain.refresh()
            #time.sleep(0.3)
            #self.move_curse()
        self.move_curse()
        return 0

