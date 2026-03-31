import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 1. 環境設定 (純原生，不需要 chromedriver)
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:appPackage": "com.android.chrome",
    "appium:noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 15)

try:
    print(". 開始測試...")
    driver.activate_app("com.android.chrome")

    # --- Case 1: presence_of_element_located ---
    # 等待搜尋入口出現
    search_input_loc = (AppiumBy.ID, "com.android.chrome:id/search_box_text")
    wait.until(EC.presence_of_element_located(search_input_loc))
    print("✅ 元素已存在於 DOM 中")

    # --- Case 2: element_to_be_clickable ---
    # 確認它可以點擊後才執行 click
    wait.until(EC.element_to_be_clickable(search_input_loc)).click()
    print("✅ 元素可點擊並已執行 click")

    # --- Case 3: text_to_be_present_in_element ---
    # 等待畫面上出現特定的提示文字 (例如搜尋建議)
    hint_loc = (AppiumBy.XPATH, "//*[contains(@text, 'Search')]")
    wait.until(EC.text_to_be_present_in_element(hint_loc, "Search"))
    print("✅ 文字內容符合預期")

    # --- Case 4: invisibility_of_element_located ---
    # 點擊後，原本的首頁搜尋框應該要「消失」或被遮蓋
    wait.until(EC.invisibility_of_element_located(search_input_loc))
    print("✅ 原元素已成功消失 (進入輸入模式)")

    # --- Case 5: visibility_of_any_elements_located ---
    # 等待畫面上出現任何一個搜尋建議列表項
    suggestion_loc = (AppiumBy.ID, "com.android.chrome:id/line_1")
    suggestions = wait.until(EC.visibility_of_any_elements_located(suggestion_loc))
    print(f"✅ 成功看到複數元素，數量：{len(suggestions)}")

except Exception as e:
    print(f"❌ 測試失敗: {e}")

finally:
    driver.quit()
