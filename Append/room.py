from Append.append_action import append

class room(append):

    defalut = {'Device': [], 'dcnt': '0'}

    def append_menu(self):
        self.name = self.read_ch()
        self.list[self.name] = self.defalut
        self.save_json()



