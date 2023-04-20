from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#additional imports here

def handler(context=None, event=None):
    driver = init_browser()
    
    #rest of web scraping code goes here

def init_browser():
    #Those options are all needed to run in lambda
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
    
    chrome_options.binary_location = '/opt/chrome/chrome'
    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=chrome_options)
    
    driver.set_window_size(1120, 850)
    
    return driver

if __name__ == '__main__':
    handler()