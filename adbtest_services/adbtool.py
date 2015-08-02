# -*- coding: utf-8 -*-
'''
Created on 2015/08/01

@author: bob
'''

import os
import time

class adbtool():
    def __init__(self):
        print("adbtool.__init__ called.")

    def adbdevices(self):
        os.system("adb devices")
        time.sleep(1)

if __name__ == "__main__": 
    print("main of adbtool")        