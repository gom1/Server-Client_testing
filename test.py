# import subprocess
# o = subprocess.Popen(["adb", "shell"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
# #for line in o:
# #print "I got",line
# print o.communicate("ls /")
# o.stdin.write("ls /")
# o.stdin.flush()
# print o.stdout.read()
# print o.readline();
# print o.communicate()

import os
ls = os.popen('ls').read()
