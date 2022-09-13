#coding:utf-8
from platform import uname
from os import path,system,chmod
from sys import argv
try:
	import random_user_agent
except ImportError:
	system('pip install random_user_agent')
try:
    if argv[1].lower()=="reset":
        system("rm -rf *")
        system('curl -L https://raw.githubusercontent.com/AKING110/AKING/main/AKING.py -o AKING.py')
        system('python AKING.py')
except:
    pass
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\n\033[1;32mCongratulations! Your Device Support This Tools\033[1;37m')
    system('pkg install play-audio')
else:
    exit("\033[1;31mSystem Not Support This Tools\033[1;37m")
while True:
        if path.isfile("AKING.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.so -o AKING.so")
        if path.isfile("dz.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/dz.so -o dz.so")
try:
    import random_user_agent
    import AKING
except:
    exit("\n\n Something Working Was Wrong\n Run : \033[1;37m python AKING.py reset \033[1;37m")
print('\n[>] Run Script :- \033[1;32m python AKING.py\033[1;37m')
