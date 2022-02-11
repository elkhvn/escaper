#!/usr/bin/env python3
import shutil
import os 

original = './escaper.py'
target = '/usr/bin/escaper'


try:
	shutil.copyfile(original, target)
	os.chmod(target,0o775)

except:
	print("""
Usage: sudo python3 setup.py

Run command with sudo privileges
""")