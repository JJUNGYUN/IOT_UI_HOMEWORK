from curses import *
from abc import *
import pandas as pd
class append(object,metaclass=ABCMeta):
    defalut = {}

    def __init__(self,window):
        self.window = window
        echo()
        self.read_json()

    def read_json(self):
        json = pd.read_json('project.json')
        self.list = json.to_dict()

    @classmethod
    @abstractmethod
    def append_menu(cls):
        pass

    def save_json(self):
        pd.DataFrame(self.list).to_json('project.json')

    def read_ch(self):
        running = True
        temp = []
        while (running):
            key = self.window.getch()


            if key == 10:
                running = False
                break
            if key == 8:
                nowy, nowx = self.window.getyx()
                if len(temp) == 0:
                    self.window.move(nowy, nowx + 1)
                    continue
                self.window.addstr(" ")
                self.window.move(nowy, nowx)
                temp.pop()
                self.window.refresh()
                continue
            temp.append(chr(key))
            if len(temp) > 20:
                nowy, nowx = self.window.getyx()
                self.window.move(nowy, nowx-1)
                self.window.addstr(" ")
                self.window.move(nowy, nowx-1)
                self.window.refresh()
                temp.pop()

        noecho()
        return ''.join(temp)

