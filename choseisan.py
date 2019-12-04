import sys
from selenium import webdriver
import time
import datetime

SLEEP_TIME = 60

def choseisan(args):
    driver = run_chrome("https://chouseisan.com/")
    #タイトル入力
    is_title_input = input_by_id(driver, "name", args[1])
    #候補日入力
    kouho = get_date(int(args[2]), args[3])
    is_kouhobi_input = input_by_id(driver, "kouho", kouho)
    #出欠表を作るをクリック
    is_click_create = click_by_id(driver, "createBtn")
    #URL取得
    print(get_value_by_id(driver, "listUrl"))
    time.sleep(SLEEP_TIME)
    driver.close()

def run_chrome(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        return driver
    except Exception as e:
        print(e)
        return None


def input_by_id(driver, id, text):
    try:
        element = driver.find_element_by_id(id)
        element.send_keys(text)
        return True
    except Exception as e:
        print(e)
        return False

def click_by_id(driver, id):
    try:
        element = driver.find_element_by_id(id)
        element.click()
        return True
    except Exception as e:
        print(e)
        return False

def get_value_by_id(driver, id):
    try:
        element = driver.find_element_by_id(id)
        value = element.get_attribute("value")
        return value
    except Exception as e:
        print(e)
        return None

def get_date(num_date, str_time):
    list_day = ["月","火","水","木","金","土","日"]
    str_dates = ""
    today = datetime.date.today()
    for i in range(num_date):
        target_date = today + datetime.timedelta(days=i+1)
        day = target_date.weekday()
        #土日以外を出力
        if day < 5:
            str_dates += target_date.strftime('%m/%d')
            str_dates += "（" + list_day[day] + "）" + str_time + "\n"
    return str_dates


if __name__ == '__main__':
    args = sys.argv
   
    if len(args) < 4:
        print('引数が違います。\nusage: コマンド タイトル名 取得日数 "時間" \n i.e.) choseisan.py イベント名 20 "22:00～24:00"')
    else:
        choseisan(args)
        exit()