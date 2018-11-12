import threading, time ,datetime

def pd():
    x = input()
    return x

t1 = threading.Thread(target=pd,args=())
x= t1.start()
while(t1.isAlive()):
    print(t1.isAlive())
    time.sleep(1)

print(x)