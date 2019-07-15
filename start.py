#!/bin/usr/python
import os,sys,time

os.system('pkg install python2')
os.system('pip2 install requests')
os.system('pip2 install bs4')
os.system('pip2 install requests')
os.system('pip2 install mechanize')

print "\033[1;91m[]\033[1;92m Selesai.."
time.sleep(1)
os.system('python2 bgsd.py')
