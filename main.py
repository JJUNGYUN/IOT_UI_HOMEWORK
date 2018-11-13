import curses
from curses import *
from Print.main import main_menu

def main():
    window = curses.initscr()
    noecho()
    curs_set(0)
    #cbreak()
    window.keypad(True)
    start_color()
    init_pair(1, COLOR_WHITE, COLOR_BLACK)
    init_pair(2, COLOR_YELLOW, COLOR_BLACK)
    init_pair(3, COLOR_RED, COLOR_BLACK)
    main_menu(window)

if __name__=='__main__':
    x = main()