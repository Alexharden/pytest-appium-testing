from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from time import sleep

# --- 連線設定 ---
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2"
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

def reset_and_find():
    """
    【避雷針 1：StaleElement 處理】
    每次動作後頁面可能跳轉，舊的元素物件會失效。
    透過回首頁並重新定位，確保每次練習的 DOM 都是新的。
    """
    driver.press_keycode(3) # 按下 Home 鍵
    sleep(1.5)
    return wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]')))

try:
    # --- 1-4. 底層座標動作組 (針對螢幕座標) ---
    phone_ele = reset_and_find()
    rect = phone_ele.rect
    x, y = int(rect['x'] + rect['width'] / 2), int(rect['y'] + rect['height'] / 2)
    
    actions = ActionBuilder(driver)
    # move_to_location: 移到螢幕絕對座標 (x, y)
    # pointer_down / pointer_up: 物理級的「壓下」與「抬起」
    # pause: 動作間的停頓 (秒)
    actions.pointer_action.move_to_location(x, y).pointer_down().pause(0.1).pointer_up()
    actions.perform()
    print("1-4. [座標類] move_to_location, pointer_down, pointer_up, pause 完成")

    # --- 5. Click (針對元素) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # click: 自動計算元素中心並執行 Down + Up 的封裝方法
    actions.pointer_action.click(phone_ele)
    actions.perform()
    print("5. [元素類] click 完成")

    # --- 6. Double Click (手動模擬版) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # 【避雷針 2：Double Click 狀態衝突】
    # 原生 double_click 容易因間隔太短報錯 pointerDown 衝突。
    # 手動用 pause(0.1) 隔開兩次點擊是最穩的做法。
    actions.pointer_action.move_to(phone_ele).pointer_down().pointer_up().pause(0.1).pointer_down().pointer_up()
    actions.perform()
    print("6. [複合類] double_click 手動模擬完成")

    # --- 7. Context Click (長按選單) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # context_click: 模擬滑鼠右鍵，在 Android 代表觸發長按選單 (ContextMenu)
    actions.pointer_action.context_click(phone_ele)
    actions.perform()
    print("7. [特殊類] context_click 完成")

    # --- 8-11. 按住、移動、釋放、偏移 (連鎖動作) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # move_to: 移到元素的中心點
    # click_and_hold: 按住不放 (狀態維持在 Down)
    # move_by: 相對偏移 (從目前位置往右移 100 像素) -> 【注意：不是 move_by_offset】
    # release: 釋放所有按下的指標 (狀態轉為 Up)
    actions.pointer_action.move_to(phone_ele).click_and_hold().move_by(100, 0).release()
    actions.perform()
    print("8-11. [狀態類] move_to, click_and_hold, move_by, release 完成")

except Exception as e:
    print(f"執行出錯: {e}")

finally:
    driver.quit()