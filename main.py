from time import sleep
from selenium import webdriver

PROXY = '91.214.31.234:8080'


# Firefox Proxy
def firefox_proxy():
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }
    driver = webdriver.Firefox()
    driver.get("https://www.icanhazip.com")
    sleep(5)
    driver.quit()


# Method 1 for Chrome Proxy
def chrome_proxy_1():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.icanhazip.com")
    sleep(5)
    driver.quit()


# Method 2 for Chrome Proxy
def chrome_proxy_2():
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }
    driver = webdriver.Chrome()
    driver.get("https://www.icanhazip.com")
    sleep(5)
    driver.quit()


if __name__ == '__main__':
    firefox_proxy()
    chrome_proxy_1()
    chrome_proxy_2()
