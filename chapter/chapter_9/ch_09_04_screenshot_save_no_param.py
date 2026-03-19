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
    # 方式：不傳遞參數 (注意：這在 Selenium/Appium 實務上較少見，通常會回傳 bool)
    result = driver.save_screenshot(
        "/Users/harden.cc.hsieh/Documents/practice/pytest-appium-testing/chapter/chapter_9/default_save.png"
    )
    print(f"截圖是否成功: {result}")
finally:
    driver.quit()
