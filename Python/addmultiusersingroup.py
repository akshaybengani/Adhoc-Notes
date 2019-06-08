# usermod -G tech username

import subprocess

usernames = input("Enter names of users seperated with commas\n")
groupname = input("Enter group name ")

nameList = usernames.split(',')


for name in nameList:
    cmdString = "usermod -G "+groupname+" "+name
    print(cmdString)
    subprocess.getoutput(cmdString)