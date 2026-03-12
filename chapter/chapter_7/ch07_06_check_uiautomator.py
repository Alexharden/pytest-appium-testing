from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #是否可被選擇
# new UiSelector.className("android.widget.TextView").checked(True)
# #是否可被點擊
# new UiSelector.className("android.widget.TextView").clickable(True)
# #是否可用
# new UiSelector.className("android.widget.TextView").enabled(True)
# #是否可被聚焦
# new UiSelector.className("android.widget.TextView").focused(True)
# #是否可被長按
# new UiSelector.className("android.widget.TextView").longClickable(True)
# #是否可被滾動
# new UiSelector.className("android.widget.TextView").scrollable(True)
# #是否被選中
# new UiSelector.className("android.widget.TextView").selected(True)


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "noReset": True,
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# --- 核心練習：使用 UIAutomator 狀態篩選器 ---

# 1. 定位「可以被點擊」且「文字包含 Chrome」的元素
# 這能確保你不會點到一個長得像 Chrome 但實際上不給點的裝飾圖示
clickable_chrome = 'new UiSelector().className("android.widget.TextView").textContains("Chrome").clickable(true)'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, clickable_chrome).click()
print(f"可以被點擊{clickable_chrome}")
print("✅ 成功點擊一個「可點擊」的 Chrome")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. 定位「目前可用 (Enabled)」的訊息圖示
# 如果 App 正在更新或被停用，enabled(false) 就會過濾掉它
enabled_msg = 'new UiSelector().text("Messages").enabled(true)'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, enabled_msg).click()
print(f"可用{enabled_msg}")
print("✅ 成功點擊一個「可用」的 Messages")
sleep(2)
driver.terminate_app("com.google.android.apps.messaging")

# 3. 定位「可被滾動」的容器 (常用於長頁面)
# 當你要執行滑動操作前，可以先確認容器是否支援滾動
is_scrollable = "new UiSelector().scrollable(true).instance(0)"
try:
    scroll_view = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, is_scrollable)
    print(f"可被滾動{is_scrollable}")
    print("✅ 找到畫面上第一個可滾動的容器")
except:
    print(f"可被滾動{is_scrollable}")
    print("❌ 畫面上目前沒有可滾動的元素")

# --- 結束連線 ---
driver.quit()
