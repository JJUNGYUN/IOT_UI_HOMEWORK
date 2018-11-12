from menu import menu

class sub_menu(menu):
    list = ["Inner Room"]
    def go_next(self):
        if self.now == 0:
            self.print_list()
        elif self.now == 1:
            self.print_list()
        elif self.now == 2:
            return False