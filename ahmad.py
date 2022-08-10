import os,time,platform
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
os.system('xdg-open https://www.facebook.com/groups/351076900316263/permalink/374959374594682/')
logo = ("""\033[1;37m    ###    ##    ## #### ##    ##  ######  ❤
   ## ##   ##   ##   ##  ###   ## ##    ##
  ##   ##  ##  ##    ##  ####  ## ##
 ##     ## #####     ##  ## ## ## ##   ####
 ######### ##  ##    ##  ##  #### ##    ##
 ##     ## ##   ##   ##  ##   ### ##    ##
 ##     ## ##    ## #### ##    ##  ######  ❤
(!)══════════════════════════════════════════
(!) Author   : ahmad khan
(!) Guthub   : ahmad
(!) Facebook : MR.AKING.07
(!) Type     : free
(!) Version  : 1.2.1
\033[1;37m(!)══════════════════════════════════════════""")

def Run():
	bit = platform.architecture()[0]
	os.system('clear')
	print(logo)
	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')
	print('[1] Pak Cloning \n[2] BD Cloning\n[0] Exit')
	Aking = input('[•] Choose : ')
	if free =='1':
		if bit =='32bit':
			import free32
		elif bit =='64bit':
			import free
	elif Aking =='2':
		if bit =='32bit':
			import BD32
		elif bit =='64bit':
			import BD
Run()
