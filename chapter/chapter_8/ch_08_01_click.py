from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本練習
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:21503",
#     "appPackage": "com.dangdang.buy2.calculator",
#     "appActivity": "com.dangdang.buy2.calculator.MainActivity",
#     "noReset": True,
# }
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# sleep(3)
# my_id = 'com.dangdang.buy2.calculator:id/tab_personal_iv'
# ele = driver.find_element(AppiumBy.ID, my_id)
# ele.click()
# sleep(3)
# driver.quit()


desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
    # "appPackage": "com.viewsonic.testapk",
    # "appActivity": "com.viewsonic.testapk.MainActivity",
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
sleep(3)

# 方法 1：使用 Accessibility ID (最推薦，執行速度最快且最準)
# 對應截圖中的 accessibility id: Phone
ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Phone")
ele.click()
print("點到了")
sleep(1)
driver.terminate_app("com.google.android.dialer")
print("關閉了")
sleep(1)

# --- 或者 ---

# 方法 2：使用 XPath (如果你習慣用路徑)
# 對應截圖中的 xpath: //android.widget.TextView[@content-desc="Phone"]
ele = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]')
ele.click()
print("點到了")
sleep(1)
driver.terminate_app("com.google.android.dialer")
print("關閉了")
sleep(1)

# --- 或者 ---

# 方法 3：使用 Android UIAutomator (截圖中的那個 new UiSelector()...)
# 當其他方法都失效時的終極大絕
cmd = 'new UiSelector().text("Phone")'
ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, cmd)
ele.click()
print("點到了")
sleep(1)
driver.terminate_app("com.google.android.dialer")
print("關閉了")
sleep(1)
