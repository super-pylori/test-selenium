from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
driver.get('https://example.com')
print(driver.current_url)