from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

## 課本的寫法
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "emulator-5554",
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# driver.install_app("E:\com.miui.calculator.apk")

# driver.quit


# 設定連線資訊：這裡我們先連到「設定」，確保 Session 建立成功
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.android.settings",
    "appium:appActivity": ".Settings",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)

# 1. 建立連線 (會先看到模擬器打開「設定」)
driver = webdriver.Remote("http://localhost:4723", options=options)
print("成功連線 Appium...")

# 2. 執行安裝 App 的動作
# 請確認這個路徑下的檔案真的存在，不然會噴 WebDriverException
apk_path = "/Users/harden.cc.hsieh/Downloads/test_apk.apk"
print(f"正在安裝 App: {apk_path}")

driver.install_app(apk_path)
print("安裝完成！")

# 3. (選做) 如果安裝完想直接打開它，可以加這行
# driver.activate_app("你的.app.package.name")

sleep(5)
driver.quit()
