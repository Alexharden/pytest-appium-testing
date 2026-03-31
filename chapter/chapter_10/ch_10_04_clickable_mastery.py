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
    print(">>> [測試開始] 練習 element_to_be_clickable (可點擊驗證)")
    print("=" * 60)

    driver.activate_app("com.android.chrome")

    # 建立等待物件
    wait = WebDriverWait(driver, 15)

    # 定義搜尋框 Locator (使用 XPATH)
    search_loc = (AppiumBy.XPATH, "//*[contains(@resource-id, 'search_box') or contains(@resource-id, 'url_bar')]")

    # --- 核心練習項目 ---
    print(">>> [步驟] 執行 wait.until(EC.element_to_be_clickable)...")

    # element_to_be_clickable 會同時確認：
    # 1. 元素存在 (Presence)
    # 2. 元素可見 (Visibility)
    # 3. 元素屬性 enabled=true 且屬性 clickable=true
    clickable_element = wait.until(EC.element_to_be_clickable(search_loc))

    # 驗證成功後執行點擊
    clickable_element.click()

    print("✅ [結果] 元素已就緒，成功執行點擊！")
    print("✅ [練習達成] element_to_be_clickable 驗證完成。")
    print("=" * 60)

except Exception as e:
    print(f"❌ [失敗] 元素在時間內無法點擊（可能是隱藏或被禁用）: {e}")

finally:
    print(">>> [結束] 關閉測試 Session。")
    driver.quit()
