# PythonでSeleniumのwebdriverモジュールをインポート
from selenium import webdriver
# Selectタグを操作できるモジュール
from selenium.webdriver.support.ui import Select

"""
ここから「# Passwordを入力」までは
VBAのLogIn()関数が該当
"""

# 1.操作するブラウザを開く
# /Users/sakur/Desktop/selenium/chromedriver
driver = webdriver.Chrome()

# 2.操作するページを開く
# ネットで顧問のトップページ
driver.get('https://www1.shalom-house.jp/komon/login.aspx')

# IDを入力
driver.find_element_by_id('txtID').send_keys('B0622801')

# Passwordを入力
driver.find_element_by_id('txtPsw').send_keys('272dec')

# フォーム内容を送信する
driver.find_element_by_id('btnLogin').click()

# メイン画面へ移動
driver.find_element_by_id('ctl00_ContentPlaceHolder1_imgBtnSyuugyou').click()


"""
ここから「# 表示ボタンをクリックする」までは
VBAのTopToAttendanceInfo()関数が該当
"""

# 上長メニューへ移動
driver.find_element_by_id('ctl00_ContentPlaceHolder1_main_ibtnSu').click()

# 勤務情報入力をクリック
driver.find_element_by_id('ctl00_ContentPlaceHolder1_superior_lnkWorkEdit').click()

# プルダウンから対象年月を選択
Select(driver.find_element_by_id('dYYYYMM')).select_by_value('201907')

# 従業員検索をクリック
driver.find_element_by_css_selector('input[value="従業員検索"]').click()

# 表示ボタンをクリックする
driver.find_element_by_css_selector('input[type="button"]').click()


"""
ここからは
VBAのAttendanceInput()関数が該当
"""

# 7月1日の日付を表示
driver.find_element_by_css_selector('input[value="7月1日"]').click()

# 勤怠情報を入力
driver.find_element_by_id("inSTHOUR").send_keys('09') 
driver.find_element_by_id("inSTMINU").send_keys('00')
driver.find_element_by_id("inEDHOUR").send_keys('18')   
driver.find_element_by_id("inEDMINU").send_keys('00')
driver.find_element_by_id("inKKHOUR").send_keys('01')
driver.find_element_by_id("inKKMINU").send_keys('00')

# 入力した休憩時間で再計算をクリック
driver.find_element_by_css_selector('input[value="入力した休憩時間で再計算"]').click()

# 更新をクリック
driver.find_element_by_css_selector('input[value="更新"]').click()
