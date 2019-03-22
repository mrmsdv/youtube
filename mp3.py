# -- encoding: utf-8 --
import os, sys
import time , random 

r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"

def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
print """
      %s+===========================+
      |%s script Created By %sMr_MSDV %s|
      +===========================+"""%(y,g,c,y)

def keluar():
	os.system("exit")


def start():
	print "%s[!] %ssebelumnya sudah pernah install Tools Ini %s? %sY/n %s?"%(r,g,r,c,r)
	while True :
		n = raw_input("masukan pilihan : ")

		if n == 'n':
				print "install Program "
				os.system("sh install.sh")
				ketik("install selesai . . . .")
				print("Untuk Menjalankan Tools Masukan comand mpsyt")
				time.sleep(3)
				pass
		elif n == 'y':
				ketik("%swaiting%s.%s.%s.%s.%s."%(g,r,c,y,w,g))
				ketik("%smau %sloading %sbentar . . . "%(g,r,g))
				print "kalau ingin search ketik %s'/nama_lagu'"%(c)
				os.system("mpsyt")
				break
				
		elif n == '':
				print("pilihan tidak Ada")
				print ("masukan comand yang Benar")
				time.sleep(1.5)
				os.system("clear")
				start()
		
		

	
start()

