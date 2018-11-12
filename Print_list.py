import curses
from curses import *
import pandas as pd
from abc import *

class Print_list(object,metaclass=ABCMeta):

    list = {}

    def __init__(self,window):
        self.load_json()
        self.window= window
        init_pair(4, COLOR_CYAN, COLOR_BLACK)
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()

    def load_json(self):
        json = pd.read_json('project.json')
        self.list = json.to_dict()
        self.showTF = []
        for i in range(len(self.list)):
            self.showTF.append(False)


    @abstractmethod
    def enter_event(self):
        pass

    @abstractmethod
    def append_event(self):
        pass

    @abstractmethod
    def quit_event(self):
        pass

    @abstractmethod
    def print_list(self):
        pass

    def get_key(self):
        self.key = self.window.getch()

    def move_curse(self,len):
        if self.key == KEY_DOWN:
            if self.now<len:
                self.now += 1
            else:
                self.now = 0
            self.print_list()
        elif self.key ==KEY_UP:
            if self.now > 0:
                self.now -= 1
            else:
                self.now = len
            self.print_list()
        elif self.key == 10:
            self.enter_event()
        elif self.key == ord('q') or self.key == ord('Q'):
            self.quit_event()
        elif self.key == ord('p') or self.key == ord('P'):
            self.append_event()
        elif self.key == 27:
            return False
        else:
            self.print_list()



