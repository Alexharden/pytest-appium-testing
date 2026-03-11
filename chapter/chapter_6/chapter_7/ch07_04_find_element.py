from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

#課本練習
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
# driver.find_element_by_id(my_id).click()
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

# --- 核心練習：各種定位點擊方式 ---

# 1. Accessibility ID (課本對應：find_element_by_accessibility_id)
# 現代寫法如下，邏輯與課本完全一致
driver.find_element("accessibility id", "Chrome").click()
print("✅ Accessibility ID 點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 2. XPath (課本對應：find_element_by_xpath)
# 使用 Inspector 提供的建議路徑
driver.find_element("xpath", '//android.widget.TextView[@content-desc="Chrome"]').click()
print("✅ XPath (Inspector) 點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 3. XPath Text (課本對應：find_element_by_xpath)
# 根據文字來定位
driver.find_element("xpath", '//*[@text="Chrome"]').click()
print("✅ XPath (Text) 點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 4. Android UIAutomator (課本對應：find_element_by_android_uiautomator)
driver.find_element("-android uiautomator", 'new UiSelector().text("Chrome")').click()
print("✅ UIAutomator 點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 5. Class Name (課本對應：find_elements_by_class_name)
# 注意：這是 find_elements (複數)，會回傳清單
driver.find_elements("class name", "android.widget.TextView")[7].click()
print("✅ Class Name (Index 7) 點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# 6. 座標點擊 (唯一解)
# 座標沒有 find_element 寫法，這是獨立的 API
driver.tap([(666, 1970)])
print("✅ 座標點擊成功")
sleep(3)
driver.terminate_app("com.android.chrome")
sleep(1)

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()