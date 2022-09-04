#coding-utf-8
from platform import uname
from os import path,system,chmod
from sys import argv
try:
	import random_user_agent
except ImportError:
	os.system('pip install random_user_agent')
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
    print('\n\033[1;32m Congregations! Your Device Support This Tools\033[1;37m')
else:
    exit("\033[1;31m System Not Support This Tools\033[1;37m")
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
try:
    import AKING
except:
    exit("\n\n Something Working Was Wrong\n Run : \033[1;37m python AKING.py reset \033[1;37m")
print('[>] Run Script :- \033[1;32m python AKING.py\033[1;37m')
