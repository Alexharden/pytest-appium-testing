from time import sleep

# 練習二
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 課本的寫法
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "emulator-5554",
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# # 判斷App是否安裝，傳遞參數為包名
# res = driver.is_app_installed("com.android.settings")
# #輸出結果為是一個布林值，即True or False
# print(res)
# driver.quit()


##練習一，看setting 設定在不在
# 設定連線資訊：這裡我們先連到「設定」，確保 Session 建立成功
# desired_caps = {
#     "platformName": "Android",
#     "appium:automationName": "UiAutomator2",
#     "appium:deviceName": "emulator-5554",      # 改成你的模擬器 ID
#     "appium:platformVersion": "14.0",          # 改成你的 Android 版本
#     "appium:appPackage": "com.android.settings", # 先啟動一個基礎 App
#     "appium:appActivity": ".Settings",
#     "noReset": True
# }

# # 2. 轉換為 Options 物件 (新版強制要求)
# options = UiAutomator2Options().load_capabilities(desired_caps)

# # 3. 建立連線 (移除 /wd/hub)
# driver = webdriver.Remote("http://localhost:4723", options=options)

# # 4. 執行檢查動作
# package_name = "com.android.settings"

# # 檢查 App 是否已安裝
# is_installed = driver.is_app_installed(package_name)

# if is_installed:
#     print(f"✅ 恭喜！App '{package_name}' 已經安裝在模擬器上了。")
# else:
#     print(f"❌ 抱歉，App '{package_name}' 尚未安裝。")

# # 5. 結束連線 (記得加括號)
# driver.quit()


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True,
}

# 2. 轉換為 Options 物件
options = UiAutomator2Options().load_capabilities(desired_caps)

# 3. 建立連線
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：判斷 ViewSonic Test APK 是否安裝 ---

# 使用你確認過的正確包名
package_name = "com.viewsonic.testapk"

# 執行判斷，res 會拿到 True 或 False
res = driver.is_app_installed(package_name)

if res:
    print(f"✅ 確認成功：{package_name} 已經安裝在模擬器中了！")
else:
    print(f"❌ 確認失敗：手機裡找不到 {package_name}，請檢查安裝步驟。")

# --- 結束連線 ---
driver.quit()
