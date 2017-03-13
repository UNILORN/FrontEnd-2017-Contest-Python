import threading
import time
import test
def handler(func):
    return func()

def hello():
    callback = test.rf_Read
    print("aa " + str(threading.activeCount()))
    print("[%s] helohelo!!" % threading.currentThread().getName())
    t=threading.Timer(0.01,hello)
    handler(callback)
    t.start()

if __name__=='__main__':
    t=threading.Thread(target=hello)
    t.start()
