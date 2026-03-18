from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


def perform_smooth_pinch(driver, start_p1, start_p2, end_p1, end_p2, steps=50, step_ms=30):
    """
    核心工具：執行極致平滑的雙指動作
    steps: 拆解步數，越多越平滑
    step_ms: 每一步的時間間隔
    """
    actions = ActionBuilder(driver)
    actions.devices = []  # 舊寫法保留參考：actions.w3c_actions.devices = []

    f1 = actions.add_pointer_input(POINTER_TOUCH, "finger1")
    f2 = actions.add_pointer_input(POINTER_TOUCH, "finger2")

    # 1. 移動到起點 (duration=0 代表瞬間出現在該點)
    f1.create_pointer_move(duration=0, x=int(start_p1[0]), y=int(start_p1[1]))
    f2.create_pointer_move(duration=0, x=int(start_p2[0]), y=int(start_p2[1]))

    # 2. 按下手指 (必須指定 button)
    f1.create_pointer_down(button=MouseButton.LEFT)
    f2.create_pointer_down(button=MouseButton.LEFT)

    # 3. 重要：停頓 0.6 秒，確保 Android 系統鎖定雙指壓力點
    f1.create_pause(0.6)
    f2.create_pause(0.6)

    # 4. 核心插值移動：將長位移拆解成 50 個微小 move
    for i in range(1, steps + 1):
        curr_x1 = start_p1[0] + (end_p1[0] - start_p1[0]) * i / steps
        curr_y1 = start_p1[1] + (end_p1[1] - start_p1[1]) * i / steps
        curr_x2 = start_p2[0] + (end_p2[0] - start_p2[0]) * i / steps
        curr_y2 = start_p2[1] + (end_p2[1] - start_p2[1]) * i / steps

        f1.create_pointer_move(duration=step_ms, x=int(curr_x1), y=int(curr_y1))
        f2.create_pointer_move(duration=step_ms, x=int(curr_x2), y=int(curr_y2))

    # 5. 抬起手指
    f1.create_pointer_up(button=MouseButton.LEFT)
    f2.create_pointer_up(button=MouseButton.LEFT)

    # 執行指令並 encode (編碼為 W3C JSON)
    actions.perform()
    actions.clear_actions()


try:
    # --- 步驟一：導航到目標圖片 ---
    print("正在開啟 Photos 並進入全螢幕圖片...")
    photo_app = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Photos"]'))
    )
    photo_app.click()

    first_pic = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Photo taken")]')
        )
    )
    first_pic.click()
    sleep(2)  # 等待圖片展開動畫

    # --- 步驟二：計算座標參數 ---
    size = driver.get_window_size()
    cx, cy = size["width"] // 2, size["height"] // 2

    # 併攏位 (兩指間距約 40 像素)
    p_center1, p_center2 = (cx, cy - 20), (cx, cy + 20)
    # 張開位 (兩指撥開到螢幕 1/4 高度)
    offset = size["height"] // 4
    p_expanded1, p_expanded2 = (cx, cy - offset), (cx, cy + offset)

    # --- 步驟三：執行慢慢【放大】 ---
    print("1. 正在執行慢慢【放大】 (Zoom Out)...")
    perform_smooth_pinch(driver, p_center1, p_center2, p_expanded1, p_expanded2)
    sleep(1.5)

    # --- 步驟四：執行慢慢【縮小】 ---
    print("2. 正在執行慢慢【縮小】 (Pinch In)...")
    # 將放大時的起點與終點對調即可
    perform_smooth_pinch(driver, p_expanded1, p_expanded2, p_center1, p_center2)

    print("任務圓滿完成：已實現平滑縮放來回！")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    sleep(2)
    driver.quit()
