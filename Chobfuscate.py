# -*- coding:utf8 -*-

# Supports python2 & python3
# Name   : ChObfuscate - Simple Python Code Obfuscator
# Author : AmirHossein Ghanami (Ch4120N)

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile
import platform
from colorama import Fore, init
init()
# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n [-] Your Python Version is not Supported!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
b85 = lambda in_ : base64.b85encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x0a\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x43\x68\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x43\x68\x34\x31\x32\x30\x4e\x0a\x23\x20\x54\x69\x6d\x65\x20\x3a\x20%s\x0a\x23\x20\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x0a\n\n" % time.ctime()

def banner(): # Program Banner
    print(f"\x1b\x5b\x33\x36\x6d\x0a\x20\x5f\x5f\x5f\x5f\x5f\x5f\x20\x5f\x5f\x20\x20\x20\x20\x20\x5f\x5f\x5f\x5f\x5f\x5f\x5f\x20\x5f\x5f\x20\x20\x20\x20\x20\x5f\x5f\x5f\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x5f\x5f\x0a\x7c\x20\x20\x20\x20\x20\x20\x7c\x20\x20\x7c\x2d\x2d\x2e\x7c\x20\x20\x20\x20\x20\x20\x20\x7c\x20\x20\x7c\x2d\x2d\x2e\x27\x20\x20\x5f\x7c\x2e\x2d\x2d\x2e\x2d\x2d\x2e\x2d\x2d\x2d\x2d\x2d\x2e\x2d\x2d\x2d\x2d\x2e\x2d\x2d\x2d\x2e\x2d\x2e\x7c\x20\x20\x7c\x5f\x2e\x2d\x2d\x2d\x2d\x2d\x2e\x2d\x2d\x2d\x2d\x2e\x0a\x7c\x20\x20\x20\x2d\x2d\x2d\x7c\x20\x20\x20\x20\x20\x7c\x7c\x20\x20\x20\x2d\x20\x20\x20\x7c\x20\x20\x5f\x20\x20\x7c\x20\x20\x20\x5f\x7c\x7c\x20\x20\x7c\x20\x20\x7c\x5f\x5f\x20\x2d\x2d\x7c\x20\x20\x5f\x5f\x7c\x20\x20\x5f\x20\x20\x7c\x7c\x20\x20\x20\x5f\x7c\x20\x20\x5f\x20\x20\x7c\x20\x20\x20\x5f\x7c\x0a\x7c\x5f\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x7c\x5f\x5f\x7c\x7c\x5f\x5f\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x7c\x20\x20\x7c\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x5f\x2e\x5f\x7c\x7c\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x5f\x5f\x5f\x7c\x5f\x5f\x7c\x0a{Fore.YELLOW}\n\t\t╔════════════════════════════════════════════╗\n\t\t║                ChObfuscate                 ║\n\t\t║        Simple Python Code Obfuscator       ║\n\t\t║  Author  :  AmirHossein Ghanami (Ch4120N)  ║\n\t\t║  Github  :  Github.com/Ch4120N             ║\n\t\t╚════════════════════════════════════════════╝\n\n")

def menu(): # Program Menu
    print("\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x31\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x32\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x33\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x34\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x35\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x36\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x38\x35\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x37\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x38\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x30\x39\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x30\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x38\x35\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x31\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x32\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x33\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x34\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x35\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x42\x61\x73\x65\x38\x35\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x36\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x37\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x38\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x31\x39\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x20\x5a\x6c\x69\x62\x2c\x20\x42\x61\x73\x65\x38\x35\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x32\x30\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x53\x69\x6d\x70\x6c\x65\x20\x45\x6e\x63\x6f\x64\x65\x0a\x20\x1b\x5b\x33\x36\x6d\x5b\x1b\x5b\x33\x35\x6d\x32\x31\x1b\x5b\x33\x36\x6d\x5d\x1b\x5b\x33\x37\x6d\x20\x45\x78\x69\x74\x0a\n")

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f" {Fore.CYAN}[{Fore.LIGHTGREEN_EX}+{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Encoded File Size : {Fore.MAGENTA}{self.datas(dts)}{Fore.RESET}\n")
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    print(f" {Fore.CYAN}[{Fore.YELLOW}?{Fore.CYAN}]{Fore.WHITE} Encode Count : {Fore.RESET}", end="")
    loop = int(eval(_input % ""))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b85(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b85decode(__[::-1]);"
    elif option == 7:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 8:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 9:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 10:
        xx = "b85(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b85decode(__[::-1]));"
    elif option == 11:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 12:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 13:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 14:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 15:
        xx = "b85(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b85decode(__[::-1]));"
    elif option == 16:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 17:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 18:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 19:
        xx = "b85(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b85decode(__[::-1])));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Clear Console Display
def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
# Main Menu
def MainMenu():
    while 1:
        try:
            
            clear_console()
            banner()
            menu()
            try:
                print(f" {Fore.CYAN}[{Fore.YELLOW}?{Fore.CYAN}]{Fore.WHITE} Option : {Fore.RESET}", end="")
                option = int(eval(_input % ""))
            except ValueError:
                sys.exit("\n Invalid Option !")
            
            if option > 0 and option <= 21:
                if option == 21:
                    sys.exit(f"\n {Fore.CYAN}[{Fore.LIGHTGREEN_EX}+{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Thanks For Using this Tool")
                clear_console()
                banner()
            else:
                sys.exit(f'\n {Fore.CYAN}[{Fore.LIGHTRED_EX}-{Fore.CYAN}]{Fore.LIGHTRED_EX} Invalid Option !')
            try:
                print(f" {Fore.CYAN}[{Fore.YELLOW}?{Fore.CYAN}]{Fore.WHITE} File Name : ", end="")
                file = eval(_input % "")
                data = open(file).read()
            except IOError:
                sys.exit(f"\n {Fore.CYAN}[{Fore.LIGHTRED_EX}-{Fore.CYAN}]{Fore.LIGHTRED_EX} File Not Found !")
            
            output = file.lower().replace('.py', '') + '_obfuscated.py'
            if option == 20:
                SEncode(data,output)
            else:
                Encode(option,data,output)
            print(f"\n {Fore.CYAN}[{Fore.LIGHTGREEN_EX}+{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Successfully Encrypted {Fore.YELLOW}{file}{Fore.RESET}")
            print(f" {Fore.CYAN}[{Fore.LIGHTGREEN_EX}+{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Saved as {Fore.YELLOW}{output}{Fore.RESET}")
            FileSize(output)
        except KeyboardInterrupt:
            # time.sleep(1)
            sys.exit(f"\n\n {Fore.CYAN}[{Fore.LIGHTRED_EX}-{Fore.CYAN}]{Fore.LIGHTRED_EX} Program Terminated !")
        print(f" {Fore.CYAN}[{Fore.YELLOW}?{Fore.CYAN}]{Fore.WHITE} Press {Fore.YELLOW}[ENTER]{Fore.WHITE} to continue/Or Press {Fore.YELLOW}Ctrl+C{Fore.WHITE} to exit ...", end="")
        eval(_input % "")
        
if __name__ == "__main__":
    MainMenu()