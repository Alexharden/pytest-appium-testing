from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy   # 導入 Appium 專用 By
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

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# my_id = 'com.dangdan.buy2:id/tab_personal_iv'
# driver.find_element(AppiumBy.ID,my_id).click()
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
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：全數使用 AppiumBy 格式 ---

# 1. 使用 ID 定位 (對應課本 ID 寫法)
# 注意：Chrome 圖示在 Launcher 中可能沒有固定 ID，此處以格式示範為主
# 假設 ID 是 com.google.android.apps.nexuslauncher:id/icon
# driver.find_element(AppiumBy.ID, "com.google.android.apps.nexuslauncher:id/icon").click()

# 2. 使用 Accessibility ID 定位 (Inspector 截圖中的 Chrome)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()
print("✅ AppiumBy.ACCESSIBILITY_ID 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 3. 使用 XPath 定位
driver.find_element(AppiumBy.XPATH, '//*[@text="Chrome"]').click()
print("✅ AppiumBy.XPATH 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 4. 使用 Android UIAutomator 定位
uia_val = 'new UiSelector().text("Chrome")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uia_val).click()
print("✅ AppiumBy.ANDROID_UIAUTOMATOR 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 5. 使用 Class Name 定位 (獲取列表)
elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
elements[7].click()
print("✅ AppiumBy.CLASS_NAME 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()