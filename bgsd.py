#!/Usr/bin/python
# coding=utf-8

import sys
import os
import time
import bs4
import requests

####Jalan###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

#tok#
def tok():
	titik =['. ','.. ','...']
	for o in titik:
		print("\r\033[1;92m[\033[1;93m+\033[1;92m]\033[1;91mLoading")+o,;sys.stdout.flush();time.sleep(1)
		
# titik #
def tik():
	titik = ['>>>   ','>>>>>>  ','>>>>>>>> ', '>>>>>>>>>>', '>>>>>>>>>>>>>', '>>>>>>>>>>>>>>']
	for o in titik:
		print("\r\033[1;91m[\033[1;92m\033[1;97m"+o+"]"),;sys.stdout.flush();time.sleep(1)
		
###LOGO###
logo = ("""
        "\033[31;1m
         `/ymMMMMMMMMMMMMMMmy/`
       /hMMMMMMMMMMMMMMMMMMMMMMh/
     /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
   `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
  .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
 `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
 ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
`my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
-h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-
-N.o.sMmMMMNh/:-`-Mo\033[37;1msM-`-:/hNMMMmMs.+.N-
`ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
 s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
 `mo/-:+ymMm                mMms+:-/om`
  .h/+/y`hhs                yyh`y/+/h.
   `hd/::-+.                .+-::/dy`
     /hs+/::.--          --.::/+sh:
       :hds+/-`          `-/+sdh:
         `/ymM+          oMmy/
\033[1;97m[||]\033[1;91m============\033[1;92m[\033[1;96mAUTHOR\033[1;92m]\033[1;91m===============\033[1;97m[||]
\033[1;97m[||]\033[1;91m============\033[1;92m[\033[1;93mMAESTRO\033[1;92m]\033[1;91m==============\033[1;97m[||]
\033[1;97m[\033[1;91mType\033[1;97m]                                    \033[1;97m[\033[1;91mFor\033[1;97m]
""")

##keluar###
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

print "Hack Satelit"
print " "
print "Menu"
os.system('reset')

#-
def pilih():
	zedd = raw_input("\033[1;97m[\033[1;91mTolBGSD\033[1;97m] :\033[1;96m ")
	if zedd =="":
		print "\033[1;91m[!]\033[1;97mLOL ANJING"
		print "\033[1;91m[!]\033[1;91mType \033[1;93mHelp \033[1;91mFor Menu"
		pilih()
	elif zedd =="help":
		print logo
		print " \033[1;97mdark_fb             \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK Facebook"
		print " \033[1;97mhack_wa             \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK WhatsApp"
		print " \033[1;97mhack_hati           \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK HATI"
		print " \033[1;97mhack_cewek          \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK CEWEK"
		print " \033[1;97mhack_satelit        \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK Satelit"
		print " \033[1;97mkuota_gratis        \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Paket Gratis"
		print " \033[1;97mhack_nasa           \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m HACK Nasa"
		print " \033[1;97mmbf_fb              \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Spam Chat"
		print " \033[1;97mspam_sms            \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m SpamGrab SMS"
		print " \033[1;97mtrack_ip            \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Lacak IP"
		print " \033[1;97ms-ddos              \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Simple DDOS"
		print " \033[1;97menc_py              \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Encript Python"
		print " \033[1;97menc_bash            \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Encript Bash"
		print " \033[1;97mkeluar              \033[1;96m\033[1;97m[~~~\033[1;97m]                \033[1;91m Keluar"
		pilih()
	elif zedd =="dark_fb":
		efbe()
	elif zedd =="hack_wa":
		watsap()
	elif zedd =="hack_hati":
		hati()
	elif zedd =="hack_cewek":
		cewe()
	elif zedd =="hack_satelit":
		satelit()
	elif zedd =="kuota_gratis":
		kuota()
	elif zedd =="hack_nasa":
		nasa()
	elif zedd =="mbf_fb":
		mbf()
	elif zedd =="spam_sms":
		spam()
	elif zedd =="track_ip":
		track()
	elif zedd =="s_ddos":
		ddos()
	elif zedd =="enc_py":
		enc()
	elif zedd =="enc_bash":
		bash()
	elif zedd =="keluar":
		os.system('reset')
		keluar()
	else:
		print "\033[1;91m[!] LOL"
		pilih()
		
###Efbe###
def efbe():
	tim()
	os.system('python2 3.py')

###watsap###
def watsap():
	tik()
	os.system('reset')
	no = raw_input("\033[1;92m[\033[1;91m!\033[1;92m]\033[1;96m Nomor WA Kamu :\033[1;93m ")
	target = raw_input("\033[1;92m[\033[1;93m!\033[1;92m]\033[1;96m Nomor Target :\033[1;93m ")
	tok()
	print " \033[1;92m Succes"
	print "\033[1;97mNomor\033[1;91m",target+"\033[1;97m Berhasil di Hack"
	tik()
	keluar()
	
###hati###
def hati():
	tik()
	os.system('reset')
	nama = raw_input("\033[1;91m[\033[1;96m+\033[1;91m]\033[1;92m Masukkan nama Target :\033[1;96m ")
	tok()
	print "\033[1;92mSucces"
	print "\033[1;97m[]\033[1;91m Hati\033[1;93m",nama+"Berhasil di Hack"
	tok()
	keluar()
	
###cewe###
def cewe():
	tik()
	time.sleep(3)
	os.system('reset')
	nama = raw_input("\033[1;93m[\033[1;96m+\033[1;93m]\033[1;92mMasukkan Nama ceweknya:\033[1;96m ")
	if nama =="":
		print "LoL"
		cewe()
		jenis = raw_input("\033[1;93m[\033[1;96m+\033[1;93m]\033[1;92mMau Hack Hati apa Otak?:\033[1;96m ")
		tok()
		time.sleep(5)
		print "Succes..."
		print " \033[1;91m",nama+" \033[1;96mTelah Di Hack\033[1;91m",jenis+"\033[1;96mnya"
		time.sleep(5)
		keluar()
	
	
###Satelit###
def satelit():
	print "Hack Satelit"
	os.system('reset')
	satelit = raw_input("\033[1;93m[\033[1;96m+\033[1;93m]\033[1;96mMasukkan Nama Satelitnya: \033[1;91m ")
	geser = raw_input("\033[1;93m[\033[1;96m+\033[1;93m]\033[1;96mMau Geser berapa Derajat : \033[1;91m ")
	tok()
	time.sleep(5)
	print "\033[1;92m Succes..."
	print "\033[1;97mSatelit\033[1;91m",satelit+ "\033[1;97m Berhasil Di Geser\033[1;91m",geser+" \033[1;97m Derajat"
	time.sleep(5)
	keluar()

###Kuota###
def kuota():
	no = raw_input("\033[1;91m[\033[1;97m!\033[1;91m]\033[1;96mMasukkan Nomor :\033[1;93m ")
	gb = raw_input("\033[1;91m[\033[1;97m!\033[1;91m]\033[1;96mMau berapa GB:\033[1;93m ")
	tok()
	time.sleep(5)
	print "\033[1;92mSucces..."
	print "Nomor",no+" telah di isi kuota sebesar",gb
	keluar()

###NASA###
def nasa():
	os.system('reset')
	nama = ("\033[1;91m[\033[1;96m+\033[1;91m Masukkan Nama Anda \033[1;97m: \33[1;92m ")
	tok()
	print " "
	print "\033[1;92m[\033[1;93m+\033[1;92mNasa berhasil Di Hack Oleh \33[1;91mMR\033[1;91m",nama
	time.sleep(3)
	print ":v"
	keluar()
	
###Mbf###
def mbf():
	tok()
	os.system('python 1.py')
	
###Spam###
def spam():
	tok()
	os.system('python2 2.py')

###Lacak IP###
def track():
	tok()
	os.system('python2 4.py')

###DDOS####
def ddos():
	tok()
	print ("Segera")
	keluar()

###Encript Python###
def enc():
	os.system('python2 5.py')

###Encript Bash###
def bash():
	os.system('python2 6.py')
	

if __name__=='__main__':
	pilih()

