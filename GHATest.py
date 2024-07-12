import argparse
import subprocess
import os

parser = argparse.ArgumentParser()

parser.add_argument('-a')    
parser.add_argument('-p')  
parser.add_argument('-l')
parser.add_argument('-i')  

args = parser.parse_args()
print(args)

print(os.system('ipconfig'))

test = subprocess.run(["ssh", "-i", args.i, "-l", args.l, "-p", args.p, args.a, "build", "test", "-s"]) 

# print("TEST\n" + test)
