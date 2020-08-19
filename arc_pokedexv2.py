from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
options.add_argument("-headless")
url2 = 'http://www.tokyochronos.net/_/api/chan/thread/?num=1834&board=cute&latest_doc_id=22'

import requests
import hashlib
import time

with requests.Session() as c:
    while 1:
        try:
            page2 = c.get(url2, headers={
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"})  # page to be compared against page1 / the base page
            file = open("pokemonhash.txt")
            myhash = file.readlines()
            myhash = myhash[0]
            print(myhash)
        except Exception as e:
            print(e)
            print('[+]Error Encountered during comparison page retrieval:')
        # hash functions
        myhash2 = hashlib.sha1(page2.text.encode('utf-8')).hexdigest()

        if myhash == myhash2:  # match hashes to detect site change
            print('[-]No Change Detected on ' + str(url2) + "")
            time.sleep(4)

        else:
            with open("pokemonhash.txt", "w") as f:
                f.write(myhash2)

            status_string = "[!]New hash detected"
            print(status_string)
            import requests
            import time

            url = "http://www.tokyochronos.net/cute/thread/1834/"
            try:
                from selenium.webdriver.firefox.options import Options as FirefoxOptions
                from selenium import webdriver


                # Proxy settings
                PROXY = "p.webshare.io:19999"
                webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                    "httpProxy": PROXY,
                    "ftpProxy": PROXY,
                    "sslProxy": PROXY,
                    "proxyType": "MANUAL",

                }

                # Fuuka functionality

                driver = webdriver.Firefox(options=options)

                driver.get("http://www.tokyochronos.net/cute/thread/1834/")

                ##Find last post in thread
                elements = driver.find_elements_by_xpath("//div[contains(@class, 'text')]")

                size = len(elements)
                print(size, "size")
                target_element = elements[size - 1]

                if (len(target_element.text.split("!pokemon", 1)) > 1):
                    ##Pokemon stuff

                    mysplitpokemon = (target_element.text.split("!pokemon", 1)[1])
                    print(mysplitpokemon)
                    mystrippedpokemon = (mysplitpokemon).lstrip()
                    print(mystrippedpokemon)
                    ##Get pokemon name
                    import json

                    mypokemon = mystrippedpokemon
                    import pokedex
                    from pokedex import pokedex
                    pokedex = pokedex.Pokedex(version='v1', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0')
                    pokemon = pokedex.get_pokemon_by_name(f'{mypokemon}')
                    print(pokemon)
                    ##Idiocy
                    with open('pokewrite.txt', 'w') as outfile:
                        json.dump(pokemon, outfile)

                    with open('pokewrite.txt') as json_file:
                        data = json.load(json_file)
                        print(data[0]['name'])
                        print(data[0]['species'])
                        print(data[0]['description'])
                        print('')
                        ArcLine = (data[0]['name'], '\n', data[0]['species'], '\n', data[0]['description'])
                        sprite = data[0]['sprite']
                        print(ArcLine)

                    ##Retreive sprite
                    url = sprite
                    r = requests.get(url, allow_redirects=True)

                    open(f'{mypokemon}' '.png', 'wb').write(r.content)

                    replybox = driver.find_element_by_id("reply_chennodiscursus")
                    replybox.send_keys(ArcLine)

                    replyboxN = driver.find_element_by_id("reply_bokunonome")
                    replyboxN.send_keys("Arc#0")

                    PokemonPNG = ("/home/selenium/"
                                  f"{mypokemon}"
                                  ".png"
                                  )
                    print(PokemonPNG)

                    replyboxFile = driver.find_element_by_id("file_image")
                    replyboxFile.send_keys(PokemonPNG)

                    print(pokemon)
                    element = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/article[1]/div[7]/section/form/fieldset/div[3]/div/input[1]").click()
                    time.sleep(11)
                    driver.quit()

                else:
                    pass
            except Exception as ex:
                print(ex)
                driver.quit()
                pass
