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
# login_xpath = "//*[@class='android.widget.TextView' and @text='登入/註冊']"
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

# --- 核心練習：XPath Class + Text 的兩種寫法 ---

# 【項目 1：Phone】
# 寫法 A：將 Class 名稱直接作為標籤（Tag Name）。這是業界最標準、效能最好的寫法。
xpath_phone = "//android.widget.TextView[@text='Phone']"

# 寫法 B：使用通配符 * 並將 Class 視為一個屬性過濾（需使用 and 連結）。
# xpath_phone = "//*[@class='android.widget.TextView' and @text='Phone']"

print(f"🚀 正在執行 Phone 定位操作")
driver.find_element(AppiumBy.XPATH, xpath_phone).click()
sleep(2)
driver.press_keycode(3)
sleep(1)


# 【項目 2：Messages】
xpath_messages = "//android.widget.TextView[@text='Messages']"
# xpath_messages = "//*[@class='android.widget.TextView' and @text='Messages']"

print(f"🚀 正在執行 Messages 定位操作")
driver.find_element(AppiumBy.XPATH, xpath_messages).click()
sleep(2)
driver.press_keycode(3)
sleep(1)


# 【項目 3：Chrome】
xpath_chrome = "//android.widget.TextView[@text='Chrome']"
# xpath_chrome = "//*[@class='android.widget.TextView' and @text='Chrome']"

print(f"🚀 正在執行 Chrome 定位操作")
driver.find_element(AppiumBy.XPATH, xpath_chrome).click()
sleep(2)
driver.press_keycode(3)
sleep(1)


# 【項目 4：Play Store】
xpath_play = "//android.widget.TextView[@text='Play Store']"
# xpath_play = "//*[@class='android.widget.TextView' and @text='Play Store']"

print(f"🚀 正在執行 Play Store 定位操作")
driver.find_element(AppiumBy.XPATH, xpath_play).click()
sleep(2)
driver.press_keycode(3)
sleep(1)

# --- 結束連線 ---
driver.quit()
