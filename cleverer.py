import time
import os
import random

from cleverwrap import CleverWrap
cw = CleverWrap("")
conv = cw.new_conversation()


from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
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



#Main loop
while True:

    mynumber2 = random.randint(5, 75)
    ##Images
    path2 = "/home/selenium/mokou/"
    random_filename2 = random.choice([
        x for x in os.listdir(path2)
        if os.path.isfile(os.path.join(path2, x))
    ])

    myrandomfile2 = (path2 + random_filename2)

    mynumber = random.randint(5, 75)
    ##Images
    path = "/home/selenium/LastExile/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    myrandomfile = (path + random_filename)


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

    my_cleverresponse =cw.say(mystfulinestripped)

    print(my_cleverresponse)
    ##Fuuka functionality

    driver = webdriver.Firefox(options=options)

    driver.get("http://www.tokyochronos.net/cute/thread/2579/")

    replybox = driver.find_element_by_id("reply_chennodiscursus")
    replybox.send_keys(my_cleverresponse)

    replyboxN = driver.find_element_by_id("reply_bokunonome")
    replyboxN.send_keys("Arc#0")

    replyboxFile = driver.find_element_by_id("file_image")
    replyboxFile.send_keys(myrandomfile)

    element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
    time.sleep(4)
    print("Sleeping", mynumber, "...")

    ##Run 2
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
    time.sleep(4)
    print("Sleeping",mynumber,"...")

    my_humanresponse = print(mystfulinestripped)

    my_cleverresponse = cw.say(mystfulinestripped)

    print(my_cleverresponse)
    ##Fuuka functionality

    driver = webdriver.Firefox(options=options)

    driver.get("http://www.tokyochronos.net/cute/thread/2579/")

    replybox = driver.find_element_by_id("reply_chennodiscursus")
    replybox.send_keys(my_cleverresponse)

    replyboxN = driver.find_element_by_id("reply_bokunonome")
    replyboxN.send_keys("grayhate#boobz")

    replyboxFile = driver.find_element_by_id("file_image")
    replyboxFile.send_keys(myrandomfile2)

    element = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
    time.sleep(12)
    print("Sleeping",12,"...")
    driver.close()
