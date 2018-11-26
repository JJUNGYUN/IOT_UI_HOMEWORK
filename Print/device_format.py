def sensor(device):
    return "\tstate :  {0} {1}\n".format(device['state'],device['measure'])

def Tv(device):
    return "\tChannel : {0} Sound : {1} ON/OFF : {2}\n".format(device['Chanel'],device['Sound'],device['ON/OFF'])

def Light(device):
    return "\tON/OFF : {0}\n".format(device['ON/OFF'])

def Fan(device):
    return "\tintensity : {0} {1}\n".format(device['intensity'],device['ON/OFF'])

'''
"TV":{"name":"","Kind":"Actuator/TV","Chanel":0,"Sound":0,"ON/OFF":["OFF","ON"]},
"Light":{"name":"","Kind":"Actuator/Light","ON/OFF":["OFF","ON"]},
"Fan":{"name":"","Kind":"Actuator/Fan","intensity":0,"ON/OFF":["OFF","ON"]}
'''