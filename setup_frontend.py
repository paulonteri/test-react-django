#!/usr/bin/env python3
import os
import subprocess

# setup frontend
print("\n")
print("\n")
print("SETTING UP FRONTEND... \n")
os.chdir('frontend')
print(os.getcwd())
print(os.listdir(os.curdir))

print("\n")
print("\n")
print("Installing frontend dependencies")
subprocess.check_call(["npm", "install"])
