# -*- coding: utf-8 -*-
from __future__ import print_function

import threading
import requests
from ctypes import *

FELICA_POLLING_ANY = 0xffff


class RFID_Read:
    def __init__(self):
        self.libpafe = cdll.LoadLibrary("/usr/local/lib/libpafe.so")
        self.pasori = self.libpafe.pasori_open()
        self.libpafe.pasori_init(self.pasori)
        self.libpafe.pasori_set_timeout(self.pasori,150)

    def Read(self):
        felica = self.libpafe.felica_polling(self.pasori, FELICA_POLLING_ANY, 0, 0)
        idm = c_uint64()
        self.libpafe.felica_get_idm.restype = c_void_p
        self.libpafe.felica_get_idm(felica, byref(idm))
        self.libpafe.free(felica)
        return idm.value

    def end(self):
        self.libpafe.pasori_close(self.pasori)
