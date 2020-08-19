import requests
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import sys
import json
import os
import random
import time

##Proxy settings on by default
PROXY = "p.webshare.io:19999"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

while True:
    ##Images
    path = "/root/home/selenium/Cirno/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    myrandomfile = (path + random_filename)

    ##Main
    options = FirefoxOptions()
    options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)

    driver.get("http://www.tokyochronos.net/cute/thread/2579/")

    ##Find last post in thread
    elements = driver.find_elements_by_xpath("//div[contains(@class, 'text')]")
    size = len(elements)
    target_element = elements[size - 1]
    ##Pokemon stuff

    mystfuline = (target_element.text)

    mystfulinestripped = (mystfuline).lstrip()
    driver.close()

    my_humanresponse = print(mystfulinestripped)

    r = requests.get(f'https://www.personalityforge.com/api/chat/?apiKey=XbNsywHwMMemhr0C&chatBotID=63906&message={my_humanresponse}&externalID=qwe-669669946&firstName=Arc&lastName=Hatewise&gender=m')

    myprintvar = print(r.json())

    myJson = str(r.content)

    original_stdout = sys.stdout


    #write PFbot response
    with open('tay_response.json', 'w') as f:
        sys.stdout = f
        print(r.text)
        sys.stdout = original_stdout

    with open('tay_response.json') as json_file:
       data = json.load(json_file)

    myTayresponse =  data['message']['message']

    print(myTayresponse)

    ##Fuuka functionality

    driver = webdriver.Firefox(options=options)

    driver.get("http://www.tokyochronos.net/cute/thread/2579/")

    replybox = driver.find_element_by_id("reply_chennodiscursus")
    replybox.send_keys(myTayresponse)

    replyboxN = driver.find_element_by_id("reply_bokunonome")
    replyboxN.send_keys("Hartjen#clingy")

    replyboxFile = driver.find_element_by_id("file_image")
    replyboxFile.send_keys(myrandomfile)

    element = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
    time.sleep(180)
    print("Sleeping", 22, "...")
    driver.close()
