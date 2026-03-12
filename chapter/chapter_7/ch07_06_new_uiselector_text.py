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
#     "noReset": True #不重置，保留app的狀態
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# my_id = 'com.dangdan.buy2:id/tab_personal_iv'
# #Android_UIAUTOMATOR text 值定位
# login_text = 'new UiSelector().text("登入/註冊")'
# driver.find_element(AppiumBy.ID,my_id).click()
# sleep(3)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,login_text).click()
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

# --- 核心練習：使用 UIAutomator Text 各種變體 ---

# 1. 完全比對文字 (最常用)
# 語法：new UiSelector().text("精確文字")
target_text = 'new UiSelector().text("Chrome")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, target_text).click()
print("✅ UIAutomator 精確文字點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. 包含特定文字 (模糊比對)
# 語法：new UiSelector().textContains("部分文字")
contains_text = 'new UiSelector().textContains("Chro")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, contains_text).click()
print("✅ UIAutomator 包含文字點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 3. 以特定文字開頭
# 語法：new UiSelector().textStartsWith("開頭文字")
start_text = 'new UiSelector().textStartsWith("Ch")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, start_text).click()
print("✅ UIAutomator 開頭文字點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 4. 使用正則表達式 (最彈性)
# 語法：new UiSelector().textMatches("正則表達式")
# 例如：找 Chrome 或 chrome (忽略大小寫的感覺)
regex_text = 'new UiSelector().textMatches("(?i)chrome")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, regex_text).click()
print("✅ UIAutomator 正則表達式點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()
