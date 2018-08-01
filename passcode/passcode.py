import subprocess
import sys

proc = subprocess.Popen(["./passcode"], stdin=subprocess.PIPE)

proc.stdin.write("hi")
proc.stdin.close()

