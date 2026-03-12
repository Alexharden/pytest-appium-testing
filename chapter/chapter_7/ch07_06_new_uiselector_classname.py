from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# className 少數情況下會是頁面中的唯一值

# (1)className 完全匹配定位
'new UIselector().className("android.widget.TextView")'

# (2)className 正則匹配定位
'new UIselector().className(".*TextView")'

loc_class = 'new UIselector().className("android.widget.TextView")'
eles = driver.find_elemebnt_by_android_uiautomator(loc_class)
