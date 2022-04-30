import os
import time
import string
import random
import urllib3
import pyfiglet
from rich import print
from bs4 import BeautifulSoup
from selenium import webdriver
from rich.prompt import Prompt, Confirm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

allCodesArray = []

def mainMenu():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')
    title = pyfiglet.figlet_format("LAWNS NITROGEN V1", font='slant')
    print(f'[cyan]{title}[/cyan]')
    # print('[white][Discord] ->[/white] [cyan]https://discord.gg/UnA4ptfRX9[/cyan]')
    # print('[white][GitHub] ->[/white] [cyan]https://github.com/Lawnless/lawns-nitrogen-v1[/cyan]')
    print(' ')
    codeCount = Prompt.ask('[cyan][?][/cyan] How many codes you want to generate?\n[cyan][>][/cyan]', show_choices=False, show_default=False)
    print('[cyan][!][/cyan] Generating {} codes.'.format(codeCount))
    time.sleep(2)
    # writtenCount = 0
    for i in range(int(codeCount)):
        generateCodes()
        time.sleep(0.01)
        # writtenCount += 1
        # if writtenCount < 10:
        #     time.sleep(0.3)
        # elif writtenCount < 50 and writtenCount > 10:
        #     time.sleep(0.1)
        # elif writtenCount < 100 and writtenCount > 50:
        #     time.sleep(0.05)
    yesOrNo = Prompt.ask('[cyan][?][/cyan] Do you want to check these codes? [cyan][Y/N][/cyan]\n[cyan][>][/cyan]')
    if yesOrNo.upper() == 'Y':
        print('[cyan][!][/cyan] Checking {} codes.'.format(codeCount))
        time.sleep(2)
        checkCodes()
        writeToFile()
    else:
        writeToFile()

def generateCodes():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # size = random.randint(16, 24)
    rand = random.randint(0, 1)
    if rand == 0:
        size = 16
    else:
        size = 24
    generated = ''.join(random.choice(letters) for i in range(size))
    allCodesArray.append(generated)
    print('[cyan][>][/cyan] https://discord.gift/{}'.format(generated))
    # print('[white]{} | [/white][cyan][>][/cyan] https://discord.gift/{}'.format(len(allCodesArray), generated))

def checkCodes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for i in range(len(allCodesArray)):
        driver.get("https://www.discord.com/gifts/{}".format(allCodesArray[i]))
        time.sleep(1)
        if 'This gift code may be expired or you might have the wrong code.' in driver.page_source:
            print('[red][Not Working][/red] [white]https://discord.gift/{}'.format(allCodesArray[i]))
            time.sleep(0.01)
        else:
            # print('[red][Not Working][/red] https://discord.gift/{}'.format(allCodesArray[i]))
            print('[green][Working][/green] [white]https://discord.gift/{}'.format(allCodesArray[i]))
            # print('[white]{} | [/white][green][Working][/green] [white]https://discord.gift/{}'.format(i, allCodesArray[i]))
            time.sleep(0.01)

def writeToFile():
    yesOrNo = Prompt.ask('[cyan][?][/cyan] Do you want to write the codes to file? [grey](codes.txt)[/grey] [cyan][Y/N][/cyan]\n[cyan][>][/cyan]')
    if yesOrNo.upper() == 'Y':
        try:
            f = open("codes.txt", "a")
            for i in range(len(allCodesArray)):
                f.write('https://discord.gift/{}\n'.format(allCodesArray[i]))
            f.close()
        except FileNotFoundError:
            f = open("codes.txt", "x")
            for i in range(len(allCodesArray)):
                f.write('https://discord.gift/{}\n'.format(allCodesArray[i]))
            f.close()
        print('[cyan][!][/cyan] {} codes writed to the file.'.format(len(allCodesArray)))
        time.sleep(0.05)
        print('[cyan][!][/cyan] Thanks for using, goodbye!')
        time.sleep(0.05)
        exit()
    else:
        print('[cyan][!][/cyan] Thanks for using, goodbye!')
        time.sleep(0.05)
        exit()

mainMenu()