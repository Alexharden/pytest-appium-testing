import time

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

try:
    driver.activate_app("com.android.chrome")
    time.sleep(3)
    # 方式：get_screenshot_as_file
    target_path = "/Users/harden.cc.hsieh/Documents/practice/pytest-appium-testing/chapter/chapter_9/chrome_as_file.png"
    driver.get_screenshot_as_file(target_path)
    print(f"✅ 檔案已透過 as_file 儲存: {target_path}")
finally:
    driver.quit()
