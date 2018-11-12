from device_append import *
from Append_Room import Append_room
from main_menu import main_menu
from Print_list import Print_list

class Room_list(Print_list):


    def enter_event(self):
        if self.now == len(self.list):
            append = Append_room()
            append.append_menu()
            endwin()
            return False
        elif self.showTF[self.now]:
            self.showTF[self.now] = False
        else:
            self.showTF[self.now] = True
        self.print_list()


    def append_event(self):
        append_menu = device_append(list(self.list.keys())[self.now])
        append_menu.print_list()
        endwin()

    def quit_event(self):
        main = main_menu().menu()
        main.print_list()
        endwin()

    def print_list(self):
        self.window.erase()
        self.window.addstr('No\tName\t\tDevice Count\n',color_pair(4))
        for i,j in enumerate(self.list):
            if i == self.now:
                self.window.addstr("{0} {1} {2} \n".format(str(i+1).rjust(3).ljust(8),j.ljust(15),self.list[j]['dcnt']),color_pair(2))
                if self.showTF[i]:
                    for device in self.list[j]['Device']:
                        self.window.addstr("\t     {0} {1} {2} \n".format(device['name'].ljust(15),device['Kind'].ljust(15),device['Condition']), color_pair(3)+A_BOLD)
            else:
                self.window.addstr("{0} {1} {2} \n".format(str(i + 1).ljust(6), j.ljust(15), self.list[j]['dcnt']),
                                   color_pair(1))
                if self.showTF[i]:
                    for device in self.list[j]['Device']:
                        self.window.addstr("\t   {0} {1} {2} \n".format(device['name'].ljust(15),device['Kind'].ljust(15),device['Condition']),color_pair(3))
        if len(self.list) == self.now:
            self.window.addstr("\t +Append Room+\n",color_pair(2))
        else:
            self.window.addstr("\t +Append Room+\n", color_pair(1))

        explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
        explain.addstr("↑,↓ : Move menu / Enter : Show Select Device / q , Q : Previous page / p, P : Append device", A_BOLD+color_pair(3))

        self.window.refresh()
        explain.refresh()
        self.move_curse(len(self.list))
        endwin()
        return 0;
