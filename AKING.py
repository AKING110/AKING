#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\nSorry System not support this tools');sys.exit()

try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd AKING && rm -f *')
        system("curl -L https://raw.githubusercontent.com/AKING110/AKING/main/AKING.py -o AKING.py && python AKING.py")
except:
    pass
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/dz.so -o dz.so")
system('clear')
print('\n\n\033[1;37m[•] This tools only for 64bit device ')
print('\n[1] Start Cloning V1.3.9 \n[2] Start Random Cloning V1.3.8 (Updated)\n[3] Check Update \n')
xd=input('[•] choose: ')
if xd in ['1','01']:
    if path.isfile('AKING.so'):
        import AKING
    else:
        system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.so -o AKING.so")
        import AKING
elif xd in ['2','02']:
    if path.isfile('Random.so'):
        import Random
    else:
        system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/Random.so -o Random.so")
        import Random
else:
        print('\n[•] Checking updates...')
        system('python AKING.py update')
