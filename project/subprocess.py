import subprocess
subprocess.call(["g++", "output.c"])
tmp=subprocess.call("./a.out")
print ("printing result")
print (tmp)
