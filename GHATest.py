import argparse
import subprocess
import os

parser = argparse.ArgumentParser()

parser.add_argument('-a')    
parser.add_argument('-p')  
parser.add_argument('-l') 

args = parser.parse_args()
print(args)


test = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=no", "-i", "id_rsa", "-l", args.l, "-p", args.p, args.a, "build", "test", "-s"]) 

# print("TEST\n" + test)
