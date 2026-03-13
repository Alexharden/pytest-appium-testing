from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

desired_caps = {
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

# 設定智能等待，最長等 10 秒
wait = WebDriverWait(driver, 10)

try:
    # 1. 點擊電話圖示進入首頁
    print("正在尋找 Phone 圖示...")
    phone_icon = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Phone")))
    phone_icon.click()
    print("已點擊 Phone，等待搜尋框出現...\n")

    # 2. 定位搜尋框元素
    search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    search_ele = wait.until(EC.presence_of_element_located((AppiumBy.ID, search_id)))

    # ==========================================
    # 🌟 Appium 元素屬性與方法「終極大補帖」 
    # ==========================================
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃        🕵️‍♂️ 元素身家調查報告 (Element Info)      ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    # --- 第一區：基礎識別 (Basic Identity) ---
    print("\n【一、基礎識別】")
    print(f"🆔 .id             : {search_ele.id}  (Appium 內部隨機生成的唯一識別碼)")
    print(f"📝 .text           : {search_ele.text}  (元素上顯示的文字)")
    print(f"🏷️  .tag_name       : {search_ele.tag_name}  (元素的 UI 標籤類型)")

    # --- 第二區：座標與尺寸 (Geometry) ---
    print("\n【二、座標與尺寸】")
    print(f"📍 .location       : {search_ele.location}  (相對於頁面左上角的絕對座標)")
    print(f"👁️  .location_in_view: {search_ele.location_in_view}  (相對於目前可視範圍的座標)")
    print(f"📏 .size           : {search_ele.size}  (元素的寬度與高度)")
    print(f"📦 .rect           : {search_ele.rect}  (座標與尺寸的完美合體字典)")

    # --- 第三區：狀態檢查 (State Check) ---
    print("\n【三、狀態檢查】")
    print(f"👀 .is_displayed() : {search_ele.is_displayed()}  (肉眼是否能在畫面上看見它？)")
    print(f"👆 .is_enabled()   : {search_ele.is_enabled()}  (是否啟用且可以被操作？)")
    print(f"✅ .is_selected()  : {search_ele.is_selected()}  (是否處於被勾選/選定狀態？)")

    # --- 第四區：萬用瑞士刀 get_attribute() ---
    # 💡 只要是 Appium Inspector 裡 "Selected Element" 列表能看到的屬性，都能用這招抓！
    print("\n【四、進階屬性 (get_attribute)】")
    print(f"🪪 resource-id     : {search_ele.get_attribute('resource-id')}")
    print(f"📄 content-desc    : {search_ele.get_attribute('content-desc')}  (無障礙標籤，通常用來當作 Accessibility ID)")
    print(f"🖱️ clickable       : {search_ele.get_attribute('clickable')}  (這個元件本身是否允許被點擊？)")
    print(f"🔤 class           : {search_ele.get_attribute('class')}  (等同於 tag_name)")
    print(f"🔍 checked         : {search_ele.get_attribute('checked')}  (如果是 Switch 開關，這裡會顯示 true/false)")

    # --- 第五區：底層驅動機制 ---
    print("\n【五、底層驅動】")
    print(f"🤖 .parent         : {search_ele.parent}  (找出是哪個 WebDriver 實體抓到這個元素的)")
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

except Exception as e:
    print("\n❌ 發生錯誤：")
    print(f"錯誤類型: {e.__class__.__name__}")
    print(f"錯誤訊息: {e}")

finally:
    driver.press_keycode(3)
    sleep(2)
    driver.quit()