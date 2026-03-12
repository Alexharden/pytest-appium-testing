from socket import timeout
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

# 課本練習
# desired_caps = {
#     "deviceName": "127.0.0.1:21503",
#     "platformName": "Android",
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.remove_app("com.miui.calculator", keepData=True, timeout=30000)
# driver.quit()


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": False,
}

# 2. 轉換為 Options 物件
options = UiAutomator2Options().load_capabilities(desired_caps)

# 3. 建立連線
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：移除 App ---

# 使用你確認過的正確包名
package_name = "com.viewsonic.testapk"

# 執行移除
driver.remove_app(
    package_name, keepData=False, timeout=30000
)  # 現階段 keepData=True 移除不了，要移除乾淨要用 adb shell cmd package uninstall -k com.viewsonic.testapk 如果真的要用 keepData=False 是可以刪除的
print(f"✅ App '{package_name}' 已被移除。")

# --- 結束連線 ---
driver.quit()
