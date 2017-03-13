import threading
import time
import test

def handler(func):
    return func()

def hello():
    callback = test.rf_Read
    print("aa " + str(threading.activeCount()))
    print("[%s] helohelo!!" % threading.currentThread().getName())
    data = handler(callback)
    if data != 0:
        t=threading.Timer(3,hello)
    else:
        t=threading.Timer(0.01,hello)
    print("%X" % data)
    t.start()

if __name__=='__main__':
    t=threading.Thread(target=hello)
    t.start()
