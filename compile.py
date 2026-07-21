import os
from tkinter import filedialog

print("\033c\033[47;30m\n give me the .js file to compile")
a=filedialog.askopenfile(title="give me the .js file to compile ? ",defaultextension="*.jx")
a=a.name
b=a.replace(".js","")
print("\033[47;30m\n")
c="cafebabe\n"
f1=open(a,"rb")
f=f1.read()
f1.close()
r=b''
counter=0
g=c.encode()
for ff in f:
   i=int(ff)
   ii=int(g[counter])
   fff=0xff & (i+ii)
   rr=bytearray([fff])
   r=r+rr
   counter=counter+1
   if counter>=len(g):
       counter=0

f1=open(b+".jscx","bw")
f1.write(r)
f1.close()