from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本重點
# # 1. 父子關係定位
# self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("ab).childSelector(text("xyz"))')
# # 2. 兄弟關係定位
# self.driver.find_element_by_android_uiautomator('new UiSelector().text("ab").fromParent(text("xyz"))')


# 延伸練習
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

# --- 核心練習：UIAutomator 關係定位 (childSelector & fromParent) ---

# 1. 父子關係定位 (childSelector)
# 邏輯：先找到 ID 為 hotseat 的容器，再從其子元素中搜尋文字為 "Chrome" 的項目
# 課本格式：new UiSelector().resourceId("父ID").childSelector(text("子文字"))
parent_id = "com.google.android.apps.nexuslauncher:id/hotseat"
chrome_selector = f'new UiSelector().resourceId("{parent_id}").childSelector(new UiSelector().text("Chrome"))'

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, chrome_selector).click()
print("✅ UIAutomator childSelector 點擊成功 (Chrome)")
sleep(2)
driver.terminate_app("com.android.chrome")
sleep(1)


# 2. 兄弟關係定位 (fromParent)
# 邏輯：先定位到 "Phone"，然後在「同一個父層」下搜尋文字為 "Messages" 的兄弟
# 課本格式：new UiSelector().text("基準文字").fromParent(text("目標文字"))
# 注意：UIAutomator 會在同一個 Parent 下橫向搜尋
msg_selector = 'new UiSelector().text("Phone").fromParent(new UiSelector().text("Messages"))'

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, msg_selector).click()
print("✅ UIAutomator fromParent 點擊成功 (Messages)")
sleep(2)
driver.terminate_app("com.google.android.apps.messaging")
sleep(1)


# --- 結束連線 ---
print("🧹 測試結束，關閉 Session")
driver.quit()


# # 1. 基礎連線設定
# desired_caps = {
#     "platformName": "Android",
#     "appium:automationName": "UiAutomator2",
#     "appium:deviceName": "emulator-5554",
#     "appium:platformVersion": "14.0",
#     "noReset": True
# }

# options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# # --- 核心練習：XPath 關係定位 (基於截圖層級) ---

# # 1. 父子關係 (從 hotseat 容器往下找 Chrome)
# # 結構：找到指定的 ViewGroup 後，找其內部的特定 TextView
# parent_child_chrome = '//android.view.ViewGroup[@resource-id="com.google.android.apps.nexuslauncher:id/hotseat"]/android.view.ViewGroup/android.widget.TextView[@text="Chrome"]'
# driver.find_element(AppiumBy.XPATH, parent_child_chrome).click()
# print("✅ XPath 父子關係點擊成功 (Chrome)")
# sleep(2)
# driver.terminate_app("com.android.chrome")
# sleep(1)

# # 2. 兄弟關係 (從 Phone 找後面的第一個兄弟 Messages)
# # 結構：找到 Phone 後，使用 following-sibling 軸定位
# # [1] 代表該層級下的第一個符合條件的兄弟
# sibling_messages = '//android.widget.TextView[@text="Phone"]/following-sibling::android.widget.TextView[1]'
# driver.find_element(AppiumBy.XPATH, sibling_messages).click()
# print("✅ XPath 兄弟關係點擊成功 (Messages)")
# sleep(2)
# driver.terminate_app("com.google.android.apps.messaging") # 修正 Messages 包名
# sleep(1)

# # 3. 回溯父層再找子層 (從 Chrome 回到父親再點擊 YouTube)
# # 結構：/.. 代表爬回上一層，再往下搜尋 YouTube
# back_to_parent_yt = '//android.widget.TextView[@text="Chrome"]/..//android.widget.TextView[contains(@text, "YouTube")]'
# driver.find_element(AppiumBy.XPATH, back_to_parent_yt).click()
# print("✅ XPath 回溯父層點擊成功 (YouTube)")
# sleep(2)
# driver.terminate_app("com.google.android.youtube")
# sleep(1)

# # 4. 索引定位 (在同一層 ViewGroup 內的第 3 個元素)
# # 根據截圖，Phone(1), Messages(2), Chrome(3)
# index_chrome = '(//android.view.ViewGroup[@resource-id="com.google.android.apps.nexuslauncher:id/hotseat"]//android.widget.TextView)[3]'
# driver.find_element(AppiumBy.XPATH, index_chrome).click()
# print("✅ XPath 索引定位點擊成功 (Chrome)")
# sleep(2)
# driver.terminate_app("com.android.chrome")

# # --- 結束連線 ---
# print("🧹 測試結束，關閉 Session")
# driver.quit()
