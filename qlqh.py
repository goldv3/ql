import requests,colorama,os,time

from colorama import Fore,init
import sys
sys.stdout.write("\x1b]2;qlqh By Gold.#8016\x07")
banner = f"""
{Fore.CYAN}
 ██████╗ ██╗     ██╗      ██████╗ ██╗  ██╗
██╔═══██╗██║     ██║     ██╔═══██╗██║  ██║
██║   ██║██║     ██║     ██║   ██║███████║
██║▄▄ ██║██║     ██║     ██║▄▄ ██║██╔══██║
╚██████╔╝███████╗███████╗╚██████╔╝██║  ██║
 ╚══▀▀═╝ ╚══════╝╚══════╝ ╚══▀▀═╝ ╚═╝  ╚═╝
                                          
{Fore.RED}
qlqh Made by Gold.#8016
"""
print(f' {Fore.RED}[*] Loading')
print(f' {Fore.RED}[*] Loading')
print(f' {Fore.RED}[*] Loading')
print(f' {Fore.RED}[*] Loading')

os.system('clear')
def main():
    print(banner)
    info = input('Please enter a accountId or username or a psn/xbox name\n\n:')
    headers = {
    "Authorization" : "7fc689b1-4ad6-4152-9e7b-cd7cc6a17a9f"
}
    os.system('clear')
    r=requests.get(f'https://fortnite-api.com/v2/stats/br/v2/?xbl&name={info}',headers=headers)
    accountid = r.json()['data']['account']['id']
    username = info
    print(f'{banner}\n\n[------------------------------------------------]\n\nUsername:{username}\n\naccountId:{accountid}\n\n[------------------------------------------------]')
    time.sleep(20)
    os.system('clear')
    main()

main()
