import platform
import os

try:os.system("clear")
except:pass	
os.system('termux-setup-storage')
os.system('python -m pip uninstall urllib3 && python -m pip install urllib3')
os.system('pkg install wget')
os.system('git pull')
try:os.system('touch OK.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("OFF").offfside()
elif 'aarch' in arc:
	__import__("Naveed").Haris()
else:
	exit(f' Unknow device machine {arc}')


	

	















