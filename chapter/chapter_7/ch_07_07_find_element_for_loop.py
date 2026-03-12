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
# driver.find_element(By.ID,'com.miui.calculator:id/btn_1_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_2_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_3_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_4_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_5_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_6_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_7_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_8_s').click()
# driver.find_element(By.ID,'com.miui.calculator:id/btn_9_s').click()

# sleep(3)
# driver.quit()

# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.dangdan.buy2",
#     "appActivity": "dangdang.buy2.activity.ActivityMainTab",
#     "platformName": "Android",
#     "noReset": True
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# mylst = driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
# for ele in mylst[0:-1]:
#     ele.click()

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

# --- 核心練習：find_elements 批次點擊 + Keycode 操作 ---

# 1. 定位到 hotseat 區域內的所有 TextView (對應你的截圖)
# 這樣可以精確抓到 Phone, Messages, Chrome, TMoble 這四個元素
app_elements = driver.find_elements(
    AppiumBy.XPATH,
    '//android.view.ViewGroup[@resource-id="com.google.android.apps.nexuslauncher:id/hotseat"]//android.widget.TextView',
)

print(f"📊 偵測到快捷列共有 {len(app_elements)} 個 App")

# 2. 執行迴圈點擊
for index, app in enumerate(app_elements):
    app_name = app.text
    print(f"🚀 正在測試第 {index + 1} 個 App: {app_name}")

    # 點擊進入 App
    app.click()
    sleep(2)  # 等待 App 啟動動畫

    # 執行 press_keycode(3) 回到桌面
    # 3 是 Android 的 HOME 鍵代碼
    driver.press_keycode(3)
    print(f"🏠 已按下 Home 鍵，回到桌面準備下一個測試")
    sleep(1)

# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()
