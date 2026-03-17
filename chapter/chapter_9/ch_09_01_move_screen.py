from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton

# 1. 連線機制設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    # 2. 取得螢幕尺寸計算座標
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]

    # 定義滑動點
    left_x = width * 0.2  # 左側位置
    right_x = width * 0.8  # 右側位置
    center_y = height * 0.5  # 螢幕高度中心

    # 定義滑動速度 (1500毫秒 = 1.5秒，實現慢慢滑的視覺效果)
    slow_speed = 1500

    # --- 執行兩次來回序列 ---
    for i in range(2):
        print(f"正在執行第 {i+1} 次手指來回滑動...")

        # --- [第一次：手指往右滑 (起點左 -> 終點右)] ---
        actions = ActionBuilder(driver)
        actions.devices = []  # 舊寫法對照：actions.w3c_actions.devices = []
        finger = actions.add_pointer_input(POINTER_TOUCH, "finger0")

        # 動作序列：移到左邊 -> 按下 -> 慢速移向右邊 -> 抬起
        finger.create_pointer_move(duration=0, x=left_x, y=center_y)
        finger.create_pointer_down(button=MouseButton.LEFT)
        finger.create_pointer_move(duration=slow_speed, x=right_x, y=center_y)
        finger.create_pointer_up(button=MouseButton.LEFT)

        actions.perform()  # 此處執行時會自動進行指令 encode
        actions.clear_actions()
        print(f"  - 第 {i+1} 次：手指【往右滑】完成")
        sleep(1)

        # --- [第二次：手指往左滑 (起點右 -> 終點左)] ---
        actions = ActionBuilder(driver)
        actions.devices = []
        finger = actions.add_pointer_input(POINTER_TOUCH, "finger0")

        # 動作序列：移到右邊 -> 按下 -> 慢速移向左邊 -> 抬起
        finger.create_pointer_move(duration=0, x=right_x, y=center_y)
        finger.create_pointer_down(button=MouseButton.LEFT)
        finger.create_pointer_move(duration=slow_speed, x=left_x, y=center_y)
        finger.create_pointer_up(button=MouseButton.LEFT)

        actions.perform()
        actions.clear_actions()
        print(f"  - 第 {i+1} 次：手指【往左滑】完成")
        sleep(1)

    print("兩次慢慢的【手指來回滑動】任務達成！")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    sleep(2)
    driver.quit()
