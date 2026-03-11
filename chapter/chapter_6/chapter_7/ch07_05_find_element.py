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

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# my_id = 'com.dangdan.buy2:id/tab_personal_iv'
# driver.find_element(by='id', value=my_id).click()
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

# --- 核心練習：依照 (by=..., value=...) 格式執行點擊 ---

# 1. Accessibility ID 方式
driver.find_element(by='accessibility id', value='Chrome').click()
print("✅ accessibility id 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. XPath 方式 (使用屬性組合)
xpath_value = '//android.widget.TextView[@content-desc="Chrome"]'
driver.find_element(by='xpath', value=xpath_value).click()
print("✅ xpath 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 3. XPath 方式 (純文字比對)
driver.find_element(by='xpath', value='//*[@text="Chrome"]').click()
print("✅ xpath text 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 4. Android UIAutomator 方式
uia_value = 'new UiSelector().text("Chrome")'
driver.find_element(by='-android uiautomator', value=uia_value).click()
print("✅ uiautomator 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 5. Class Name 方式 (取得列表後索引)
# 注意：find_elements 複數形式同樣適用 by/value
elements = driver.find_elements(by='class name', value='android.widget.TextView')
elements[7].click()
print("✅ class name 點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# 6. 座標方式 (座標為特殊 API，不使用 find_element)
driver.tap(positions=[(666, 1970)])
print("✅ 座標點到了")
sleep(2)
driver.terminate_app("com.android.chrome")

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()