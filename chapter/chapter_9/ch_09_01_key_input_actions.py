from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 匯入 W3C Actions 鍵盤相關組件
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.key_input import KeyInput
from selenium.webdriver.common.keys import Keys

# 1. 連線機制設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True  # 保持 App 登入狀態，不清除資料
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    # 2. 前置導覽：進入搜尋介面 (使用簡單點擊)
    print("正在開啟 Messages 並進入搜尋框...")
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Messages"]'))).click()
    
    # 點擊主畫面的搜尋列 ID
    search_bar = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.google.android.apps.messaging:id/open_search_bar_text_view')))
    search_bar.click()
    
    # 等待軟體鍵盤彈出 (這很重要，否則 Focus 可能會漏掉)
    sleep(1.5)

    # 3. 核心練習：建立 W3C Actions 鍵盤動作序列
    actions = ActionBuilder(driver)
    
    # 【add_key_input】: 宣告一個鍵盤類型的 Input Device
    keyboard = actions.add_key_input("my_keyboard")

    print("開始執行 Key Input 動作序列...")

    # --- 模擬輸入 'Hi' (含大寫組合與停頓) ---

    # [create_key_down]: 模擬按下 Shift 鍵不放
    keyboard.create_key_down(Keys.SHIFT)
    
    # [create_key_down/up]: 按下並放開 'h' (此時會輸出大寫 H)
    keyboard.create_key_down('h')
    keyboard.create_key_up('h')
    
    # [create_key_up]: 釋放 Shift 鍵，回到小寫模式
    keyboard.create_key_up(Keys.SHIFT)

    # [create_pause]: 在字母之間加入 0.5 秒的停頓 (模擬打字間隔)
    keyboard.create_pause(0.5)

    # [create_key_down/up]: 輸入小寫 'i'
    keyboard.create_key_down('i')
    keyboard.create_key_up('i')

    # [create_pause]: 停頓一下後按下 Enter
    keyboard.create_pause(0.5)
    keyboard.create_key_down(Keys.ENTER)
    keyboard.create_key_up(Keys.ENTER)

    # 4. 執行與編碼 (Perform 會自動觸發底層的 encode 過程)
    # 將上述步驟編碼成 W3C 標準 JSON 格式並發送給 Server
    actions.perform()
    
    # [clear_actions]: 必須清理，否則下次 Actions 會保留這次的按鍵狀態
    actions.clear_actions()
    print("動作執行成功：已輸入 'Hi' 並按下 Enter")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    sleep(2)
    driver.quit()