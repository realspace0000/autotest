# -*- coding: utf-8 -*-
'''
Created on 2015/08/01

@author: bob
'''
import sys,time,os
import xmlrunner
import unittest
#import adbtest_services
import adbtest_services
import random

class AdbTest1(unittest.TestCase):
    def setUp(self):
        print("AdbTest1.setUp()")        
#        super(AdbTest1, self).setUp()
#        self.adbtool = adbtest_services.adbtool()
        
    def tearDown(self):
        print("AdbTest1.tearDown()")
        
    def testAdbTest1(self):
        print("======================================================================")
        print("======================================================================")
        print("testAdbTest1 started.")
        print("======================================================================")
        print("======================================================================")
        time.sleep(1)

        print("Server address=[ http://www.google.com ]")
        
        result = True
        self.assertTrue(result,"result has to be True but was NOT True.")        
        print("======================================================================")
        print("======================================================================")
        print("testAdbTest1 finished.")
        print("======================================================================")
        print("======================================================================")

        print("testAdbTest1 ### Result: Passed. ###")
        print("======================================================================")

    def testAdbTest2(self):
        print("testAdbTest2 started.")
        if random.choice("12") == "1":
            result = False
        else:
            result = True
        self.assertTrue(result,"result has to be True but was NOT True.")        
        print("testAdbTest2 finished.")
        
    def testAdbTest3(self):
        print("testAdbTest3 started.")
        result = True
        self.assertTrue(result,"result has to be True but was NOT True.")        
        print("testAdbTest3 finished.")
        
        
        
if __name__ == "__main__":
    sys.argv = ['','AdbTest1.testAdbTest1']
    runner = xmlrunner.XMLTestRunner(output=os.getenv("RESULT_PATH"), stream=sys.stdout)
    suite = unittest.TestLoader().loadTestsFromTestCase(AdbTest1)
    runner.run(suite)
    