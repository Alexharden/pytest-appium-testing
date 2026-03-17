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

    # 3. 獲取元素上的文字並直接印出
    text_value = search_ele.text
    print(f"\n✅ 成功獲取元素的 text 值: [{text_value}]")

except Exception as e:
    print("\n❌ 發生錯誤：")
    print(f"錯誤類型: {e.__class__.__name__}")
    print(f"錯誤訊息: {e}")

finally:
    driver.press_keycode(3)
    sleep(2)
    driver.quit()
