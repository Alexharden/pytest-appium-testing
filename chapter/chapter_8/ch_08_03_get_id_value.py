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
    # 1. 先點擊電話圖示進入首頁
    print("正在尋找 Phone 圖示...")
    phone_icon = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Phone")))
    phone_icon.click()
    print("已點擊 Phone，等待搜尋框出現...")

    # --- 核心測試區塊 ---
    
    # 2. 使用更新後的正確 ID 定位搜尋框 (根據你的截圖)
    search_id = "com.google.android.dialer:id/open_search_bar_text_view"
    
    # 使用智能等待直到元素出現在畫面上，並存入變數
    ele_by_id = wait.until(EC.presence_of_element_located((AppiumBy.ID, search_id)))

    # 3. 使用更新後的正確 XPath 定位搜尋框 (注意已經改成 TextView)
    search_xpath = '//android.widget.TextView[@resource-id="com.google.android.dialer:id/open_search_bar_text_view"]'
    
    # 因為上面已經確認元素存在了，這裡直接用 find_element 抓取並存入另一個變數
    ele_by_xpath = driver.find_element(AppiumBy.XPATH, search_xpath)

    # 4. 使用 .format() 印出兩者的內部 id 值
    print("\nID 定位的內部元素值: {}".format(ele_by_id.id))
    print("XPath 定位的內部元素值: {}".format(ele_by_xpath.id))

    # 5. 比較這兩個定位方式是不是真的抓到同一個元素
    if ele_by_id.id == ele_by_xpath.id:
        print("✅ 測試通過：兩個元素的 id 完全一致，是同一個元素！")
    else:
        print("❌ 測試失敗：兩個元素的 id 不一致，抓到不同的東西了。")

    # 💡 加碼技巧：在 Appium 中，其實你也可以直接比較兩個「元素物件」本身
    if ele_by_id == ele_by_xpath:
        print("✅ 元素物件直接比較：也是同一個！")

except Exception as e:
    print("\n❌ 發生錯誤：")
    print(f"錯誤類型: {e.__class__.__name__}")
    print(f"錯誤訊息: {e}")

finally:
    driver.press_keycode(3)
    sleep(2)
    driver.quit()