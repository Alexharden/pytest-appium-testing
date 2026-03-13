from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# --- 1. 設定 Capabilities ---
desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    # ==========================================
    # 第一部分：使用 ID / Class 定位檢查狀態
    # ==========================================
    print("--- 開始第一段：ID/Class 操作 ---")
    
    # 進入 Battery 頁面
    battery_menu = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='Battery']")))
    battery_menu.click()
    print("✅ 成功進入 Battery 頁面")

    # 定位 Switch 開關
    switch_ele = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.Switch")))

    # 獲取初始狀態
    initial_status = switch_ele.get_attribute("checked") == "true"
    print(f"ID 檢查：初始狀態為【{'開啟' if initial_status else '關閉'}】")
    
    # 執行切換
    switch_ele.click()
    sleep(1) # 🌟 重要：等待動畫完成
    
    new_status = switch_ele.get_attribute("checked") == "true"
    print(f"ID 檢查：切換後狀態為【{'開啟' if new_status else '關閉'}】")

    # 🌟 為了確保第二段測試一致，如果狀態變了，我們把它切換回初始狀態
    if new_status != initial_status:
        print("正在還原初始狀態以利第二段測試...")
        switch_ele.click()
        sleep(1)

    # 返回、返回、Home
    print("第一段完成：執行返回、返回、Home...")
    driver.back()
    sleep(1)
    driver.back()
    sleep(1)
    driver.press_keycode(3)
    sleep(2)

    # ==========================================
    # 第二部分：全部使用 XPath 定位檢查狀態
    # ==========================================
    print("\n--- 開始第二段：XPath 操作 ---")
    
    # 重新啟動 Settings
    driver.activate_app("com.android.settings")
    
    # XPath 進入 Battery
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='Battery']"))).click()

    # XPath 定位 Switch
    switch_xpath = "//android.widget.Switch"
    switch_xp_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, switch_xpath)))

    # 獲取 XPath 流程的初始狀態
    xp_initial_status = switch_xp_ele.get_attribute("checked") == "true"
    print(f"XPath 檢查：初始狀態為【{'開啟' if xp_initial_status else '關閉'}】")

    # 執行切換
    switch_xp_ele.click()
    
    # 🌟 關鍵修正：給系統時間更新屬性，否則會抓到舊的狀態
    sleep(1) 

    xp_final_status = switch_xp_ele.get_attribute("checked")
    print(f"✅ XPath 驗證：切換動作已完成，目前屬性值為: {xp_final_status}")

    # 導覽回桌面
    print("第二段完成：執行返回、返回、Home...")
    driver.press_keycode(4)
    sleep(1)
    driver.press_keycode(4)
    sleep(1)
    driver.press_keycode(3)

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

finally:
    sleep(2)
    driver.quit()
    print("\n測試結束。")