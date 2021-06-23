import requests
import threading
import time
import random
import sys, os
import colored
from colored import fg, bg, attr, stylize
import keyboard 
import tkinter as tk
from tkinter import ttk, messagebox 

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
red = fg(1)
green = fg(2)
root = tk.Tk()
root.withdraw()
__version__ = '1.4'
_AppName_ = "DankGrinder"

def download_file(url, filename=''):
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

try:
    # -- Online Version File
    # -- Replace the url for your file online with the one below.
    response = requests.get(
        'https://raw.githubusercontent.com/DitaMatata/DankGrinder/main/version.txt')
    data = response.text

    if float(data) > float(__version__):
        messagebox.showinfo('Software Update', 'Update Available!')
        mb1 = messagebox.askyesno('Update!', fr'Do you want to update to v{data}?')
        if mb1 is True:
            downloadLink = 'https://github.com/DitaMatata/DankGrinder/releases/download/v1.2/DankGrinder.-.v1.5.exe'
            download_file(downloadLink, 'DankGrinder - v1.4.exe')
            sys.exit()
        elif mb1 == False:
            os.system("cls")
            pass
    else:
        messagebox.showinfo('Software Update', 'No Updates are Available.')
except Exception as e:
    messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))


print(stylize("""
\t\t██████╗  █████╗ ███╗   ██╗██╗  ██╗     ██████╗ ██████╗ ██╗███╗   ██╗██████╗ ███████╗██████╗ 
\t\t██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔════╝ ██╔══██╗██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
\t\t██║  ██║███████║██╔██╗ ██║█████╔╝     ██║  ███╗██████╔╝██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
\t\t██║  ██║██╔══██║██║╚██╗██║██╔═██╗     ██║   ██║██╔══██╗██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
\t\t██████╔╝██║  ██║██║ ╚████║██║  ██╗    ╚██████╔╝██║  ██║██║██║ ╚████║██████╔╝███████╗██║  ██║
\t\t╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                          
""", red))

check = input(f"{r2}Do you have a previous save file? [Enter y or n] ")
if check == 'y' or check == 'Y':
    a = open("tokenandid.txt", "r")
    x = a.read().split(":")
    token = x[0]
    channel = x[1]
    print(token + channel)
    a.close()
else: 
    save = input(f"{r2}Do you want to save your token and id? [Enter y or n] ")
    token = input(f"{r2}[{b}?{r2}] Token: ")
    channel = input(f"{r2}[{b}?{r2}] Channel Id: ")
    if save == 'y' or save == 'Y':
        a = open("tokenandid.txt", "w+")
        a.write(f'{token}:{channel}')
        a.close()
    else:
        pass
PERIOD_OF_TIME = int(input(f"{r2}[{b}?{r2}] Time in seconds: "))
while True:    
    startime = time.time()
    def execute_command(command = "", cooldown = 0):
        while True:
            if time.time() >= startime + PERIOD_OF_TIME:
                print("Time limit exceeded")
                break
            print(f"{r2}[{b}!{r2}] Loaded: '{command}' With cooldown of {cooldown} Seconds")

            requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data = {'content': command},
                headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization' : token
                }
            )
            print(f"{r2}[{b}+{r2}] '{command}' Ran successfully")

            time.sleep(cooldown + random.randint(2, 10))

    commands = {
        "pls beg" : 45,
        "pls hunt" : 40,
        "pls fish" : 40,
        "pls dig" : 40,
        "pls daily" : 86400
    }
    
    for cmd, cooldown in commands.items():
        threading.Thread(target = execute_command, kwargs = {"command" : cmd, "cooldown" : cooldown}).start()
        time.sleep(5)
    break
