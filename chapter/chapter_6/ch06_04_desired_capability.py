# ##小米計算機
# # 定義空字典，用來存放預期能力
# desired_caps= {}
# #設置測試的平台是 Andriod
# desired_caps['platformName'] = 'Android'
# #設置設備的 IP 地址及窗口
# desired_caps['deviceName'] = '127.0.0.1:21503'
# #設置測試的 Android 系統的版本
# desired_caps['platformVersion'] = '7.1.2'
# #設置 APK 文件對應的包名
# desired_caps['appPackage'] = 'com.miui.calculartor'
# #啟動 Activity
# desired_caps['appActivity'] = 'com.miui.calculartor.cal.CalculatorActivity'

# #請勿重製應用程式狀態
# desired_caps['noReset'] = True

# #使用 Unicode 輸入法，以支持中文輸入
# desired_caps['unicodeKeyboard'] = True

# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:21503",
#     "platformVersion": "7.1.2",
#     "appPackage": "com.miui.calculartor",
#     "appActivity": "com.miui.calculartor.cal.CalculatorActivity",
#     "noReset": True,
#     "unicodeKeyboard": True
# }



##底下是 mac計算機
# 定義空字典，用來存放預期能力
desired_caps = {}

# 1. 設置測試平台為 mac
desired_caps['platformName'] = 'mac'

# 2. 設置自動化引擎為 Mac2 (這是跑 Mac 原生 App 必須的)
desired_caps['appium:automationName'] = 'Mac2'

# 3. 設置設備名稱 (在 Mac 上通常寫 'Mac' 或是 'PC' 即可)
desired_caps['deviceName'] = 'Mac'

# 4. 設置 Mac 計算機的 Bundle ID 
# 這是 Apple 官方計算機的身分證字號
desired_caps['appium:bundleId'] = 'com.apple.calculator'

# 5. 請勿重製應用程式狀態 (Mac 上的應用程式狀態通常會保留)
desired_caps['noReset'] = True

# --- 另一種寫法：直接定義完整的字典 ---

desired_caps = {
    "platformName": "mac",
    "appium:automationName": "Mac2",
    "deviceName": "Mac",
    "appium:bundleId": "com.apple.calculator",
    "noReset": True
}