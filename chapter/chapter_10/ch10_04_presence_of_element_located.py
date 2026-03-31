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
    print(">>> [測試開始] 僅使用 Presence_of_element_located 驗證流程")
    print("=" * 60)

    driver.activate_app("com.android.chrome")

    # 建立等待物件 (Explicit Wait)
    wait = WebDriverWait(driver, 15)

    # 定義搜尋框 Locator (使用 XPATH 兼容不同版本的 Chrome ID)
    search_loc = (AppiumBy.XPATH, "//*[contains(@resource-id, 'search_box') or contains(@resource-id, 'url_bar')]")

    # --- 核心練習項目 ---
    print(">>> [步驟] 執行 wait.until(EC.presence_of_element_located)...")

    # 此方法會持續輪詢，直到元素出現在 XML 樹中
    search_bar = wait.until(EC.presence_of_element_located(search_loc))

    # 點擊以確認該元素確實可用
    search_bar.click()

    print("✅ [結果] 成功偵測到元素存在並執行點擊！")
    print("✅ [練習達成] Presence_of_element_located 驗證完成。")
    print("=" * 60)

except Exception as e:
    print(f"❌ [失敗] 元素未在預期時間內出現: {e}")

finally:
    print(">>> [結束] 關閉測試 Session。")
    driver.quit()
