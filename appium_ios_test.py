'''
iOS Appium Native Script
'''
import unittest
import HtmlTestRunner
import os
from appium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
class AppTest(unittest.TestCase):
 
    def setUp(self) -> None:
        # Set up appium
        app = os.path.join(os.path.dirname(__file__), '/Users/jaegeun.yoon/Library/Developer/Xcode/DerivedData/SecuritySDK-aejgqwaviqpsstcobueelwsvtldv/Build/Products/Debug-iphonesimulator', 'SecuritySDK.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'ios',
                'platformVersion': '15.5', # SDK Version
                'deviceName': 'simulator',
                'automationName': 'xcuitest',
                'newCommandTimeout': 7200,
                'bundleId': 'yanolja.SecuritySDK',
                'udid': '2996AB36-A34D-4BEF-828A-1AEA0484FB8E', # simulator
            })
        self.app = 'yanolja.SecuritySDK'

    def testRun(self):
        driver = self.driver.launch_app()
        status = self.driver.query_app_state(self.app)

        if status == 0 :
            print("not installed")
        elif status == 1 :
            print("not running")
        elif status == 2 :
            print("running in background or suspended")
        elif status == 3 :
            print("running in background")
        elif status == 4 :
            print("running in foreground")
        else:
            print("status error")

        sleep(7)


        self.driver.terminate_app(self.app)

    def tearDown(self) -> None:
        self.driver.quit()
 
if __name__ == '__main__':
    testcase = unittest.TestLoader().loadTestsFromTestCase(AppTest)
    testsuite = unittest.TestSuite([testcase])
    HtmlTestRunner.HTMLTestRunner(output="Reports",
                                report_name = "Report",
                                report_title = "Test Results",
                                combine_reports = True).run(testsuite)