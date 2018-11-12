from Print_list import Print_list
from Print_list import *
import main_menu

class Device_list(Print_list):

    def enter_event(self):
        self.print_list()

    def append_event(self):
        self.print_list()

    def quit_event(self):
        main = main_menu.main_menu(window=self.window)
        main.print_list()

    def print_list(self):
        all_cnt = 0
        self.window.erase()
        self.window.addstr('No\t   Name \t Kind   \t Condition \t Room\n', color_pair(4))
        for i,j in enumerate(self.list):
            for device in self.list[j]['Device']:
                if all_cnt == self.now:
                    #No devicename Roomname Condition
                    self.window.addstr("{0} {1} {4} {2} {3} \n".format(str(i+1).rjust(3).ljust(8),device['name'].ljust(15),
                                                                   device['Condition'].ljust(15),j,device['Kind'].ljust(15)),color_pair(2))
                else:
                    self.window.addstr(
                        "{0} {1} {4} {2} {3} \n".format(str(i+1).ljust(6),device['name'].ljust(15),
                                                                   device['Condition'].ljust(15),j,device['Kind'].ljust(15)),
                    color_pair(1))
                all_cnt +=1

        explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
        explain.addstr("↑,↓ : Move menu / q , Q : Previous page",
                       A_BOLD + color_pair(3))

        self.window.refresh()
        explain.refresh()
        self.move_curse(all_cnt-1)
        return 0
