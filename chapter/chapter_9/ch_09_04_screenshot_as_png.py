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
    # 方式：get_screenshot_as_png (取得二進制數據)
    png_data = driver.get_screenshot_as_png()
    print(f"✅ 已獲取二進制數據，長度: {len(png_data)}")

    # 手動寫入檔案範例
    with open("manual_binary_save.png", "wb") as f:
        f.write(png_data)
finally:
    driver.quit()
