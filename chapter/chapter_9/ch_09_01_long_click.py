from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionBuilder, ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
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
# driver.implicitly_wait(10)

# driver.find_element(AppiumBy.ID, 'comd.dangdang.buy2:id/tab_personal_iv').click()
# sleep(2)
# #獲取視窗大小
# size_dict = driver.get_window_size()
# actions = ActionBuilder(driver)
# #輸入源設備列為空
# actions.w3c_actions.devices = []
# # === 手指長按 ===
# #添加一個新的輸入源到設備列表中，輸入源類行為 Touuch, id 為finger0
# new_input = actions.w3c_actions.add_pointer_input('touch', 'finger0')
# #輸入源的動作：移動到某個點，這裡使用相對位子，x軸的居中位子，y軸的0.3位子
# new_input.move_to_location(x = size_dict['width'] * 0.5, y = size_dict['height'] * 0.3)
# #按住鼠標左鍵
# new_input.create_pointer_down(MouseButton.LEFT)
# #停頓2秒
# new_input.create_pause(2)
# #釋放鼠標左鍵
# new_input.create_pointer_up(MouseButton.LEFT)
# #執行
# actions.perform()
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
    # 2. 定位 Phone 圖示
    phone_ele = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Phone"]'))
    )
    rect = phone_ele.rect
    center_x = rect["x"] + rect["width"] // 2
    center_y = rect["y"] + rect["height"] // 2

    # --- 練習 A：底層長按 (Pointer Input) ---
    actions = ActionBuilder(driver)

    # 【舊寫法保留】：actions.w3c_actions.devices = []
    actions.devices = []

    # 【舊寫法保留】：finger = actions.w3c_actions.add_pointer_input('touch', 'finger0')
    finger = actions.add_pointer_input(POINTER_TOUCH, "finger0")

    # 核心物理動作序列
    # 1. 移動手指到指定位置
    finger.create_pointer_move(duration=0, x=center_x, y=center_y)

    # 2. 【修正點】：使用 button= 指定參數，避免位置參數數量錯誤
    # 在 touch 設備中，button=0 或 MouseButton.LEFT 都代表手指壓下
    finger.create_pointer_down(button=MouseButton.LEFT)

    # 3. 停頓時間 (長按 2 秒)
    finger.create_pause(2)

    # 4. 抬起手指 (同樣建議指定 button)
    finger.create_pointer_up(button=MouseButton.LEFT)

    # perform() 執行時會內部自動執行 encode 過程
    actions.perform()
    actions.clear_actions()
    print("A. 執行底層 Pointer 長按完成")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    sleep(2)
    driver.quit()
