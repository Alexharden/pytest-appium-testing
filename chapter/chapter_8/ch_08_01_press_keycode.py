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

# 設定智能等待
wait = WebDriverWait(driver, 10)

try:
    # --- 第一段：使用 ID 定位 ---
    print("--- 開始第一段：ID 操作 (press_keycode) ---")

    # 1. 點擊電話圖示
    phone_icon_ele = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Phone")))
    phone_icon_ele.click()
    print("點到了 Phone")

    # 2. 定位假搜尋框並點擊
    fake_search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    wait.until(EC.element_to_be_clickable((AppiumBy.ID, fake_search_id))).click()

    # 3. 定位真輸入框並取得焦點
    real_search_id = "com.google.android.dialer:id/open_search_view_edit_text"
    real_search_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, real_search_id)))
    real_search_bar.click()
    sleep(1)

    # 4. 迴圈輸入 (加上 sleep 避免崩潰)
    for digit in "123456789":
        driver.press_keycode(int(digit) + 7)
        sleep(0.3)
    print("ID 流程輸入成功")

    # 5. 清空內容
    real_search_bar.clear()

    # 🌟 修改點：組合返回動作 (確保退乾淨再跑下一段)
    print("ID 流程：執行返回、返回、Home...")
    driver.press_keycode(4)  # 返回 1: 收鍵盤
    sleep(1)
    driver.press_keycode(4)  # 返回 2: 退出搜尋，回撥號首頁
    sleep(1)
    driver.press_keycode(3)  # 按下 Home: 回桌面
    print("ID 流程完成")
    sleep(2)

    # --- 第二段：全部使用 XPath 定位 ---
    print("\n--- 開始第二段：XPath 操作 (press_keycode) ---")

    # 1. 點擊電話圖示
    phone_xpath = '//android.widget.TextView[@content-desc="Phone"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, phone_xpath))).click()

    # 2. 點擊假搜尋框
    fake_search_xpath = (
        '//android.widget.TextView[@resource-id="com.google.android.dialer:id/open_search_bar_text_view"]'
    )
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, fake_search_xpath))).click()

    # 3. 定位真輸入框並取得焦點
    real_search_xpath = (
        '//android.widget.EditText[@resource-id="com.google.android.dialer:id/open_search_view_edit_text"]'
    )
    real_search_bar_xp = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, real_search_xpath)))
    real_search_bar_xp.click()
    sleep(1)

    # 4. 迴圈輸入
    for digit in "987654321":
        driver.press_keycode(int(digit) + 7)
        sleep(0.3)
    print("XPath 流程輸入成功")

    # 5. 清空內容
    real_search_bar_xp.clear()

    # 🌟 修改點：同樣執行連按兩次返回的策略
    print("XPath 流程：執行返回、返回、Home...")
    driver.press_keycode(4)  # 返回 1: 收鍵盤
    sleep(1)
    driver.press_keycode(4)  # 返回 2: 回首頁
    sleep(1)
    driver.press_keycode(3)  # 按下 Home: 回桌面

except Exception as e:
    print(f"\n❌ 發生錯誤: {e.__class__.__name__}\n{e}")

finally:
    sleep(2)
    driver.terminate_app("com.google.android.dialer")
    driver.quit()
    print("\n測試結束。")
