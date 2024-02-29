import random
import pyfiglet
import webbrowser
import os
from colorama import Fore
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

toolname=pyfiglet.figlet_format("Shanawaz Whatsapp Bomber")

print(toolname)
driver = None  

def main():
    clean()
    banner()
    ans=True
    while ans:
        print("""
        1. Start bombing
        2. Follow me on Insta
        3. Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            clean()
            bomb()
        elif ans=="2":
            webbrowser.open('https://www.instagram.com/shanawaz_hacker?igsh=MXJkdHd5bmYwaDE5Ng==')
            print("\n Thanks for follow me!")
            sleep(0.3)
            main()
        elif ans=="3":
            print("\n Goodbye")
            ans = None
            exit()
        else:
            print("\n Not a valid choice. Try again.")
            sleep(0.3)
            main()

def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Set path to the ChromeDriver executable.
    service = Service(ChromeDriverManager().install())

    global driver  # Use the global driver variable
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://web.whatsapp.com/')

    return driver  # Return the initialized driver object

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def bomb():
    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key whenever you\'re ready!')

    user = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
    user.click()

    print('Waiting 5 seconds to let WhatsApp load...')
    sleep(5)
    # The classname of message box may vary.
    msg_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        button.click()

    print('Bombing Complete!!')
    sleep(5)
    main()

driver = setup()
input('Enter any key after scanning QR code')
main()
