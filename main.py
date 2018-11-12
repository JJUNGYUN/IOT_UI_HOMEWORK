import main_menu
import curses
from curses import *

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
    main_menu.main_menu(window=window)

if __name__=='__main__':
    x = main()