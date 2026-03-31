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
    print("\n" + "=" * 60)
    print(">>> [測試開始] 練習 visibility_of_element_located (可見度驗證)")
    print("=" * 60)

    driver.activate_app("com.android.chrome")

    # 建立等待物件
    wait = WebDriverWait(driver, 15)

    # 定義搜尋框 Locator
    # 這裡我們找 Chrome 的網址列容器，它必須「完全顯示」在畫面上
    search_loc = (AppiumBy.XPATH, "//*[contains(@resource-id, 'search_box') or contains(@resource-id, 'url_bar')]")

    # --- 核心練習項目 ---
    print(">>> [步驟] 執行 wait.until(EC.visibility_of_element_located)...")

    # visibility_of_element_located 會檢查：
    # 1. 元素是否存在於 DOM 中
    # 2. 元素是否在螢幕上可見 (Displayed)
    visible_element = wait.until(EC.visibility_of_element_located(search_loc))

    # 驗證成功後進行點擊
    visible_element.click()

    print("✅ [結果] 元素已成功顯示並執行點擊！")
    print("✅ [練習達成] visibility_of_element_located 驗證完成。")
    print("=" * 60)

except Exception as e:
    print(f"❌ [失敗] 元素在時間內未顯示在畫面上: {e}")

finally:
    print(">>> [結束] 關閉測試 Session。")
    driver.quit()
