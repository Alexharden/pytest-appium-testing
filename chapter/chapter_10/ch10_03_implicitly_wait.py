import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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
    # ------------------------------------------------------
    # 核心設定：隱性等待 (Implicitly Wait)
    # ------------------------------------------------------
    # 這行之後，所有的 find_element 都會自動獲得「超能力」：
    # 沒看到元素不會立刻報錯，而是會持續輪詢直到 10 秒逾時。
    driver.implicitly_wait(10)
    print(">>> [設定] 已開啟全域隱性等待：10 秒")

    print(">>> [操作] 啟動 Chrome 並喚醒...")
    driver.activate_app("com.android.chrome")

    # 模擬 Chrome 開啟很慢的情況，隱性等待會在這裡發揮作用
    print(">>> [尋找] 正在嘗試定位搜尋框...")

    # 注意：這裡不需要寫 time.sleep()！
    search_bar = driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text")
    search_bar.click()
    print("✅ 成功定位並點擊搜尋框！")

    # ------------------------------------------------------
    # 執行截圖：驗證隱性等待後的成果
    # ------------------------------------------------------
    screenshot_name = "implicit_wait_success.png"
    driver.save_screenshot(screenshot_name)
    print(f"📸 截圖已儲存為: {screenshot_name}")

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

finally:
    print(">>> [結束] 關閉 Session。")
    driver.quit()
