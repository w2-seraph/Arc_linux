import requests
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import sys
import random
import os
import time

options = FirefoxOptions()
options.add_argument("-headless")

##Proxy settings
PROXY = "p.webshare.io:19999"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}


while True:
    url = "http://dratomic.com/js/sg/sg_ko.php"
    response = requests.request("GET", url)
    
    original_stdout = sys.stdout
    
    with open('quickbrwnfoOx.txt', 'w') as f:
        sys.stdout = f
        print(response.text)
        sys.stdout = original_stdout
    
    quickbrownresponse = response.text
    
    ##Images
    path = "/root/home/selenium/qbf/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    
    myrandomfile = (path + random_filename)
    
    driver = webdriver.Firefox(options=options)
    
    driver.get("http://www.tokyochronos.net/cute/thread/2579/")
    
    replybox = driver.find_element_by_id("reply_chennodiscursus")
    replybox.send_keys(quickbrownresponse)
    
    replyboxN = driver.find_element_by_id("reply_bokunonome")
    replyboxN.send_keys("Norik")
    
    replyboxFile = driver.find_element_by_id("file_image")
    replyboxFile.send_keys(myrandomfile)
    
    element = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
    time.sleep(120)
    print("Sleeping", 12, "...")
    driver.close()
