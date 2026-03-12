from time import sleep

from appium import webdriver

# 1. 必須匯入這個 Options 類別
from appium.options.android import UiAutomator2Options

# #課本寫法
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# #虛擬器設備
# desired_caps['platformVersion'] = '7.1.2'
# desired_caps['deviceName'] = '127.0.0.1:21503'
# #App的存放路徑
# desired_caps['app'] = 'E:\com.miui.calculator.apk'
# #App的包名和Activity
# desired_caps['appPackage'] = 'com.miui.calculator'
# desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'
# #安裝並啟動App
# driver = webdriver.Remote("http://localhost:4723", desired_caps)
# #等待三秒
# sleep(3)
# driver.quit()


desired_caps = {
    "platformName": "Android",  # 系統
    "appium:automationName": "UiAutomator2",  # 自動化引擎
    "appium:deviceName": "emulator-5554",  # 設備名稱
    "appium:platformVersion": "14.0",  # 這裡建議改成你 Android Studio 下載的真實版本 (API 34 是 14.0)
    "appium:appPackage": "com.android.settings",  # App的包名
    "appium:appActivity": ".Settings",  # App的Activity
    "noReset": True,  # 不重置應用程式狀態
}

# 2. 將字典轉換成 Options 物件
options = UiAutomator2Options().load_capabilities(desired_caps)

# 3. 使用 options 參數連線，並去掉舊版的 /wd/hub 路徑
# Appium 2.x Server 預設路徑通常直接是 http://localhost:4723
driver = webdriver.Remote("http://localhost:4723", options=options)

print("成功連線 Appium，正在等待 5 秒...")
sleep(5)

driver.quit()
