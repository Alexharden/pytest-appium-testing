from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 課本練習
# '''
# 獲取包和activity
# '''
# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.dangdan.buy2",
#     "appActivity": "dangdang.buy2.activity.ActivityMainTab",
#     "platformName": "Android",
#     "noReset": True
# }

# drvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# package = drvier.current_activity
# print("package:{}".format(package))
# activity = drvier.current_activity()
# print("activity:{}".format(activity))
# drvier.quit()


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.viewsonic.testapk",
    "appium:appActivity": ".MainActivity",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)

# 2. 建立連線
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：獲取當前 App 資訊 ---

# 獲取當前包名 (Package) 這是 App 的唯一識別碼（身分證字號）。
# 注意：這是屬性，不需要加括號 ()
current_pkg = driver.current_package
print("當前包名 (Package): {}".format(current_pkg))

# 獲取當前活動名稱 (Activity) 這是 App 裡面的單一畫面。
# 注意：這也是屬性，不需要加括號 ()
current_act = driver.current_activity
print("當前活動 (Activity): {}".format(current_act))
# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()
