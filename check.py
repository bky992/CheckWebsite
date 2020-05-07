#Created by @bky_992
#4Study
#theMx0nday


import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Check WebSite")
print(ascii_banner)
print("by bky992 (4Study)")
print("[!] Place the website below \/")
Url = str(input(' > '))
request = requests.get(Url)

if request.status_code == 200:
    print("[+]Website ok (200 ok)")
    content = request.content
elif request.status_code == 503:
    print("[+]site is dead. (503 unavailabled)")
elif request.status_code == 403:
    print("[+] Insufficient permissions to access the page (403 Forbidden)")
