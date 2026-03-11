from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

# # 課本練習
# desired_caps = {
#     "deviceName": "127.0.0.1:21503", 
#     "platformName": "Android",
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.activate_app("com.miui.calculator")
# sleep(3)
# #終止 App
# driver.terminate_app("com.miui.calculator")
# sleep(3)
# driver.quit()



# state=0 app未安裝
# state=1 app未啟動
# state=2 app在後台掛起
# state=3 app在後台運行
# state=4 app在前台啟動

# 1. 基礎連線設定
# 我們指定連線到你的 ViewSonic Test APK
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.viewsonic.testapk",
    "appium:appActivity": ".MainActivity", # 請確認你的正確 Activity 名稱
    "noReset": True
}

options = UiAutomator2Options().load_capabilities(desired_caps)

# 2. 建立連線並開啟 App
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("✅ App 已啟動，等待 3 秒...")
sleep(3)

# 3. 關閉 App
# 課本舊寫法：driver.close_app()
# 現代新寫法：terminate_app("包名")
print("🚀 正在關閉 App (Terminate)...")
driver.terminate_app("com.viewsonic.testapk", timeout=600)
sleep(3)

# 4. 結束連線
print("🧹 測試結束，關閉 Session")
driver.quit()