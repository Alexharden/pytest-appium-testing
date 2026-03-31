import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
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
    print(">>> [測試開始] 練習 Lambda 自定義等待 (Flexible Waiting)")
    print("=" * 60)

    driver.activate_app("com.android.chrome")

    # 建立等待物件
    wait = WebDriverWait(driver, 15)

    # 定義搜尋框 Locator (Tuple 格式)
    search_loc = (AppiumBy.XPATH, "//*[contains(@resource-id, 'search_box') or contains(@resource-id, 'url_bar')]")

    # --- 核心練習項目：Lambda 運算式 ---
    print(">>> [步驟] 執行 wait.until(lambda x: x.find_element(*search_loc))...")

    # x 代表傳入的 driver
    # *search_loc 是將 Tuple (By, Value) 拆解成兩個參數傳給 find_element
    element = wait.until(lambda x: x.find_element(*search_loc))

    # 驗證成功後執行點擊
    element.click()

    print("✅ [結果] Lambda 成功捕獲元素並執行點擊！")
    print("✅ [練習達成] 自定義 Lambda 等待驗證完成。")
    print("=" * 60)

except Exception as e:
    print(f"❌ [失敗] Lambda 等待超時或元素定位錯誤: {e}")

finally:
    print(">>> [結束] 關閉測試 Session。")
    driver.quit()
