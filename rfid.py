import threading
import time
import test

def handler(func):
    return func()

def hello():
    callback = test.rf_Read
    print("aa " + str(threading.activeCount()))
    print("[%s] helohelo!!" % threading.currentThread().getName())
    if handler(callback) != 0:
        t=threading.Timer(3,hello)
    else
        t=threading.Timer(0.01,hello)
    t.start()

if __name__=='__main__':
    t=threading.Thread(target=hello)
    t.start()
