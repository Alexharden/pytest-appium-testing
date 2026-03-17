from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    # --- 第一段：使用 ID 定位與檢查 ---
    print("--- 開始第一段：ID 操作 ---")
    phone_icon = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Phone")))
    if phone_icon.is_displayed():
        print("✅ ID: 確認 Phone 圖示已顯示")
        phone_icon.click()

    # 1. 檢查外層假框
    fake_search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    fake_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, fake_search_id)))
    if fake_bar.is_displayed():
        print("✅ ID: 確認外層搜尋框已顯示，執行點擊")
        fake_bar.click()
        sleep(1)

    # 2. 檢查內層真框
    real_search_id = "com.google.android.dialer:id/open_search_view_edit_text"
    real_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, real_search_id)))
    if real_bar.is_displayed():
        print("✅ ID: 確認真正輸入框已顯示")
        real_bar.send_keys("123456")

    # 🌟 修改點：組合返回動作 (確保退乾淨再跑下一段)
    if driver.is_keyboard_shown():
        driver.hide_keyboard()

    print("ID 流程：執行返回與 Home...")
    driver.back()  # 返回撥號首頁
    sleep(1)
    driver.press_keycode(3)  # 回到桌面
    sleep(2)

    # --- 第二段：全部使用 XPath 定位與檢查 ---
    print("\n--- 開始第二段：XPath 操作 ---")

    # 1. 點擊電話 (XPath)
    phone_xpath = '//android.widget.TextView[@content-desc="Phone"]'
    phone_icon_xp = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, phone_xpath)))
    if phone_icon_xp.is_displayed():
        print("✅ XPath: 確認 Phone 圖示已顯示")
        phone_icon_xp.click()

    # 2. 檢查外層假框 (XPath)
    fake_xpath = '//android.widget.TextView[@resource-id="com.google.android.dialer:id/open_search_bar_text_view"]'
    fake_bar_xp = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, fake_xpath)))
    if fake_bar_xp.is_displayed():
        print("✅ XPath: 確認外層搜尋框已顯示")
        fake_bar_xp.click()
        sleep(1)

    # 3. 檢查內層真框 (XPath)
    real_xpath = '//android.widget.EditText[@resource-id="com.google.android.dialer:id/open_search_view_edit_text"]'
    real_bar_xp = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, real_xpath)))
    if real_bar_xp.is_displayed():
        print("✅ XPath: 確認真正輸入框已顯示")
        real_bar_xp.send_keys("987654")

    # 🌟 修改點：使用連按兩次返回的策略
    print("XPath 流程：執行連按兩次返回與 Home...")
    driver.press_keycode(4)  # 第一次 Back (收鍵盤)
    sleep(0.5)
    driver.press_keycode(4)  # 第二次 Back (回 App 首頁)
    sleep(0.5)
    driver.press_keycode(3)  # Home (回桌面)

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

finally:
    sleep(2)
    # 建議加上 terminate，確保下次執行時 App 是冷啟動
    driver.terminate_app("com.google.android.dialer")
    driver.quit()
