from platform import uname
from os import path,system,chmod
from sys import argv
try:
    if argv[1].lower()=="reset":
        system("rm -rf AKING.so")
        system("rm -rf RNDM.so")
        system("rm -rf dz.so")
except:
    pass
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
else:
    exit("\033[1;31m System Not Support This Tools")
while True:
        if path.isfile("RNDM.so"):                                                                                                                       
            break
        else:
            system('clear')
            print(' \033[1;32m installing files please wait...\033[1;37m')
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/RNDM.cpython-310.so -o RNDM.so")
        if path.isfile("AKING.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.cpython-310.so -o AKING.so")
        if path.isfile("dz.so"):
             break
        else:
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/dz.so -o dz.so")
import AKING
exit("\n\n Something Working Was Wrong\n Run :  python AKING.py reset ")
