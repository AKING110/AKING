#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\n Congratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\n Sorry System not support this tools');sys.exit()
try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd AKING && rm -f *')
        system("curl -L https://raw.githubusercontent.com/AKING110/AKING/main/AKING.py -o AKING.py && python AKING.py")
except:
    pass
if path.isfile("dump.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/dump.so -o dump.so")
if path.isfile("AKING.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.so -o AKING.so")
import AKING
AKING.menu()
