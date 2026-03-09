from appium import webdriver
from time import sleep

# 課本練習
# desired_caps = {"deviceName": "127.0.0.1:21503", 
# "appPackage": "com.miui.calculator", 
# "appActivity": "com.miui.calculator.cal.CalculatorActivity",
# "platformName": "Android",
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# sleep(3)
# #借助 close_app，關閉 App
# driver.close_app()
# sleep(3)

# #使用 launch_app()，重啟 app
# driver.launch_app()
# sleep(3)
# driver.quit()


from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

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
driver.terminate_app("com.viewsonic.testapk")
sleep(3)

# 4. 重新啟動 App
# 課本舊寫法：driver.launch_app()
# 現代新寫法：activate_app("包名")
print("🚀 正在重新啟動 App (Activate)...")
driver.activate_app("com.viewsonic.testapk")
sleep(3)

# 5. 結束連線
print("🧹 測試結束，關閉 Session")
driver.quit()