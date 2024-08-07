import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-a')    
parser.add_argument('-p')  
parser.add_argument('-l') 

args = parser.parse_args()
print(args)

test = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=no", "-i", "~/.ssh/id_rsa", "-l", args.l, "-p", args.p, args.a, "build", "test", "-s"], capture_output=True, text=True) 

print(test.stdout)
if "FAIL" in test.stdout:
  sys.exit(1)
