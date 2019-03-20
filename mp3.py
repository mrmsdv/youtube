# -- encoding: utf-8 --
import os, sys
import time , random


def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.5)
ketik("Created By Mr_MSDV")
print "sebelumnya sudah pernah install Tools Ini ? Y/n ?"
n = raw_input("masukan pilihan : ")
if n == 'n':
	print "install Program "
	os.system("sh install.sh")
if n == 'y':
	ketik("waiting.....")
	ketik("mau loading bentar . . . ")
	os.system("clear")
	print "kalau ingin search ketikan comand"
	print "search nama_lagu.mp3"
	os.system("mpsyt")

