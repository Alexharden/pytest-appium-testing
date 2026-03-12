from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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

# --- 核心練習：使用 index 與 instance 進行定位 ---

# 1. 使用 instance(n) 定位 Chrome
# 邏輯：找到全畫面上第 1 個 (索引 0) 類別為 TextView 且文字含 Chrome 的元素
# instance 非常適合用於全局搜尋
chrome_inst = 'new UiSelector().className("android.widget.TextView").textContains("Chrome").instance(0)'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, chrome_inst).click()
print("✅ 使用 instance(0) 成功點擊 Chrome")
sleep(2)
driver.terminate_app("com.android.chrome")

# 2. 使用 index(n) 定位 Messages
# 邏輯：在同一個父容器下，尋找 index 為 n 的元素
# 注意：index 受到 UI 層級影響較大，通常會搭配 parent 屬性
# 假設在 hotseat 區域，Messages 是該層級下的第 2 個元素 (index 1)
msg_index = 'new UiSelector().resourceId("com.google.android.apps.nexuslauncher:id/hotseat").childSelector(new UiSelector().index(1))'
# 如果不確定父層，單純用 index 容易點錯，建議像下面這樣寫：
# msg_index = 'new UiSelector().className("android.widget.TextView").text("Messages").index(1)'

try:
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, msg_index).click()
    print("✅ 使用 index 配合 childSelector 成功點擊 Messages")
except:
    # 如果 index 不對，改用保險的 instance
    msg_inst = 'new UiSelector().text("Messages").instance(0)'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, msg_inst).click()
    print("✅ Index 失敗，改用 instance(0) 點擊 Messages")

sleep(2)
driver.terminate_app("com.google.android.apps.messaging")

# 3. 使用 instance(n) 找出畫面上「所有」可滾動容器中的第一個
# 這是處理 ListView 或 ScrollView 最穩的方式
is_scrollable = "new UiSelector().scrollable(true).instance(0)"
try:
    scroll_view = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, is_scrollable)
    print("✅ 找到全畫面第一個可滾動實例 (instance 0)")
except:
    print("❌ 找不到可滾動實例")

# --- 結束連線 ---
driver.quit()
