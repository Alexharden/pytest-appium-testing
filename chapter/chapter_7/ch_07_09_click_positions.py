from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本練習
# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.miui.calculator",
#     "appActivity": "com.miui.calculator.cal.CalculatorActivity",
#     "platformName": "Android",
#     "platformVersion": "10.0",
#     "noReset": True
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(20)
# driver.tap([427, 1747], 1)
# sleep(3)
# #不能用 driver.quit()，要用 driver.terminate_app()
# driver.terminate_app("com.miui.calculator")


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

# --- 核心練習：座標點擊 (Tap) ---
# 注意：driver.tap 的參數是一個 list 裡面放 tuple 格式：[(x, y)]

# 1. 點擊 Phone (185, 1977)
print("🚀 正在座標點擊: Phone (185, 1977)")
driver.tap([(185, 1977)])
sleep(2)
driver.press_keycode(3)  # 回主畫面
sleep(1)

# 2. 點擊 Messages (434, 1977)
print("🚀 正在座標點擊: Messages (434, 1977)")
driver.tap([(434, 1977)])
sleep(2)
driver.press_keycode(3)
sleep(1)

# 3. 點擊 Chrome (684, 1977)
print("🚀 正在座標點擊: Chrome (684, 1977)")
driver.tap([(684, 1977)])
sleep(2)
driver.press_keycode(3)
sleep(1)

# 4. 點擊 Play Store (945, 1977)
print("🚀 正在座標點擊: Play Store (945, 1977)")
driver.tap([(945, 1977)])
sleep(2)
driver.press_keycode(3)
sleep(1)

# --- 結束連線 ---
print("🧹 座標點擊測試結束")
driver.quit()
