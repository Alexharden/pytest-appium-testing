import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
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
    print(">>> [操作] 啟動 Chrome 並點擊搜尋框...")
    driver.activate_app("com.android.chrome")

    # 建立等待物件
    wait = WebDriverWait(driver, 10)

    # 先用 until 等待搜尋框出現並點擊
    search_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/search_box_text")))
    search_bar.click()

    # ------------------------------------------------------
    # 核心設定：顯示等待 (Explicit Wait) - until_not
    # ------------------------------------------------------
    print(">>> [測試] 現在搜尋框應該已經被啟動，原來的入口應該要消失...")

    # 使用 until_not：直到 該元素「從畫面上消失」或「不再顯示」
    # 我們等原本那個 search_box_text 消失，代表已經進入了輸入模式
    is_gone = wait.until_not(EC.presence_of_element_located((AppiumBy.ID, "com.android.chrome:id/search_box_text")))

    if is_gone:
        print("✅ 成功！原本的搜尋框入口已消失，證明頁面已切換。")

    # 截圖存檔
    driver.save_screenshot("explicit_wait_until_not.png")

except Exception as e:
    print(f"❌ 條件未達成（元素沒消失）: {e}")

finally:
    driver.quit()
