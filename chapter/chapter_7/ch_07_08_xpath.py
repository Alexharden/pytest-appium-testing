from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本練習
# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.dangdan.buy2",
#     "appActivity": "dangdang.buy2.activity.ActivityMainTab",
#     "platformName": "Android",
#     "noReset": True
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# sleep(3)
# my_id = "com.dangdang.buy2:id/tab_personal_iv"
# #通過 path的 text 定位 “登入/註冊“
# login_xpath = "//*[@text='登入/註冊']"
# driver.find_element(AppiumBy.ID, my_id).click()
# sleep(2)
# driver.find_element(AppiumBy.XPATH, login_xpath).click()
# sleep(3)
# driver.quit()

# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：XPath 四大項獨立點擊 (不使用迴圈) ---

# --- 項目 1：Phone ---
xpath_phone = '//android.widget.TextView[@content-desc="Phone"]'
print(f"🚀 正在點擊: {xpath_phone}")
driver.find_element(AppiumBy.XPATH, xpath_phone).click()
sleep(2)
driver.press_keycode(3)  # 按下 Home 鍵
print("🏠 Phone 測試完成，已返回主畫面")
sleep(1)

# --- 項目 2：Messages ---
xpath_messages = '//android.widget.TextView[@content-desc="Messages"]'
print(f"🚀 正在點擊: {xpath_messages}")
driver.find_element(AppiumBy.XPATH, xpath_messages).click()
sleep(2)
driver.press_keycode(3)
print("🏠 Messages 測試完成，已返回主畫面")
sleep(1)

# --- 項目 3：Chrome ---
xpath_chrome = '//android.widget.TextView[@content-desc="Chrome"]'
print(f"🚀 正在點擊: {xpath_chrome}")
driver.find_element(AppiumBy.XPATH, xpath_chrome).click()
sleep(2)
driver.press_keycode(3)
print("🏠 Chrome 測試完成，已返回主畫面")
sleep(1)

# --- 項目 4：TMoble (Predicted App) ---
xpath_tmoble = '//android.widget.TextView[@content-desc="Predicted app: Play Store"]'
print(f"🚀 正在點擊: {xpath_tmoble}")
driver.find_element(AppiumBy.XPATH, xpath_tmoble).click()
sleep(2)
driver.press_keycode(3)
print("🏠 TMoble 測試完成，已返回主畫面")
sleep(1)

# --- 結束連線 ---
print("🧹 所有點擊流程結束")
driver.quit()
