import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 引入預設的判斷條件
from selenium.webdriver.support import expected_conditions as EC

# 引入顯示等待的核心類別
from selenium.webdriver.support.ui import WebDriverWait

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
    print(">>> [操作] 啟動 Chrome...")
    driver.activate_app("com.android.chrome")

    # ------------------------------------------------------
    # 核心設定：顯示等待 (Explicit Wait) - until
    # ------------------------------------------------------
    # 建立等待物件：最多等 10 秒，每 0.5 秒檢查一次
    wait = WebDriverWait(driver, 10)

    print(">>> [等待] 正在等待搜尋框出現在畫面上，且必須是『可見』狀態...")

    # 使用 until：直到 元素出現 (presence) 且 可見 (visibility)
    search_bar = wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.android.chrome:id/search_box_text")))

    # 一旦條件達成，wait.until 會直接回傳該元素物件
    search_bar.click()
    print("✅ 成功！條件達成，已點擊搜尋框。")

    # 截圖存檔
    driver.save_screenshot("explicit_wait_until.png")

except Exception as e:
    print(f"❌ 逾時未達成條件: {e}")

finally:
    driver.quit()
