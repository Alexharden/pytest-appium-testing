from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

# # 課本練習
# desired_caps = {
#     "deviceName": "127.0.0.1:21503",
#     "platformName": "Android",
#     "noReset": True
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# window_size = driver.get_window_size()
# print(window_size)
# driver.quit()


# 1. 基礎連線設定
# 我們指定連線到你的 ViewSonic Test APK
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

windows = driver.get_window_size()
print(windows["width"])
print(windows["height"])
# 4. 結束連線
print("🧹 測試結束，關閉 Session")
driver.quit()
