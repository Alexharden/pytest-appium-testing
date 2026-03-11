from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# #課本練習
# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.dangdan.buy2",
#     "appActivity": "dangdang.buy2.activity.ActivityMainTab",
#     "platformName": "Android",
#     "noReset": True
# }

# drvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# my_id = 'com.dangdan.buy2:id/tab_personal_iv'
# driver.find_element(AppiumBy.ID, my_id).click()
# sleep(3)
# driver.quit()


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True
}

options = UiAutomator2Options().load_capabilities(desired_caps)

# 2. 建立連線
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：獲取當前 App 資訊 ---
driver.find_element("accessibility id", "Chrome").click()
print("id點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 使用 Inspector 提供的建議路徑
driver.find_element("xpath", '//android.widget.TextView[@content-desc="Chrome"]').click()
print("xpath Inspector 點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 或者是根據文字來定位
driver.find_element("xpath", '//*[@text="Chrome"]').click()
print("xpath text 點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 假設有 resource id 是 com.android.launcher3:id/icon
# driver.find_element("id", "com.google.android.apps.nexuslauncher:id/icon").click()
# print("resource id 點到了")
# sleep(3)
# driver.terminate_app("com.android.chrome")
# sleep(1)

#Android UIAutomator
driver.find_element("-android uiautomator", 'new UiSelector().text("Chrome")').click()
print("uiautomator 點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# Class name 點擊畫面中第 3 個 TextView (索引從 0 開始，假設 Chrome 是第 3 個)
driver.find_elements("class name", "android.widget.TextView")[7].click()
print("class name 點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

#座標
driver.tap([(666, 1970)])
print("座標點到了")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)


# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()