#!/usr/bin/env python3
import os
import subprocess

print("Backend starting... \n")

# Running Backend
print("\n")
print("\n")
print("Running Backend... \n")
os.chdir('backend')
print("\n")
print("\n")
os.system("python3 manage.py runserver  &")
os.system("sleep 10")
print("\n")
print("\n")
print("\n")
print(os.getcwd())
print(os.listdir(os.curdir))
