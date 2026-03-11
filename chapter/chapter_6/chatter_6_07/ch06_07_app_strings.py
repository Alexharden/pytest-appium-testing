from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

# 課本練習
# desired_caps = {
#     "deviceName": "127.0.0.1:21503", 
#     "platformName": "Android",
#     "appActivity": "com.miui.calculator.cal.CalculatorActivity",
#     "appPackage": "com.miui.calculator"
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# en_res = driver.app_strings("en", "/path/to/file")
# print("en strings is {}", format(en_res)) 
# zh_res = driver.app_strings("zh")
# print("zh strings is {}", format(zh_res))
# driver.quit()


# 1. 基礎連線設定
desired_caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14.0",
    "appium:appPackage": "com.viewsonic.testapk",
    "appium:appActivity": ".MainActivity", 
    "noReset": True
}

options = UiAutomator2Options().load_capabilities(desired_caps)

# 2. 建立連線
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("✅ App 已啟動，準備獲取字串資源...")
sleep(3)

# 3. 核心練習：獲取 App 字串資源 (app_strings)
# 注意：如果 App 內部沒有定義英文資源，en_res 可能會回傳預設字串
try:
    # 獲取英文資源
    en_res = driver.app_strings("en")
    print("英文資源字串 (en): {}".format(en_res))

    # 獲取中文資源 (如果 App 有支援)
    zh_res = driver.app_strings("zh")
    print("中文資源字串 (zh): {}".format(zh_res))

except Exception as e:
    print(f"❌ 無法獲取字串資源，可能該 APK 未定義 strings.xml。錯誤內容: {e}")

# 4. 結束連線
print("🧹 測試結束，關閉 Session")
driver.quit()