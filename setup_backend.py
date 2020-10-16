#!/usr/bin/env python3
import os
import subprocess


# Install Python dependencies
print("\n")
print("\n")
print("Intalling Python dependencies... \n")
os.chdir('backend')
print(os.getcwd())
print(os.listdir(os.curdir))
subprocess.check_call(["pip3", "install", "-r", "requirements.txt"])

# Install Python dependencies
print("\n")
print("\n")
print("Creating database and making migrations... \n")
subprocess.check_call(["python3", "manage.py", "migrate"])
