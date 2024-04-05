import customtkinter
import re
import os
import math
import sys
import os
from PIL import Image
import requests

folder_name = "leaguecalculator"
file_path = '%s\\{}'.format(folder_name) %  os.environ['APPDATA'] 
if not os.path.exists(file_path):
    os.makedirs(file_path)

def download_img(dir, name, pic_url):

    with open(f'{dir}\\{name}', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    
    logo = Image.open(f'{dir}\\{name}')
    new_name = "lol.ico"
    logo.save(f'{dir}\\{new_name}',format="ICO")
    os.remove(f'{dir}\\{name}')
    

def file_write(file: str, object: str):
    try:
        with open(file, "w") as f:
            f.write(object)
            return True
    except:
        return False

def look_for_files():
    package = """__version__ = "1.0.0"

# Essentials API

def roundify(n):
    import math
    m = 1
    return int(math.ceil(n*m)/m)

class string():
    
    def before(text: str, kw: str):
        return text[:text.index(kw)]

    def after(text: str, kw: str):
        return text[text.index(kw):].replace(kw,"")

class file():

    def read(file: str):
        try:
            with open(file, "r") as f:
                x = ''.join(f.readlines())
                if x == "":
                    return None
                return x
        except:
            return None
    
    def readlines(file: str):
        try:
            with open(file, "r") as f:
                x = f.readlines()
                if x == "[]":
                    return None
                return x

        except:
            return None
    
    def write(file: str, object: str):
        try:
            with open(file, "w") as f:
                f.write(object)
                return True
        except:
            return False
    
    def append(file: str, object: str):
        try:
            with open(file, "a") as f:
                f.write(object)
                return True

        except:
            return None
        
    def look_for(file: str, object: str):
        try:
            with open(file, "r") as f:
                list = f.readlines()
                l_en = []
                for x in list:
                    l_en.append(x.replace("\\n",""))
                
                if object in l_en:
                    return True
                else:
                    return False
                
        except:
            return None

class text():

    def default(text: str):
        return text.capitalize().rstrip()
    
    def title(text: str):

        t: str= ""
        i = 0

        for x in text.split():
            if i == len(text.split()) - 1:
                t += x.capitalize()
            else:
                t += x.capitalize() + " "

            i += 1
        
        return t.rstrip()

class templates():

    def discord_py():

        template = ''.join(file.read("data\\dpy.txt"))

        if file.read("discord.py") == None:
            file.write("discord.py", template)
        else:
            loop = True
            i = 2
            while loop:
                if file.read("discord{}.py".format(i)) == None:
                    file.write("discord{}.py".format(i), template)
                    loop = False
                
                i += 1

"""
    defaultrank = "1\n4\n0"
    items = {"lol.ico":download_img(file_path, "lol.png", "https://i.postimg.cc/8zdm3x9S/lol.png"), "essentials.py":file_write(f"{file_path}\\essentials.py", package), "rank.txt":file_write(f"{file_path}\\rank.txt", defaultrank)}

    for item in items:
        if not os.path.exists(file_path + "\\%s" % item):
            items[item]

look_for_files()

sys.path.insert(0, file_path)
from essentials import *

class league():

    def round_up(n, p): 
        m = 10**p  
        return (math.ceil(n*m)/m) 

    def substring_after(s, delim):
        return s.partition(delim)[2]

    def sortRank(currentrank):
        ranks = {1:"Iron",2:"Bronze",3:"Silver",4:"Gold",5:"Platinum",6:"Emerald",7:"Diamond",8:"Master",9:"Grand Master",10:"Challenger"}
        rank = "".join(ranks[currentrank])

        return rank
        
    def get_rank(self):
        txt = file.read(file_path + "\\rank.txt").split()

        currentrank = int(txt[0])
        league = txt[1]
        lp = int(txt[2])
        return [self.sortRank(currentrank), league, lp, currentrank]

    def get_text(self):
        data = self.get_rank(self)

        rank = data[0]
        league = int(data[1])
        lp = int(data[2])

        game = (int((100 - lp) / 20))
        game = int(self.round_up(game, 0))
        if game < 1:
            game = 1
        
        avglp = int(100 - lp) / game
        avglp = int(self.round_up(avglp, 0))
        if game > 1:
            addition = "s"
        else:
            addition = ""

        return f"You are {rank} {league}, {lp} lp. \n+{100 - lp} lp's to rankup.\nEstimated {game} (+{avglp} lp per) game{addition} away from rankup."
    
    def get_newrank(interact, self):
        data = self.get_rank(self)

        numrank = int(data[3])
        league = int(data[1])
        lp = int(data[2])

        if interact == None:
            return
        if interact[0] == "-":
            num = self.substring_after(interact, "-")
            afterlp = int(lp) - int(num)
            if afterlp < 0:
                afterlp = 75
                if league == 4:
                    numrank -= 1
                    league = 1
                elif league < 4:
                    league += 1
                if numrank < 1:
                    numrank = 1
            data = f"{numrank}\n{league}\n{afterlp}"
            file.write(file_path + "\\rank.txt", data)
            
        elif interact[0] == "+":
            num = self.substring_after(interact, "+")
            afterlp = int(lp) + int(num)
            if afterlp > 99:
                afterlp = afterlp - 100
                afterlp = str(afterlp).replace("+","")
                if league == 1:
                    numrank += 1
                    league = 4
                elif league > 1:
                    league -= 1
                if numrank > 5:
                    numrank = 5
            data = f"{numrank}\n{league}\n{afterlp}"
            file.write(file_path + "\\rank.txt", data)

class LeagueGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("League WR Ratio")
        self.iconbitmap(file_path + "\\lol.ico") # Get the ico from appdata

        self.app_width, self.app_height = 600, 400
        self.set_window_position()

        self.textbox = customtkinter.CTkTextbox(width=300, height=150, master=self)
        self.button = customtkinter.CTkButton(master=self, text="Match Result", command=self.open_input_dialog_event)
        self.logo_label = customtkinter.CTkLabel(master=self, text="Made by Zgn", font=customtkinter.CTkFont(size=16, weight="bold"))

        self.textbox.grid(row=0, column=1, padx=(40, 0), pady=(0, 200))
        self.logo_label.grid(row=0, column=0, padx=5, pady=(365, 0))

        self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.update_textbox()

    def set_window_position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (self.app_width / 2)
        y = (screen_height / 2) - (self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(x)}+{int(y)}")

    def update_textbox(self):
        self.textbox.delete("0.0", customtkinter.END)
        self.textbox.insert("0.0", "\t\tWR Ratio\n\n\n" + league.get_text(league))

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Enter your LP\n(such as +25 or -8)", title="League WR Ratio")
        dialog_width, dialog_height = 300, 200
        x, y = self.get_window_position(dialog_width, dialog_height, self)
        dialog.geometry(f"{dialog_width}x{dialog_height}+{int(x)}+{int(y)}")
        lp = str(dialog.get_input())
        league.get_newrank(lp, league)
        self.update_textbox()

    @staticmethod
    def get_window_position(width, height, self):
        screen_width = LeagueGUI.winfo_screenwidth(self)
        screen_height = LeagueGUI.winfo_screenheight(self)
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        return x, y

if __name__ == "__main__":
    app = LeagueGUI()
    app.mainloop()