import argparse
import subprocess
import os

parser = argparse.ArgumentParser()

parser.add_argument('-a')    
parser.add_argument('-p')  
parser.add_argument('-l')
parser.add_argument('-i')  

subprocess.run("curl" "-s" "http://whatismyip.akamai.com/")

args = parser.parse_args()
print(args)


test = subprocess.run(["ssh", "-i", args.i, "-l", args.l, "-p", args.p, args.a, "build", "test", "-s"]) 

# print("TEST\n" + test)
