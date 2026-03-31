import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 1. 環境設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:appPackage": "com.android.chrome",
    "appium:noReset": True,
    "appium:adbExecTimeout": 60000,
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 15)

try:
    print("\n" + "=" * 60)
    print("      Native EC 終極百科 - 穩定執行版")
    print("=" * 60)

    driver.activate_app("com.android.chrome")

    # [Case 1] Locator 類：存在、可見、可點擊
    search_loc = (AppiumBy.XPATH, "//*[contains(@resource-id, 'search_box') or contains(@resource-id, 'url_bar')]")
    wait.until(EC.presence_of_element_located(search_loc))
    wait.until(EC.visibility_of_element_located(search_loc))
    btn = wait.until(EC.element_to_be_clickable(search_loc))
    btn.click()
    print("✅ 基礎 Locator 系列通過")

    # [Case 2] Object 類：Visibility (Object)
    # 先獲取真正輸入框的物件
    edit_loc = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    edit_obj = wait.until(EC.visibility_of_element_located(edit_loc))

    # 這裡傳入的是 Object，不是 Locator
    wait.until(EC.visibility_of(edit_obj))
    print("✅ visibility_of (Object) 通過")

    # [Case 3] 內容驗證
    edit_obj.send_keys("Victory")
    wait.until(EC.text_to_be_present_in_element(edit_loc, "Victory"))
    print("✅ text_to_be_present 通過")

    # [Case 4] Invisibility (消失)
    del_btn_loc = (AppiumBy.ID, "com.android.chrome:id/delete_button")
    driver.find_element(*del_btn_loc).click()
    # 等待按鈕消失
    wait.until(EC.invisibility_of_element_located(del_btn_loc))
    print("✅ invisibility 通過")

    # [Case 5] Staleness (失效) - 關鍵修正！
    print(">>> 執行: staleness_of (強迫 App 釋放資源)")
    # 單純 back() 可能不夠，我們直接切換到「設定」App 確保 Chrome 的 UI 樹被銷毀
    driver.activate_app("com.android.settings")

    # 再次檢查那個「舊的」edit_obj，它現在應該保證是 Stale 了
    wait.until(EC.staleness_of(edit_obj))
    print("✅ staleness_of (Object) 終於通過！")

    print("\n" + "=" * 60)
    print("🎉 恭喜！原生 EC 全滿貫，連最難的 Staleness 都解決了！")
    print("=" * 60)

except Exception as e:
    print(f"\n❌ 失敗位置：{e}")

finally:
    driver.quit()
