import subprocess
import argparse

a = subprocess.Popen('netsh wlan show profile', shell=True, stdout=subprocess.PIPE)
b = a.stdout.read()
c = b.split("All User Profile     : ")

lst = len(c) - 1


while lst!=0:
	ab = subprocess.Popen('netsh wlan show profile name="%s" key=clear' %c[lst].rstrip(), shell=True, stdout=subprocess.PIPE)
	b1 = ab.stdout.read()
	c1 = b1.split("Key Content            : ")
	passwords = c1[1].split("Cost settings")[0].rstrip()
	print "\n" + c[lst].rstrip() + "   ==>>  " + passwords + "\n"
	lst = lst - 1


a = raw_input()