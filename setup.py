#!/usr/bin/env python3
import os
import subprocess
print("|||||||||||||  SETUP ||||||||||||| \n")

# verify python
ver_py = subprocess.check_output(["python3", "--version"])
if not ("python 3" in (str(ver_py)).lower()):
    raise Exception("Please intall Python 3 !!!!!!!!!")
try:
    subprocess.check_call(["pip3", "install", "django"])
except Exception as e:
    print("\n \n \n \n")
    print("CANNOT INSTALL PYTHON PACKAGES.....")
    print("It is very likely that this is not a problem with the setup...")
    print("This script cannot run without the permission to install packages...")
    print("Please fix the permissions first...")
    print("\n")
    raise e

ver_js = subprocess.check_output(["node", "--version"])
if not ("v" in (str(ver_js)).lower()) or len(ver_js) < 5 or len(ver_js) > 20:
    raise Exception("Please intall Node !!!!!!!!!")
subprocess.check_call(["node", "test.js"])


print("Setup working... \n")
print(os.getcwd())
print(os.listdir(os.curdir))
print("\n")
os.system("sleep 2")


print("||||||||||||| BACKEND  ||||||||||||| \n")
print(os.getcwd())
print(os.listdir(os.curdir))
subprocess.check_call(["python3", "setup_backend.py"])
os.system("sleep 4")

print("|||||||||||||  FRONTEND  ||||||||||||| \n")
print(os.getcwd())
print(os.listdir(os.curdir))
subprocess.check_call(["python3", "setup_frontend.py"])
os.system("sleep 4")

# Running Application
print("||||||||||||| RUN  ||||||||||||| \n")
print(os.getcwd())
print(os.listdir(os.curdir))
subprocess.check_call(["python3", "run_application.py"])
