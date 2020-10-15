#!/usr/bin/env python3
import os
print("|||||||||||||  APPLICATION ||||||||||||| \n")


print("Website starting... \n")

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
