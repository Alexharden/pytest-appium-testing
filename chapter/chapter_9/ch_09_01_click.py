from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionBuilder, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 練習
# 1. 連線機制設定
# desired_caps = {
#     "deviceName": "127.0.0.1:21503",
#     "platformName": "Android",
#     "appPackage": "com.dangdang.buy2",
#     "appActivity": "com.dangdang.buy2.activity.ActivityMainTab",
#     "automationName": "UiAutomator2",
#     "noReset": True
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# sleep(3)
# my_ele = driver.find_element(AppiumBy.ID, 'comd.dangdang.buy2:id/tab_personal_iv')
# my_ele.click()
# sleep(2)
# login_ele = driver.find_element(AppiumBy.ID, 'comd.dangdang.buy2:id/tv_agile_user_name')
# ActionChains(driver).click(login_ele).perform()
# sleep(2)
# driver.quit()

# 1. 連線機制設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    # --- 1. 座標定位點擊 (練習 move_to_location) ---
    # 先取得 Phone 的中心座標
    phone_ele = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]'))
    )
    rect = phone_ele.rect
    center_x = rect["x"] + rect["width"] // 2
    center_y = rect["y"] + rect["height"] // 2

    actions = ActionBuilder(driver)
    # 直接移到絕對座標點擊，這不需要依賴元素物件，比較不會噴 Stale 錯誤
    actions.pointer_action.move_to_location(center_x, center_y).pointer_down().pause(0.1).pointer_up()
    actions.perform()
    print("執行：座標定位點擊完成")
    sleep(2)

    # --- 2. 元素 click (練習單純 click) ---
    # 因為剛才點開了 Phone，我們要按 Home 鍵回到主畫面
    driver.press_keycode(3)
    sleep(1)

    # 【重點】必須重新 find，因為頁面刷新過了
    phone_ele = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]'))
    )
    actions = ActionBuilder(driver)
    actions.pointer_action.click(phone_ele)
    actions.perform()
    print("執行：元素點擊 (click) 完成")

    # --- 3. 元素 double_click (練習雙擊) ---
    # 再次回到主畫面
    driver.press_keycode(3)
    sleep(1)

    phone_ele = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]'))
    )
    actions = ActionBuilder(driver)
    # 手動模擬雙擊，避免狀態衝突
    actions.pointer_action.move_to(phone_ele).pointer_down().pointer_up().pause(0.1).pointer_down().pointer_up()
    actions.perform()
    print("執行：手動模擬雙擊完成")

except Exception as e:
    print(f"執行出錯: {e}")
