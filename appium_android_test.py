# Android environment
import unittest
import HtmlTestRunner
from time import sleep
from tqdm import tqdm
from appium import webdriver

class AppTest(unittest.TestCase) :

    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '12.0'
        desired_caps['deviceName'] = 'emulator64_arm64'

        desired_caps['app'] = '/Users/' + os.getenv('USER') + '/ysec/YSEC_DEV/app/build/intermediates/apk/debug/app-debug.apk'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.app = 'com.cultsotry.yanolja.nativeapp.dev'

    def test_install(self):
        # check app installed
        is_install = self.driver.is_app_installed(self.app)

        if not is_install :
            print("download app")
        else:
            print("installed ok")

        #self.driver.install_app('/Users/' + os.getenv('USER') + '/QA/debug-app.apk')

    def test_app_remove(self):
        # check app installed
        is_install = self.driver.is_app_installed(self.app)

        if is_install :
            pass
            #self.driver.remove_app(self.app)

    def testRun(self):

        # lauching test app
        for x in tqdm(range(0, 2)):
            self.driver.launch_app()
            #self.driver.toggle_wifi()
            self.driver.close_app()
            
        sleep(5)

        self.driver.launch_app()

        # check app state
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

        sleep(1.5)


        self.driver.background_app(10)
        self.driver.activate_app(self.app)

        #assert self.driver.current_activity == "MainActivity"


        #self.driver.switch_to.context("NATIVE_APP")

        self.driver.terminate_app(self.app)

    def test_SwitchActivity(self):
        # check : switching activity
        #self.driver.start_activity(self.app, "NewMainActivity")

        #assert self.driver.current_activity == "NewMainActivity"

        sleep(1)

        # check : switching activity
        #self.driver.start_activity(self.app, "MainActivity")



    def tearDown(self) -> None:
        # check : reinstall
        self.driver.quit()
        print("Done.")

if __name__ == '__main__' :
    testcase = unittest.TestLoader().loadTestsFromTestCase(AppTest)
    #unittest.TextTestRunner(verbosity=2).run(testcase)
    testsuite = unittest.TestSuite([testcase])
    HtmlTestRunner.HTMLTestRunner(output="Reports",
                                report_name = "Report",
                                report_title = "Test Results",
                                combine_reports = True).run(testsuite)