from Append.append_action import append

class Append_sensor(append):
    defalut = {"name":"","Kind":"Sensor","Condition":"OFF"}

    def append_menu(self,Room_name):
        self.window.addstr("Name : ")
        self.name = self.read_ch()
        self.defalut["name"] = self.name
        self.list[Room_name]['Device'].append(self.defalut)
        self.list[Room_name]['dcnt'] = len(self.list[Room_name]['Device'])
        self.save_json()
