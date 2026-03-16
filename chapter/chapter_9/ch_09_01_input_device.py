from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 匯入 W3C Actions 相關組件 (修正後的 Selenium 4.x 路徑)
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction

# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:noReset": True
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

wait = WebDriverWait(driver, 10)

try:
    # 2. 找到目標元素並計算座標
    # 我們以 Phone 圖示為練習對象
    phone_xpath = '//android.widget.TextView[@content-desc="Phone"]'
    phone_ele = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, phone_xpath)))

    # 獲取元素矩形區域並計算中心點 (需轉為 int)
    rect = phone_ele.rect
    center_x = int(rect['x'] + rect['width'] / 2)
    center_y = int(rect['y'] + rect['height'] / 2)

    # 3. 配置 Input Device (手指)
    actions = ActionBuilder(driver)
    
    # 標準 W3C 做法：透過 add_pointer_input 註冊一個設備名為 'finger1'
    # 這就是你課本提到的 Input Device 宣告
    finger = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger1")

    # 【備註：被註解的簡寫法】
    # actions = ActionBuilder(driver, mouse=finger)
    # 理由：在學習 Input Device 核心概念時，手動註冊設備 (add_pointer_input) 
    # 才能展現「新增一個輸入源」的標準邏輯，這對未來「多指操作」非常重要。

    # 4. 描述動作流程 (這就是 add_action 的過程)
    # 我們透過 actions.pointer_action 這個代理人來操作剛才定義的 finger 設備
    
    # 動作 A: 移動手指到目標上方
    actions.pointer_action.move_to_location(center_x, center_y)
    
    # 動作 B: 手指壓下螢幕
    actions.pointer_action.pointer_down()
    
    # 動作 C: 停頓 2 秒 (模擬長按效果)
    actions.pointer_action.pause(2.0)
    
    # 動作 D: 手指抬起離開螢幕
    actions.pointer_action.pointer_up()

    # 5. 執行 (Perform)
    # 此時所有剛才 add 進去的 action 會一次打包送出執行
    actions.perform()
    print(f"成功透過 W3C Actions 點擊座標: ({center_x}, {center_y})")

    # 6. 清理 (Clear Action)
    # 確保 Builder 緩存被清空，防止下一個動作序列發生重複執行的靈異現象
    actions.clear_actions()
    print("動作已透過 clear_actions 清空，狀態重置完成")

except Exception as e:
    print(f"程式執行發生錯誤: {e}")

finally:
    # 結束後關閉 Session
    sleep(2)
    driver.quit()