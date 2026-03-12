from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# #課本練習
# desired_caps = {
#     "deviceName": '127.0.0.1:21503',
#     "appPackage": "com.dangdan.buy2",
#     "appActivity": "dangdang.buy2.activity.ActivityMainTab",
#     "platformName": "Android",
#     "noReset": True #不重置，保留app的狀態
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #輸出當前包和activity
# my_id = 'com.dangdan.buy2:id/tab_personal_iv'
# #Android_UIAUTOMATOR text 值定位
# login_text = 'new UiSelector().resourceIdmatches(".+tv_agile_user_name")'
# driver.find_element(AppiumBy.ID,my_id).click()
# sleep(3)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,login_text).click()
# sleep(3)
# driver.quit()


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

# --- 核心練習：使用 textStartsWith 前綴比對 ---

# 1. 搜尋容器 (FrameLayout) - 使用「精確匹配」
# 語法：^開頭 $結尾
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceIdMatches("^com.google.android.apps.nexuslauncher:id/search_container_hotseat$")',
).click()
print("✅ 搜尋容器點擊成功")
sleep(1)
driver.press_keycode(3)
print("退回桌面了")

# 2. Google 圖示 (ImageView) - 使用「後綴匹配」
# 語法：.* 代表前方有任意字元，最後以 g_icon 結尾
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceIdMatches(".*g_icon$")').click()
print("✅ Google 圖示點擊成功")
sleep(1)
driver.press_keycode(3)
print("退回桌面了")

# 3. 語音搜尋 (ImageView) - 使用「包含匹配」
# 語法：.* 包圍關鍵字，代表中間只要出現 mic_icon 即可
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceIdMatches(".*mic_icon.*")').click()
print("✅ 語音搜尋點擊成功")
sleep(1)
driver.press_keycode(3)
print("退回桌面了")

# 4. Google Lens (ImageButton) - 使用「前綴匹配」
# 語法：^ 代表開頭，.* 代表後方可接任意字元
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceIdMatches("^com.google.android.apps.nexuslauncher:id/lens.*")',
).click()
print("✅ Google Lens 點擊成功")
driver.press_keycode(3)
print("退回桌面了")

# --- 結束連線 ---
driver.press_keycode(3)  # 回桌面
driver.quit()
