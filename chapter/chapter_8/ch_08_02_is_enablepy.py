from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# --- 配置參數 ---
desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "ensureWebviewsHavePages": True,
    "nativeWebScreenshot": True,
    "newCommandTimeout": 3600,
    "connectHardwareKeyboard": True
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    # ==========================================
    # 第一部分：使用 ID 定位 (高效率 send_keys 版)
    # ==========================================
    print("--- 開始 ID 操作流程 ---")
    
    # 1. 進入撥號 App
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Phone"))).click()
    print("✅ 已進入 Phone App")

    # 2. 處理「假」搜尋框 (TextView)
    fake_search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    wait.until(EC.element_to_be_clickable((AppiumBy.ID, fake_search_id))).click()
    print("✅ 已點擊外層假搜尋框")

    # 3. 處理「真」輸入框 (EditText)
    real_search_id = "com.google.android.dialer:id/open_search_view_edit_text"
    real_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, real_search_id)))
    
    # 快速輸入與清空
    real_bar.send_keys("123456789")
    print(f"✅ ID 成功輸入內容: {real_bar.text}")
    sleep(1)
    
    real_bar.clear()
    print("✅ ID 內容已清空")

    # 4. 返回桌面邏輯
    if driver.is_keyboard_shown():
        driver.hide_keyboard()
    
    driver.back() # 回到 App 首頁
    sleep(1)
    driver.press_keycode(3) # 回到桌面
    print("✅ ID 流程完成，已回到桌面")
    sleep(2)

    # ==========================================
    # 第二部分：使用 XPath 定位 (高效率 send_keys 版)
    # ==========================================
    print("\n--- 開始 XPath 操作流程 ---")
    
    # 1. 再次點擊 Phone (XPath)
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]'))).click()

    # 2. 點擊假搜尋框 (XPath)
    fake_xp = '//android.widget.TextView[@resource-id="com.google.android.dialer:id/open_search_bar_text_view"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, fake_xp))).click()

    # 3. 定位真輸入框
    real_xp = '//android.widget.EditText[@resource-id="com.google.android.dialer:id/open_search_view_edit_text"]'
    real_bar_xp = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, real_xp)))
    
    # 快速輸入
    real_bar_xp.send_keys("987654321")
    print(f"✅ XPath 成功輸入內容: {real_bar_xp.text}")
    sleep(1)
    
    # 4. 退出流程 (雙重 Back 確保萬無一失)
    print("執行返回與 Home 動作...")
    driver.press_keycode(4) # 第一次 Back (收鍵盤)
    sleep(0.5)
    driver.press_keycode(4) # 第二次 Back (回 App 首頁)
    sleep(0.5)
    driver.press_keycode(3) # Home (回桌面)

except Exception as e:
    print(f"❌ 腳本執行失敗: {e}")

finally:
    sleep(2)
    # 確保 App 關閉，下次測試不衝突
    driver.terminate_app("com.google.android.dialer")
    driver.quit()
    print("\n測試結束，連線已斷開。")