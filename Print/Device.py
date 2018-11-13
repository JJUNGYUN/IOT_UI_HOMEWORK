import threading, time ,datetime
from Print.list import _list
from curses import *
class Device(_list):

    def enter_event(self):
        self.print_list()

    def append_event(self):
        self.print_list()

    def quit_event(self):
        return True

    def print_list(self):
        all_cnt = 0
        t1 = threading.Thread(target=self.get_key, args=())
        t1.start()
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
        self.window.refresh()
        while (t1.isAlive()):
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timewin = newwin(1, 20, 0, self.maxx - 21)
            timewin.addstr(str(now), A_BOLD + color_pair(3))
            explain = newwin(1, self.maxx - 1, self.maxy - 1, 0)
            explain.addstr(
                "↑,↓ : Move menu / Enter : Show Select Device / q , Q : Previous page ",
                A_BOLD + color_pair(3))

            timewin.refresh()
            explain.refresh()

        #self.move_curse()
        self.move_curse(all_cnt-1)
        return 0
