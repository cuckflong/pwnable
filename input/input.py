import subprocess
import sys
import os
import socket
import time

args = []
for i in range(100):
        args.append("a")
args[0] = "/home/input2/input"
args[65] = ""
args[66] = "\x20\x0a\x0d"
args[67] = "8000"
sin_r, sin_w = os.pipe()
ser_r, ser_w = os.pipe()

myenv = {}
myenv["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"
proc = subprocess.Popen(args, stdin=sin_r, stderr=ser_r, stdout=1, env=myenv)

os.write(sin_w, '\x00\x0a\x00\xff')
os.write(ser_w, '\x00\x0a\x02\xff')
os.close(sin_r)
os.close(sin_w)
os.close(ser_r)
os.close(ser_w)

f = open("\x0a", "w")
f.write("\x00\x00\x00\x00")
f.close()

time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))
s.send("\xde\xad\xbe\xef")
s.close()

proc.communicate()