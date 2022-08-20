import os,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print('\033[1;32m[•] Congrats! Your Device Support This Tools \033[1;37m')
    os.system('xdg-open https://facebook.com/groups/351076900316263/')
    import AKING
else:
    exit('\033[1;31m[×] Sorry Device Not Support')
