# -*- coding: utf-8 -*-

from __future__ import print_function
from ctypes import *

# libpafe.hの77行目で定義
FELICA_POLLING_ANY = 0xffff

def rf_Read():

    libpafe = cdll.LoadLibrary("/usr/local/lib/libpafe.so")

    libpafe.pasori_open.restype = c_void_p
    pasori = libpafe.pasori_open()
    
    libpafe.pasori_init(pasori)

    libpafe.felica_polling.restype = c_void_p
    felica = libpafe.felica_polling(pasori, FELICA_POLLING_ANY, 0, 0)

    idm = c_uint64()
    libpafe.felica_get_idm.restype = c_void_p
    libpafe.felica_get_idm(felica, byref(idm))

    # IDmは16進表記
    print("%X" % idm.value)

    # READMEより、felica_polling()使用後はfree()を使う
    # なお、freeは自動的にライブラリに入っているもよう
    libpafe.free(felica)

    libpafe.pasori_close(pasori)
