#!/usr/bin/env python3
import os
print("|||||||||||||  RUNNING THE APPLICATION ||||||||||||| \n")


print("Website starting... \n")
print(os.listdir(os.curdir))

# Running Backend
os.system("python3 run_backend.py")


# Running Frontend
os.system("python3 run_frontend.py")
