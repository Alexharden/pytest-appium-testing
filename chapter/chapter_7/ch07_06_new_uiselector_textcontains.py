from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本練習
desired_caps = {
    "deviceName": "127.0.0.1:21503",
    "appPackage": "com.dangdan.buy2",
    "appActivity": "dangdang.buy2.activity.ActivityMainTab",
    "platformName": "Android",
    "noReset": True,  # 不重置，保留app的狀態
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 輸出當前包和activity
my_id = "com.dangdan.buy2:id/tab_personal_iv"
# Android_UIAUTOMATOR text 值定位
login_text = 'new UiSelector().textContains("登入")'
driver.find_element(AppiumBy.ID, my_id).click()
sleep(3)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, login_text).click()
sleep(3)
driver.quit()

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

# --- 核心練習：使用 textContains 模糊比對 ---

# 1. 使用 Chrome 的部分文字 "Chro"
# 只要畫面上的文字包含 "Chro" 就會被點擊
target_text = 'new UiSelector().textContains("Chro")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, target_text).click()
print("✅ textContains('Chro') 點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. 使用 Play Store 的部分文字 "Play"
play_text = 'new UiSelector().textContains("Play")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, play_text).click()
print("✅ textContains('Play') 點擊成功")
sleep(2)
driver.terminate_app("com.android.vending")  # Play Store 的包名

# 3. 使用 YouTube 的部分文字 "You"
yt_text = 'new UiSelector().textContains("You")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, yt_text).click()
print("✅ textContains('You') 點擊成功")
sleep(2)
driver.terminate_app("com.google.android.youtube")
# 4. 使用 Settings 的部分文字 "Sett"
phone_text = 'new UiSelector().textContains("Phon")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, phone_text).click()
print("✅ textContains('Phone') 點擊成功")
sleep(2)
driver.terminate_app("com.google.android.dialer")

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()
