from Append.append_action import append

class Append_actuator(append):

    def append_menu(self,Room_name,type):
        self.window.addstr("Name : ")

        self.name = self.read_ch()
        self.default['Actuator'][type]["name"] = self.name
        self.default['Actuator'][type]["ON/OFF"] = ["OFF"]
        self.list[Room_name]['Device'].append(self.default['Actuator'][type])
        self.list[Room_name]['dcnt'] = len(self.list[Room_name]['Device'])
        self.save_json()
