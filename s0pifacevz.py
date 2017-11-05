#!/usr/bin/env python3

import pifacedigitalio as pfio
import time
import os
import sys
import pycurl
import array

VZ_SERVER = ""
VZ_PATH = ""
VZ_PORT = 80

VZUUID = ['','','','','','','','']

def getVZUUID(pin):
    global VZUUID
    return VZUUID[pin]

def pinHit(event):
    global VZ_SERVER
    global VZ_PATH
    global VZ_PORT

    vz_url = "http://%s:%s/%s/data/%s.json" % (VZ_SERVER,VZ_PORT,VZ_PATH, getVZUUID(event.pin_num))

    c = pycurl.Curl()
    c.setopt(pycurl.URL, vz_url)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
    c.perform()
    c.close

pfio.init()

pifacedigital = pfio.PiFaceDigital()
listener = pfio.InputEventListener(chip=pifacedigital)

signalDirection = pfio.IODIR_RISING_EDGE

for pin in range (0,7):
    if VZUUID[pin] != "":
        listener.register(pin, signalDirection, pinHit)

listener.activate()
