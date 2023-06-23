import requests
from datetime import datetime
import os
from colorama import Fore, Style

##time shit
current_time = datetime.now().strftime(f"{Fore.MAGENTA}[{Fore.WHITE}%H:%M:%S{Fore.MAGENTA}]")

##code
url = "https://discord.com/api/v9/users/@me/profile"
headers = {
    "authorization": "",
}

def update_profile(token, new_pronouns):
    headers["authorization"] = token
    
    data = {
        "pronouns": new_pronouns,
    }
    
    response = requests.patch(url, headers=headers, json=data)
    
    response_dict = response.json()
    
    
    if response.ok:
        print(f"{Fore.MAGENTA}{current_time} {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Profile Updated! {Fore.WHITE} {'***' + token[-10:]}:{Style.RESET_ALL}")
    else:
        error_message = response_dict.get("message", "An unknown error occurred.")
        print(f"{Fore.MAGENTA}{current_time} {Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Failed! {Fore.WHITE} {'***' + token[-10:]}:{Style.RESET_ALL}")

os.system("cls")
new_pronouns = input("[input] Enter your new pronouns: ")

with open("tokens.txt", "r") as f:
    for line in f:
        token = line.strip()
        update_profile(token, new_pronouns)
