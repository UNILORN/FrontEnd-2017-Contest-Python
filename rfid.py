# -*- coding: utf-8 -*-
from __future__ import print_function

import threading
import requests
import RFID_Read

FELICA_POLLING_ANY = 0xffff

def handler(func):
    return func()

def run():
    callback = rfid.Read
    data = handler(callback)
    if data != 0:
        #requrl = 'http://front2017.unilorn.com/api/rfid?rfid=%X' % data
        #resdata = requests.get(requrl)
        #print(resdata.text)
        t = threading.Timer(0.5, run)
    else:
        t = threading.Timer(0, run)
    print(data)
    t.start()

if __name__ == '__main__':
    rfid = RFID_Read.RFID_Read()
    t = threading.Thread(target=run)
    t.start()
