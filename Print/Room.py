import threading, time ,datetime
from Print.list import _list
from Append.room import room
from curses import *
from Print.append import device_append
from Print.Room_device import Room_device
class Room(_list):

    def enter_event(self):
        if self.now == len(self.list):
            self.window.addstr("Name : ")
            append = room(self.window)
            append.append_menu()
            self.load_json()
        elif self.showTF[self.now] == False:
            self.showTF[self.now] = True


        self.print_list()

    def append_event(self):
        device_append(list(self.list.keys())[self.now],self.window)
        self.load_json()
        self.print_list()

    def quit_event(self):
        return True

    def print_list(self):
        t1 = threading.Thread(target=self.get_key, args=())


        for i,j in enumerate(self.list):
            if self.showTF[i]:
                room_device = Room_device(self.window, j)
                room_device.print_list()
                self.showTF[i] = False
        self.window.erase()
        self.window.addstr('No\tName\t\tDevice Count\n', color_pair(4))

        for i, j in enumerate(self.list):
            try:
                if i == self.now:
                    self.window.addstr(
                        "{0} {1} {2} \n".format(str(i + 1).rjust(3).ljust(8), j.ljust(15), self.list[j]['dcnt']),
                        color_pair(2))

                else:
                    self.window.addstr("{0} {1} {2} \n".format(str(i + 1).ljust(6), j.ljust(15), self.list[j]['dcnt']),
                                       color_pair(1))
            except:
                continue
        if len(self.list) == self.now:
            self.window.addstr("\t +Append Room+\n", color_pair(2))
        else:
            self.window.addstr("\t +Append Room+\n", color_pair(1))

        t1.start()
        self.window.refresh()
        while (t1.isAlive()):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timewin = newwin(1, 20, 0, self.maxx - 21)
            timewin.addstr(str(now), A_BOLD + color_pair(3))
            explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
            explain.addstr(
                "↑,↓ : Move menu / Enter : Show Select Device / q , Q : Previous page / p, P : Append device",
                A_BOLD + color_pair(3))

            timewin.refresh()
            explain.refresh()

        #self.move_curse()
        self.move_curse(len(self.list))

        return 0