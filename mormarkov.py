import markovify
import time
import random
import os
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

#Get raw text as string.
#Image file input

path = r"/root/home/selenium/Mordin/"

#Proxy settings
PROXY = "p.webshare.io:19999"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}



#Fuuka functionality
while True:
        # Get raw text as string.
        lines = open('mordin.csv').read().splitlines()
        myline = random.choice(lines)
        

        ##Filename
        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])
        myrandomfile = (path + random_filename)

        ##Timer
        mynumber=random.randint(90,180)
        print("Waiting ",mynumber)
        time.sleep(mynumber)
        driver = webdriver.Firefox(options=options)
        driver.get("http://www.tokyochronos.net/cute/thread/2579/")
        
        replybox = driver.find_element_by_id("reply_chennodiscursus")
        replybox.send_keys(myline)
        
        
        replyboxN = driver.find_element_by_id("reply_bokunonome")
        replyboxN.send_keys("Mordor#9")

        replyboxFile = driver.find_element_by_id("file_image")
        replyboxFile.send_keys(myrandomfile)

        element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
        time.sleep(8)
        driver.close()
