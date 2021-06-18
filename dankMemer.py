import requests
import threading
import time
import random
import os
import colored
from colored import fg, bg, attr, stylize

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
red = fg(1)

print(stylize("""

\t\t██████╗  █████╗ ███╗   ██╗██╗  ██╗     ██████╗ ██████╗ ██╗███╗   ██╗██████╗ ███████╗██████╗ 
\t\t██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔════╝ ██╔══██╗██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
\t\t██║  ██║███████║██╔██╗ ██║█████╔╝     ██║  ███╗██████╔╝██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
\t\t██║  ██║██╔══██║██║╚██╗██║██╔═██╗     ██║   ██║██╔══██╗██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
\t\t██████╔╝██║  ██║██║ ╚████║██║  ██╗    ╚██████╔╝██║  ██║██║██║ ╚████║██████╔╝███████╗██║  ██║
\t\t╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                            
""", red))


PERIOD_OF_TIME = int(input(f"{r2}[{b}?{r2}] Time in seconds: "))
while True:    
    token = input(f"\n{r2}[{b}?{r2}] Token: ")
    channel = input(f"{r2}[{b}?{r2}] Channel Id: ")

    def execute_command(command = "", cooldown = 0):
        print(f"{r2}[{b}!{r2} Loaded: '{command}' With cooldown of {cooldown} Seconds")
        while True:
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

    print()

    startime = time.time()

    for cmd, cooldown in commands.items():
        threading.Thread(target = execute_command, kwargs = {"command" : cmd, "cooldown" : cooldown}).start()
        print("sleep")
        time.sleep(5)
        if time.time() >= startime + PERIOD_OF_TIME:
            print("Time limit exceeded")
            time.sleep(3)
            os._exit(1)
        else:
            continue

        