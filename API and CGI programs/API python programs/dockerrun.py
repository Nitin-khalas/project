#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi



osname1 = cgi.FieldStorage()
osname = osname1.getvalue("x")
print("{}\n".format(osname))
cmd = "docker run -d -i -t --name {0} ubuntu:14.04".format(osname)

x = sp.getstatusoutput(cmd)
status = x[0]
output = x[1]

if status == 0:
   print("{0} :installed successfully".format(osname))
else:
   print("Installtion failed")
