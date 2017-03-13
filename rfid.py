import threading
import time
import requests
import test

def handler(func):
    return func()

def hello():
    callback = test.rf_Read
    data = handler(callback)
    if data != 0:
        requrl = 'http://front2017.unilorn.com/api/rfid?rfid=%X' % data
        resdata = requests.get(requrl)
        t=threading.Timer(3,hello)
        print(resdata.text)
    else:
        t=threading.Timer(0.01,hello)
    print("%X" % data)
    t.start()

if __name__=='__main__':
    t=threading.Thread(target=hello)
    t.start()
