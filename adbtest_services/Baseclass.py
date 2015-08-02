# -*- coding: utf-8 -*-
'''
Created on 2015/08/01

@author: bob
'''
import unittest
import os

from adbtest_services import adbtool

class Baseclass(unittest.TestCase):
    def setUp(self):
        print("Baseclass.setUp() called.")
        self.adbtool = adbtool()
        self.resultPath = os.getenv("RESULT_PATH")
        try:
            self.deviceId, self.deviceIndex = os.getenv("DEVICE_ID").split(":")
        except:
            self.deviceId = ""
            self.deviceIndex = "0"
    def tearDown(self):
        print("Baseclass.tearDown() called.")

if __name__ == "__main__": 
    classList    =    [] 
    classList.append(Baseclass()) 
    for value in classList: 
        print("===== class =====") 
        print("resultPath = " + value.resultPath)
        