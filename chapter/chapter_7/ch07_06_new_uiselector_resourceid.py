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
# login_text = 'new UiSelector().resourceId("com.dangdang.byu2:id/tv_agile_user_name")'
# driver.find_element(AppiumBy.ID,my_id).click()
# sleep(3)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,login_text).click()
# sleep(3)
# driver.quit()

desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


# --- 核心練習：resourceId 的各種組合技 ---

# 1. 精確組合：ID + Text (最推薦)
# 語法：new UiSelector().resourceId("ID").text("文字")
photos_selector = 'new UiSelector().resourceId("com.google.android.apps.nexuslauncher:id/g_icon")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, photos_selector).click()
print("✅ Photos (ID+Text) 點擊成功")
sleep(2)
driver.press_keycode(3)

# --- 結束連線 ---
print("🧹 測試結束")
driver.quit()
