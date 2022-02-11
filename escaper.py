#!/usr/bin/env python3


import sys
import os.path
import re


n=len(sys.argv)


# Adding colors to our output
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'








text=input(bcolors.WARNING + "\nEnter the text you want to escape:\n" + bcolors.ENDC)


text = re.sub("\"","\\\"",text)
text = re.sub("\$","\\\$",text)
text = re.sub("\`","\\\`",text)
text = re.sub("!","\\!",text)


print(bcolors.OKGREEN + "\n\n\n\nResult:\n" + bcolors.ENDC + text)

