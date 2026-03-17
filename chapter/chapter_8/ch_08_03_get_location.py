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

# 設定智能等待，最長等 10 秒
wait = WebDriverWait(driver, 10)

try:
    # 1. 點擊電話圖示進入首頁
    print("正在尋找 Phone 圖示...")
    phone_icon = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Phone")))
    phone_icon.click()
    print("已點擊 Phone，等待搜尋框出現...")

    # 2. 使用 ID 定位搜尋框
    search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    search_ele = wait.until(EC.presence_of_element_located((AppiumBy.ID, search_id)))

    # --- 核心測試區塊 ---

    # 方法一：使用 location 獲取絕對座標
    loc_absolute = search_ele.location
    print(f"\n📍 [方法一] location (絕對座標):")
    print(f"   X 軸 = {loc_absolute.get('x')}, Y 軸 = {loc_absolute.get('y')}")

    # 方法二：使用 location_in_view 獲取可視區域內的座標
    loc_in_view = search_ele.location_in_view
    print(f"\n👁️ [方法二] location_in_view (可視範圍座標):")
    print(f"   X 軸 = {loc_in_view.get('x')}, Y 軸 = {loc_in_view.get('y')}")

    # 比較兩者是否相同 (好玩加碼測試)
    if loc_absolute == loc_in_view:
        print("\n✅ 觀察結果：因為畫面沒有經過滑動，目前絕對座標與可視座標完全一致！")
    else:
        print("\n🔍 觀察結果：數值不同，代表這個頁面可能經過了滑動或有特定的 UI 框架差異。")

except Exception as e:
    print("\n❌ 發生錯誤：")
    print(f"錯誤類型: {e.__class__.__name__}")
    print(f"錯誤訊息: {e}")

finally:
    driver.press_keycode(3)
    sleep(2)
    driver.quit()
