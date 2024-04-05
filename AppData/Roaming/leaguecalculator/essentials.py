__version__ = "1.0.0"

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
                    l_en.append(x.replace("\n",""))
                
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

        template = ''.join(file.read("data\dpy.txt"))

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

