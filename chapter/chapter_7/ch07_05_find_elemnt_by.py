from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy  # 導入 Appium 專用 By
from appium.webdriver.common.appiumby import By

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
# driver.find_element(By.ID,my_id).click()
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

# --- 核心練習：使用 By 物件進行點擊 ---

# 1. Accessibility ID (使用 AppiumBy)
# 截圖中的 Chrome content-desc
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()
print("✅ AppiumBy.ACCESSIBILITY_ID 點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. XPath (使用 By)
xpath_val = '//android.widget.TextView[@content-desc="Chrome"]'
driver.find_element(By.XPATH, xpath_val).click()
print("✅ By.XPATH 點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 3. Android UIAutomator (使用 AppiumBy)
uia_val = 'new UiSelector().text("Chrome")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uia_val).click()
print("✅ AppiumBy.ANDROID_UIAUTOMATOR 點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 4. Class Name (使用 By)
# 取得複數元素後點擊第 8 個 (Index 7)
elements = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
elements[7].click()
print("✅ By.CLASS_NAME 點擊成功")
sleep(2)
driver.terminate_app("com.android.chrome")

# 5. ID (使用 By)
# 雖然 Chrome 圖示沒 ID，但用法格式如下 (以你課本的 ID 為例)
# my_id = 'com.android.launcher3:id/icon'
# driver.find_element(By.ID, my_id).click()

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()
