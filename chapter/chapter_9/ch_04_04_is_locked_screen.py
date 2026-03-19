import time
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
    "appium:appPackage": "com.android.chrome",
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(10)

driver.lock()
print("當前螢幕狀態{}".format(driver.is_locked()))  # True
sleep(3)
driver.unlock()
print("當前螢幕狀態{}".format(driver.is_locked()))  # False

driver.quit()
