from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from time import sleep

# --- 基礎連線設定 ---
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
    【避雷針 1：處理 StaleElement 與 物理狀態重置】
    1. 每點開一個 App，原本主畫面的 DOM 就會失效，必須重新 find_element。
    2. 按下 Home 鍵 (keycode 3) 除了回首頁，也能強制讓手機端未完成的觸控狀態 (Down) 被中斷。
    """
    driver.press_keycode(3) 
    sleep(1.5)
    return wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]')))

try:
    # --- 1-4. 底層座標動作組 (針對螢幕座標的精確控制) ---
    phone_ele = reset_and_find()
    rect = phone_ele.rect
    x, y = int(rect['x'] + rect['width'] / 2), int(rect['y'] + rect['height'] / 2)
    
    actions = ActionBuilder(driver)
    # move_to_location: 手指懸空移到螢幕絕對座標 (x, y)
    # pointer_down / pointer_up: 最底層的「壓下」與「抬起」指令
    # pause: 必備指令，用於控制長按時間或動作間的間隔
    actions.pointer_action.move_to_location(x, y).pointer_down().pause(0.1).pointer_up()
    actions.perform()
    print("1-4. [底層類] move_to_location, pointer_down, pointer_up, pause 完成")

    # --- 5. Click (語意化高級方法) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # click: 封裝好的方法，會自動算中心點並執行完整的一按一放
    actions.pointer_action.click(phone_ele)
    actions.perform()
    print("5. [語意類] click 完成")

    # --- 6. Double Click (手動模擬版) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # 【避雷針 2：Double Click 邏輯衝突】
    # 原生 double_click 若中間沒 pause，在部分 Android 版本會判定為兩次 Down 衝突。
    # 手動用 pause(0.1) 隔開兩次點擊是最穩健的 W3C 寫法。
    actions.pointer_action.move_to(phone_ele).pointer_down().pointer_up().pause(0.1).pointer_down().pointer_up()
    actions.perform()
    print("6. [複合類] double_click 手動模擬完成")

    # --- 7. Context Click (長按選單) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # context_click: 模擬滑鼠右鍵。在 Android 系統中，這通常被對應為「觸發長按選單」。
    actions.pointer_action.context_click(phone_ele)
    actions.perform()
    print("7. [特殊類] context_click 完成")

    # --- 8-11. 連鎖手勢組 (按住、偏移、釋放) ---
    phone_ele = reset_and_find()
    actions = ActionBuilder(driver)
    # move_to: 移到元素的中心點 (不用再手動算 x, y)
    # click_and_hold: 按住後不放手，手指狀態維持在 Pressed
    # move_by: 重要！這是「相對偏移」(你提到的 mover_by)，從目前位置往右移 100 像素
    # release: 這是按住後的必備動作，將手指從螢幕抬起
    actions.pointer_action.move_to(phone_ele).click_and_hold().move_by(100, 0).release()
    actions.perform()
    print("8-11. [連鎖類] move_to, click_and_hold, move_by, release 完成")

except Exception as e:
    print(f"執行出錯: {e}")

finally:
    driver.quit()