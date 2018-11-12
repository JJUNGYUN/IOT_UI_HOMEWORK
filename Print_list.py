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

    def move_curse(self,len):
        key = self.window.getch()
        if key == KEY_DOWN:
            if self.now<len:
                self.now += 1
            else:
                self.now = 0
            self.print_list()
        elif key ==KEY_UP:
            if self.now > 0:
                self.now -= 1
            else:
                self.now = len
            self.print_list()
        elif key == 10:
            self.enter_event()
        elif key == ord('q') or key == ord('Q'):
            self.quit_event()
        elif key == ord('p') or key == ord('P'):
            self.append_event()
        elif key == 27:
            return False
        else:
            self.print_list()



