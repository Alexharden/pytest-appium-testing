from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

# 課本練習
# desired_caps = {"deviceName": "127.0.0.1:21503",
# "appPackage": "com.miui.calculator",
# "appActivity": "com.miui.calculator.cal.CalculatorActivity",
# "platformName": "Android",
# }
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# sleep(3)
# # 使用 background_app(seconds=3) 讓 App 進入背景
# driver.background_app(seconds=3)
# sleep(3)
# driver.quit()

# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.viewsonic.testapk",
    "appium:appActivity": ".MainActivity",
    "noReset": False,
}

# 2. 轉換為 Options 物件 (解決 TypeError)
options = UiAutomator2Options().load_capabilities(desired_caps)

# 3. 建立連線 (移除 /wd/hub)
driver = webdriver.Remote("http://localhost:4723", options=options)

print("✅ App 已啟動，準備執行背景切換練習...")
sleep(3)

# --- 核心練習：將 App 推到背景 ---
# seconds=5 代表 App 會在背景待 5 秒，然後自動回到前景
print("🚀 執行：讓 App 進入背景 5 秒...")
driver.background_app(seconds=5)

# 注意：這行指令執行時，你會看到模擬器回到桌面，5 秒後 App 會自己跳回來
print("✅ App 應該已經自動回到前景了")

sleep(3)

# 4. 結束連線
print("🧹 測試結束，關閉 Session")
driver.quit()
