import getpass
import pickle
#from tkinter import *

masterpass= input("Enter Your Master Password\n")

if masterpass=="12345":
    acc_name=input("Enter Your Account Name\n")

    with open("pass.me", "rb") as readme:
       dicti=pickle.load(readme)

    if acc_name in dicti:
        password=getpass.dicti[acc_name]
        print("\nPassword= ",password)
        exit(0)
    else:
        print("\nInformation is incorrect\n")
        exit(0)


