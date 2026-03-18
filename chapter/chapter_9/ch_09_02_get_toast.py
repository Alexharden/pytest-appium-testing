import re
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 1. 連線機制設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:noReset": True,
    "appium:forceAppLaunch": True,
    "appium:shouldTerminateApp": True,  # 結束時自動嘗試終止
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    print("\n>>> [步驟 1] 強迫啟動 Settings...")
    driver.activate_app("com.android.settings")
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[contains(@text, 'Search') or @text='Settings']")))

    print(">>> [步驟 2] 滑動尋找 About 項目...")
    # 使用 setMaxSearchSwipes 確保滑到底部
    selector = 'new UiScrollable(new UiSelector().scrollable(true)).setMaxSearchSwipes(15).scrollIntoView(new UiSelector().textContains("About"))'
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)

    # 解決點錯位置：等待回彈動畫靜止並重新定位
    sleep(2)
    about_ele = driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'About')]")
    about_ele.click()
    print("✅ 成功點擊 About")

    print(">>> [步驟 3] 尋找 Build number...")
    build_selector = (
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Build number"))'
    )
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, build_selector)

    sleep(1.5)
    build_num_ele = driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'Build number')]")

    print("\n" + "=" * 60)
    print("      Toast 捕捉實驗報告 (完整 7 次)")
    print("=" * 60)

    for i in range(1, 8):
        build_num_ele.click()
        print(f"\n[第 {i} 次點擊]")

        # (A) XPath Class
        try:
            t_a = WebDriverWait(driver, 1.5, poll_frequency=0.05).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//*[@class='android.widget.Toast']"))
            )
            print(f" (A) Class定位: {t_a.text}")
        except:
            print(" (A) Class定位: 未捕捉")

        # (B) XPath Text
        try:
            t_b = driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'already') or contains(@text, 'step')]")
            print(f" (B) Text定位 : {t_b.text}")
        except:
            print(" (B) Text定位 : 未捕捉")

        # (C) Page Source + Regex (文字還原)
        source = driver.page_source
        match = re.search(r'android.widget.Toast.*?text="(.*?)"', source)
        if match:
            print(f" (C) 源碼提取 : {match.group(1)}")
        else:
            print(" (C) 源碼提取 : 未發現")

        sleep(0.4)

    print("\n" + "=" * 60)

except Exception as e:
    print(f"\n❌ 錯誤: {e}")

finally:
    # --- 這裡執行完整關閉 ---
    print("\n>>> [清理] 正在徹底關閉 Settings 並釋放資源...")
    try:
        # 強制停止 App
        driver.terminate_app("com.android.settings")
        print("✅ Settings 已從後台完全關閉")
    except:
        print("⚠️ 無法關閉 App 或 App 已處於關閉狀態")

    driver.quit()
