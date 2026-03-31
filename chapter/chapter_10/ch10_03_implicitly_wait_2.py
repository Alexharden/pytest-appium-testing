import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 1. 環境設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
    "appium:appPackage": "com.android.chrome",
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    # 設定隱性等待 10 秒
    driver.implicitly_wait(10)
    print(">>> [設定] 已開啟全域隱性等待：10 秒")

    print(">>> [操作] 啟動 Chrome...")
    driver.activate_app("com.android.chrome")
    time.sleep(2)  # 給一點基礎緩衝

    # ------------------------------------------------------
    # 故意寫一個找不到的 ID
    # ------------------------------------------------------
    print(">>> [尋找] 正在尋找一個不存在的 ID: 'this_id_does_not_exist'...")
    print(">>> [觀察] 你會發現程式在這裡會『卡住』剛好 10 秒，這就是隱性等待在努力輪詢...")

    start_time = time.time()

    # 這行一定會失敗
    target = driver.find_element(AppiumBy.ID, "com.android.chrome:id/this_id_does_not_exist")

    # 如果真的找到了（不可能），就點擊
    target.click()

except Exception as e:
    end_time = time.time()
    duration = end_time - start_time
    print(f"\n❌ 果然找不到！程式總共掙扎了 {duration:.2f} 秒")
    print(f"❌ 錯誤訊息: {type(e).__name__}")  # 通常是 NoSuchElementException

finally:
    print("\n>>> [結束] 關閉 Session。")
    driver.quit()
