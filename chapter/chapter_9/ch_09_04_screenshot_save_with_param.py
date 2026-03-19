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
    # 方式：傳遞參數指定路徑
    filename = "/Users/harden.cc.hsieh/Documents/practice/pytest-appium-testing/chapter/chapter_9/chrome_home_save.png"
    driver.save_screenshot(filename)
    print(f"✅ 截圖已儲存至: {filename}")
finally:
    driver.quit()
