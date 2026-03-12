import os
from dataclasses import replace

from appium import webdriver
from appium.options.android import UiAutomator2Options

## 課本的寫法
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "emulator-5554",
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# driver.install_app(app_path="E:\\com.miui.calculator.apk", replace=True, timeout=10000, allow_test_packages=True,useSdcard=True,grant_permissions=False)

# driver.quit()


# 1. 建議使用動態路徑，避免路徑寫死出錯
# 假設你的 APK 放在目前資料夾下的 apk 子目錄內
apk_path = "/Users/harden.cc.hsieh/Downloads/test_apk.apk"

# 2. 現代化設定 (Capabilities)
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",  # 改成你的模擬器 ID
    "appium:platformVersion": "14.0",  # 改成你的 Android 版本
    "appium:appPackage": "com.android.settings",  # 先啟動一個基礎 App
    "appium:appActivity": ".Settings",
    "noReset": True,
}

# 3. 轉換為 Options 物件 (新版強制要求)
options = UiAutomator2Options().load_capabilities(desired_caps)

# 4. 建立連線 (移除 /wd/hub)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# 5. 執行安裝練習
# 課本的參數在 Appium Python Client 中要對應正確的參數名
print(f"正在安裝 App: {apk_path}")
driver.install_app(
    app_path=apk_path,
    replace=True,
    timeout=60000,  # 注意：這裡的單位通常是毫秒 (ms)
    allow_test_packages=True,
    useSdcard=True,
    grant_permissions=False,
)
print("安裝成功！")

# 6. 結束連線 (記得加括號)
driver.quit()
