#! /usr/bin/env python3
import os
import sys
import time
import json
import random 
try:
    import requests
except:
    os.system('pip install requests')
try:
    import colorama
except:
    os.system('pip install colorama')
try:
    import pyshorteners
except:
    os.system('pip install pyshorteners')

from colorama import Fore, Back, Style, init
import requests
import pyshorteners

# Initialize colorama
init(autoreset=True)


c = Fore


# Reset
RESET = "\033[0m"

# Regular Colors
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

# Bold
BOLD_BLACK = "\033[1;30m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW = "\033[1;33m"
BOLD_BLUE = "\033[1;34m"
BOLD_PURPLE = "\033[1;35m"
BOLD_CYAN = "\033[1;36m"
BOLD_WHITE = "\033[1;37m"


UNDERLINE_BLACK = "\033[4;30m"
UNDERLINE_RED = "\033[4;31m"
UNDERLINE_GREEN = "\033[4;32m"
UNDERLINE_YELLOW = "\033[4;33m"
UNDERLINE_BLUE = "\033[4;34m"
UNDERLINE_PURPLE = "\033[4;35m"
UNDERLINE_CYAN = "\033[4;36m"
UNDERLINE_WHITE = "\033[4;37m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
HI_BLACK = "\033[0;90m"
HI_RED = "\033[0;91m"
HI_GREEN = "\033[0;92m"
HI_YELLOW = "\033[0;93m"
HI_BLUE = "\033[0;94m"
HI_PURPLE = "\033[0;95m"
HI_CYAN = "\033[0;96m"
HI_WHITE = "\033[0;97m"
BOLD_HI_BLACK = "\033[1;90m"
BOLD_HI_RED = "\033[1;91m"
BOLD_HI_GREEN = "\033[1;92m"
BOLD_HI_YELLOW = "\033[1;93m"
BOLD_HI_BLUE = "\033[1;94m"
BOLD_HI_PURPLE = "\033[1;95m"
BOLD_HI_CYAN = "\033[1;96m"
BOLD_HI_WHITE = "\033[1;97m"
BG_HI_BLACK = "\033[0;100m"
BG_HI_RED = "\033[0;101m"
BG_HI_GREEN = "\033[0;102m"
BG_HI_YELLOW = "\033[0;103m"
BG_HI_BLUE = "\033[0;104m"
BG_HI_PURPLE = "\033[0;105m"
BG_HI_CYAN = "\033[0;106m"
BG_HI_WHITE = "\033[0;107m"




class Urlmask:
    def __init__(self):
        self.shortlinks = []



    def shormeSite(self,url):
        try:
            url = requests.get(url=f"https://shortme.site/api?api=f7a7dcd6484967e9e8e7f3590dce66bb8a93665b&url={url}").json()['shortenedUrl']
            print(f'{GREEN}[+] URL MASK{RED}:{YELLOW} {str(url)} {PURPLE}    #(ADS){WHITE}')
        except:
            pass
   

    def shorten_with_all_services(self, url):
        shortener = pyshorteners.Shortener()
        services = ["tinyurl", "isgd"]

       
        try:
            s = pyshorteners.Shortener()
            
            try:
                short_url1 = s.tinyurl.short(url)
                print(f'{GREEN}[+] URL MASK{RED}:{YELLOW} {str(short_url1)}{WHITE}')
            except Exception as e:
                print(f"{RED}[!] TinyURL Error - {str(e)}{WHITE}")  
            try:
                short_url2 = s.isgd.short(url)
                print(f'{GREEN}[+] URL MASK{RED}:{YELLOW} {str(short_url2)}{WHITE}')
            except Exception as e:
                print(f"{RED}[!] is.gd Error - {str(e)} {WHITE}")
            try:
                short_url3 = s.dagd.short(url)
                print(f'{GREEN}[+] URL MASK{RED}:{YELLOW} {str(short_url3)}{WHITE}')
            except Exception as e:
                print(f"{RED}[!] da.gd Error - {str(e)} {WHITE}")
            try:
                short_url5 = s.clckru.short(url)
                print(f'{GREEN}[+] URL MASK{RED}:{YELLOW} {str(short_url5)}{WHITE}')
            except Exception as e:
                print(f"{RED}[!] clck.ru Error - {str(e)} {WHITE}")
        except Exception as main_error:
            print(f"{RED}[!] General Error - {str(main_error)} {WHITE}")




    def run(self,url):
        self.shormeSite(url=url)
        self.shorten_with_all_services(url=url)


            


        


#Urlmask().run(url='https://www.google.com')

def banner():
    bnr = f"""{RED}
             __                          __       ______ 
.--.--.----.|  |  .--------.---.-.-----.|  |--.  |__    |
|  |  |   _||  |  |        |  _  |__ --||    <   |__    |
|_____|__|  |__|  |__|__|__|___._|_____||__|__|  |______|
{GREEN}             Telegram{RED}:{PURPLE} https://t.me/how_tohack 
"""
    print(bnr)


def main():
    banner()
    link = ''
    try:
        link = sys.argv[1]
    except:
        link = input(f"{BLUE}[*] Enter Url: {YELLOW}")
    if link:
        print('')
        Urlmask().run(url=link)

    





if __name__ == "__main__":
    main(); 










