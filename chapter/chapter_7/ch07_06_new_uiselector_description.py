ele_desp = 'new Uiselector().description("Storm Sprite)'
eles = driver.find_element_by_android_uiautomator(ele_desp)

# 開頭匹配定位
ele_desp = 'new Uiselector().descriptionStartsWith("Storm Sprite)'
eles = driver.find_element_by_android_uiautomator(ele_desp)

# 正則匹配
ele_desp = 'new Uiselector().descriptionMatches("^Storm.*$")'
eles = driver.find_element_by_android_uiautomator(ele_desp)
