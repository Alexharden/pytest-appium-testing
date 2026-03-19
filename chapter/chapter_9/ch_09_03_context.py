from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#appium 事前設置
# appium --allow-insecure '*:chromedriver_autodownload'

# 1. 修改連線設定：拿掉可能導致衝突的 appActivity，改用手動啟動
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
    "appium:chromedriver_autodownload": True,
    "appium:adbExecTimeout": 60000,
    # 只指定 package，不寫死 Activity 讓系統自己選最適合的
    "appium:appPackage": "com.android.chrome" 
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print("\n" + "="*50)
    print("      Chrome Hybrid Context 穩定版實驗")
    print("="*50)

    # --- 關鍵修正：確保 Chrome 被開啟 ---
    print(">>> [操作] 強制喚醒 Chrome App...")
    driver.activate_app("com.android.chrome")
    
    # 給它一點時間過場動畫
    time.sleep(5) 

    # --- 方法 1: 循環獲取上下文 (driver.contexts) ---
    # 這是重點：WebView 不會立刻出現，必須輪詢（Polling）
    webview_context = None
    print(">>> [探測] 正在搜尋 WEBVIEW 上下文...")
    
    for i in range(10): # 最多等 10 次 (20秒)
        all_contexts = driver.contexts
        print(f"    第 {i+1} 次偵測: {all_contexts}")
        
        for c in all_contexts:
            if 'WEBVIEW' in c or 'CHROMIUM' in c:
                webview_context = c
                break
        
        if webview_context:
            break
        time.sleep(2)

    # --- 方法 2: 顯示目前的狀態 ---
    print(f"\n[1. 所有上下文]: {driver.contexts}")
    print(f"[2. 當前上下文]: {driver.current_context}")

    # --- 方法 3: 執行切換 ---
    if webview_context:
        print(f"\n>>> [切換] 執行 switch_to.context('{webview_context}')")
        driver.switch_to.context(webview_context)
        
        print(f"    切換後成功！當前為: {driver.current_context}")
        
        # 真正執行一個 WebView 專屬動作：導覽網頁
        print(">>> [網頁] 前往 Google 並獲取標題...")
        driver.get("https://www.google.com")
        time.sleep(2) # 等網頁載入
        print(f"    當前網頁標題為: {driver.title}")

        # 切回原生
        driver.switch_to.context('NATIVE_APP')
        print(f">>> [切換] 已回到原生模式: {driver.current_context}")
    else:
        print("\n❌ 失敗：即使強制啟動也找不到 Web 上下文。")
        print("💡 檢查點：請確認模擬器的 Chrome 畫面是否停在『歡迎使用』？如果是，請手動點掉。")

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

finally:
    print(">>> 正在結束 Session...")
    driver.quit()