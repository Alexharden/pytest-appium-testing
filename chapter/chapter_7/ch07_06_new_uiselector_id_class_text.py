from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# ... (desired_caps 設定與之前相同)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 定義基礎屬性
MY_ID = "com.dangdang.buy2:id/tv_agile_user_name"
MY_CLASS = "android.widget.TextView"
MY_TEXT = "登入/註冊"

# --- 核心練習：UiSelector 屬性組合 ---

# 1. 第一組：ID + Class (適用於：知道 ID 但想確保它是特定的 UI 元件類型)
# 語法：new UiSelector().resourceId("ID").className("ClassName")
id_plus_class = f'new UiSelector().resourceId("{MY_ID}").className("{MY_CLASS}")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, id_plus_class).click()
print("✅ ID + Class 組合點擊成功")
sleep(2)


# 2. 第二組：ID + Text (適用於：ID 重複，需要靠文字內容來精確區分)
# 語法：new UiSelector().resourceId("ID").text("文字")
id_plus_text = f'new UiSelector().resourceId("{MY_ID}").text("{MY_TEXT}")'
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, id_plus_text).click()
print("✅ ID + Text 組合點擊成功")
sleep(2)


# --- 進階：三合一組合 (ID + Class + Text) ---
# 當畫面上有一堆長得很像的按鈕時，這招是終極必殺技
triple_combo = f'new UiSelector().resourceId("{MY_ID}").className("{MY_CLASS}").text("{MY_TEXT}")'
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, triple_combo).click()

# --- 結束連線 ---
print("🧹 測試結束")
driver.quit()
