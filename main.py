#!/usr/bin python3

from os import system, path
from sys import exit
import warnings
import argparse
from plugins.styling import *


# Disable wornings
warnings.filterwarnings("ignore")

def x(command):
    system(command)

# Print Banner
bannerFunc()

# Command Line Utility
parser = argparse.ArgumentParser(usage="Help Menu of untimSubs")
parser.add_argument('-d', '--domain' ,dest="d", help="Enter Domain Name", type=str, required=True)
args = parser.parse_args()

domainName = args.d

def mainFunction():

    if domainName:
        print("")
        print(f"{bold}{orange}Target :{purple} {domainName} {reset}")
        print("")
        # Make and change or Change Directory
        if path.exists("Tools") == True:
            x("cd Tools")

        else:
            x("mkdir Tools")
            x("cd Tools")
        x("mkdir Subdomains")

        # Finding Subdomains using amass
        print(f"{bold}{blue}\nFinding Subdomains using amass, Please wait...{reset}")
        x(f"amass enum -d {domainName} > Subdomains/subdomansAmass.txt")

        # Finding Subdomains using sublist3r
        print(f"{bold}{blue}\nFinding Subdomains using sublist3r, Please wait...{reset}")
        x(f"sublist3r -d {domainName} > Subdomains/subdomansSublist3r.txt")
        print("\n\n")
        
        # Finding Subdomains using sublist3r
        print(f"{bold}{blue}\nFinding Subdomains using sublist3r, Please wait...{reset}")
        x(f"subfinder -d {domainName} -o Subdomains/subdomansSubfinder.txt")
        print("\n\n")

        # Finding Subdomains using subbrute
        print(f"{bold}{blue}\nFinding Subdomains using subbrute, Please wait...{reset}")
        x("cd subbrute")
        x(f"python3 subbrute.py {domainName} > Subdomains/subdomansSubbrute.txt")
        x("cd ..")
        print("\n\n")

        # Finding Subdomains using Knock
        print(f"{bold}{blue}\nFinding Subdomains using Knock, Please wait...{reset}")
        x("cd KnockPy")
        x(f"python knock.py {domainName} > Subdomains/subdomansKnock.txt")
        x("cd ..")
        print("\n\n")

    else:
        print("")
        print(f"{bold}{red}Please enter valid credential.{reset}")
        exit(0)

# Call main function
if __name__ == "__main__":
    try:
        mainFunction()
    except KeyboardInterrupt:
        getOpinion = input("\nWant to exit : (y/n)").lower()
        if getOpinion == "y":
            exit()
        elif getOpinion == "n":
            pass
        else:
            print("Enter 'y' for yes and 'n' for no.")