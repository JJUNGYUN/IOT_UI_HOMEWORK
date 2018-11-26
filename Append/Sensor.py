from Append.append_action import append

class Append_sensor(append):

    def append_menu(self,Room_name,type):
        self.window.addstr("Name : ")
        self.name = self.read_ch()
        self.default['Sensor'][type]["name"] = self.name
        self.list[Room_name]['Device'].append(self.default['Sensor'][type])
        self.list[Room_name]['dcnt'] = len(self.list[Room_name]['Device'])
        self.save_json()
