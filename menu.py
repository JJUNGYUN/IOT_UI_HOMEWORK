import curses
from curses import *
from abc import *
class menu(object,metaclass=ABCMeta):
    list = []
    def __init__(self):
        self.curses_init()

    @classmethod
    def menu(cls):
        return cls()

    @abstractmethod
    def go_next(self):
        pass

    def curses_init(self):
        self.window = curses.initscr()
        noecho()
        self.window.keypad(True)
        start_color()
        init_pair(1,COLOR_WHITE,COLOR_BLACK)
        init_pair(2,COLOR_YELLOW,COLOR_BLACK)
        init_pair(3,COLOR_RED,COLOR_BLACK)
        self.now = 0
        self.maxy, self.maxx = self.window.getmaxyx()

    def move_curse(self):
        key = self.window.getch()
        if key == KEY_DOWN:
            if self.now<len(self.list)-1:
                self.now += 1
            self.print_list()
        elif key ==KEY_UP:
            if self.now > 0:
                self.now -= 1
            self.print_list()
        elif key == 10:
            self.go_next()
        else:
            self.print_list()

    def print_list(self):
        self.window.erase()
        for i,j in enumerate(self.list):
            if i == self.now:
                self.window.addstr(str(i+1)+". "+j+"\n",color_pair(2))
            else:
                self.window.addstr(str(i+1)+". "+j+"\n",color_pair(1))

        explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
        explain.addstr("↑,↓ : Move menu / Enter : Select", A_BOLD+color_pair(3))

        #new_panel = panel.new_panel(explain)
        #panel.update_panels()
        #doupdate()
        self.window.refresh()
        explain.refresh()
        self.move_curse()
        endwin()

        return 0

'''
if __name__=='__main__':
    menu = menu()
    wrapper(menu.print_list())
'''