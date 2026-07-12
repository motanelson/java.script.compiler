import os
print("\033c\033[47;31m\ngive me a utf-64 .bin file to js ? ")
a=input().strip()
b=a.replace(".bin","")
c="hello\n"
f1=open(a,"r",encoding="utf-32")
f=f1.read()
f1.close()
c=c.encode("utf-32")
r=None
counter=0
g=c
r=''
counter1=0
for ff in f:
   if counter1==0:
       i=ord(ff)
       ii=int(g[counter])
       fff=0xffff & (i-ii)
       rr=chr(fff)
   
       r=r+rr
       
       counter=(counter+1) 
       if counter>=len(g):
           counter=0
   counter1=(counter1+1)  & 1
r=r[2:]

f1=open("/tmp/"+b+".js","w",encoding="utf-8")
f1.write(r)
f1.close()

os.system("xdg-open /tmp/"+b+".js")