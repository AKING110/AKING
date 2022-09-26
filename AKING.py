#coding:utf-8
from platform import uname
from os import path,system,chmod
from sys import argv
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
else:
    exit("\033[1;31mSystem Not Support This Tools\033[1;37m")
while True:
        if path.isfile("dz.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/AKING110/Data/main/dz.so -o dz.so")
import AKING
