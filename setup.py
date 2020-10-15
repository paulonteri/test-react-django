#!/usr/bin/env python3
import os
print("|||||||||||||  APPLICATION SETUP ||||||||||||| \n")


print("Setup working... \n")
print(os.getcwd())
print(os.listdir(os.curdir))
print("\n")

# Install Python dependencies
print("\n")
print("\n")
print("Intalling Python dependencies... \n")
os.chdir('backend')
print(os.getcwd())
print(os.listdir(os.curdir))
os.system("pip install -r requirements.txt")

# Install Python dependencies
print("\n")
print("\n")
print("Creating database and making migrations... \n")
os.system("python3 manage.py migrate")


# setup frontend
print("\n")
print("\n")
print("SETTING UP FRONTEND... \n")
os.chdir('../frontend')
print(os.getcwd())
print(os.listdir(os.curdir))

print("\n")
print("\n")
print("Installing frontend dependencies")
os.system("npm install")


# Running Backend
print("\n")
print("\n")
print("Running Backend... \n")
os.chdir('../backend')
print("\n")
print("\n")
os.system("python3 manage.py runserver  &")
os.system("sleep 7")
print(os.getcwd())
print(os.listdir(os.curdir))

# Running Frontend
print("\n")
print("\n")
print("Running Frontend... \n")
os.chdir('../frontend')
print("\n")
print("\n")
print("Website starting... \n")
os.system("npm start")
