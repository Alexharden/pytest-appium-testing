import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

# 1. 環境設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
    "appium:appPackage": "com.android.chrome",
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print(">>> [開始] 啟動 Chrome...")
    driver.activate_app("com.android.chrome")

    # ------------------------------------------------------
    # 核心：強制等待 (Static Wait / Forced Wait)
    # ------------------------------------------------------
    print(">>> [等待] 現在進入強制等待 5 秒，這期間程式什麼都不會做...")

    time.sleep(5)  # <--- 這就是強制等待

    print(">>> [續行] 5 秒結束，繼續執行後續動作。")
    # ------------------------------------------------------

    # 執行截圖證明等待後的狀態
    filename = "after_forced_wait.png"
    driver.save_screenshot(filename)
    print(f"✅ 截圖已完成: {filename}")

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

finally:
    print(">>> [結束] 關閉 Session。")
    driver.quit()
