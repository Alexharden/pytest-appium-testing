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
# login_xpath = "//android.widget.TextView[contains(@text, '登入/註冊')]"
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

# --- 核心練習：使用 XPath contains 進行模糊定位 ---

# --- 項目 1：Phone ---
# 語法：//標籤[contains(@屬性, '關鍵字')]
xpath_phone = '//android.widget.TextView[contains(@content-desc, "Phone")]'
print(f"🚀 正在模糊點擊: {xpath_phone}")
driver.find_element(AppiumBy.XPATH, xpath_phone).click()
sleep(2)
driver.press_keycode(3)  # 回主畫面
sleep(1)

# --- 項目 2：Messages ---
xpath_messages = '//android.widget.TextView[contains(@content-desc, "Messages")]'
print(f"🚀 正在模糊點擊: {xpath_messages}")
driver.find_element(AppiumBy.XPATH, xpath_messages).click()
sleep(2)
driver.press_keycode(3)
sleep(1)

# --- 項目 3：Chrome ---
xpath_chrome = '//android.widget.TextView[contains(@content-desc, "Chrome")]'
print(f"🚀 正在模糊點擊: {xpath_chrome}")
driver.find_element(AppiumBy.XPATH, xpath_chrome).click()
sleep(2)
driver.press_keycode(3)
sleep(1)

# --- 項目 4：Play Store (原 TMoble 欄位) ---
# 注意：這裡使用 contains 避開了 "Predicted app: " 這一長串前綴
xpath_playstore = '//android.widget.TextView[contains(@content-desc, "Play Store")]'
print(f"🚀 正在模糊點擊: {xpath_playstore}")
driver.find_element(AppiumBy.XPATH, xpath_playstore).click()
sleep(2)
driver.press_keycode(3)
sleep(1)

# --- 結束連線 ---
print("🧹 所有模糊點擊流程結束")
driver.quit()
