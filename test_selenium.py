from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

op = Options()
# ヘッドレスモード（Linux上で動かすとき必ずこのモードにしておく）
op.add_argument('--headless') # ブラウザを出さない
op.add_argument('--disable-gpu')                      
op.add_argument('--disable-extensions')               
op.add_argument('--proxy-server="direct://"')         
op.add_argument('--proxy-bypass-list=*')              
op.add_argument('--blink-settings=imagesEnabled=false')
op.add_argument('--lang=ja')                          
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')
op.add_argument("--log-level=3")
op.add_argument('--ignore-certificate-errors')
op.add_argument('--ignore-ssl-errors')
op.add_argument("--window-size=1440,1080")
op.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('excludeSwitches', ['enable-logging'])
op.add_experimental_option('useAutomationExtension', False)
# op.add_experimental_option("detach", True) # ブラウザ出るモードの時処理終了後もブラウザを閉じない
op.page_load_strategy = 'eager'
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
# driver.get('https://example.com')
# print(driver.current_url)

# （A表）先月から過去1年間の当せん番号　のリンクを格納した配列を返す
def get_tableA_links():
    for i in range(0, 3):
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
        except Exception as e:
            print(e)
            time.sleep(5)
        else:
            break

    url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/numbers/backnumber/index.html'
    driver.get(url)

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "ナンバーズ3")))
    except Exception as e:
        time.sleep(10)

    lists = []
    links = driver.find_elements_by_partial_link_text('ナンバーズ3')
    for link in links:
        lists.append(link.get_attribute('href'))
        if len(lists) == 12:
            break 
    return lists


tableA_links = get_tableA_links()
print(tableA_links)