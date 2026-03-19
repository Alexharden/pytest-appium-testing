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
    # 方式：get_screenshot_as_base64
    base64_str = driver.get_screenshot_as_base64()
    print(f"✅ 已獲取 Base64 字串 (前50碼): {base64_str[:50]}...")

    # 提示：這串字串可以直接用於 HTML 報告渲染
finally:
    driver.quit()
