#!/usr/bin/python

import os,cgitb,cgi,commands,sys

cgitb.enable()

print "content-type:text/html"
print ""

# recv from staas_object.html

recv=cgi.FieldStorage()
n=recv.getvalue('storage')
sz=recv.getvalue('size')

print commands.getstatusoutput('sudo lvcreate --name '+n+' --size '+sz+' demo')
print commands.getstatusoutput('sudo mkfs.xfs /dev/demo/'+n)
print commands.getstatusoutput('sudo mkdir /mnt/'+n)


commands.getstatusoutput('sudo mount /dev/demo/'+n+' /mnt/'+n)

print commands.getstatusoutput("echo '/mnt/{}    *(rw,no_root_squash)'  >>/etc/exports ".format(n))

print commands.getstatusoutput("sudo exportfs -ar")
	
print commands.getstatusoutput("sudo echo 'mkdir /media/{}'  >>nfs.sh    ".format(n))
print commands.getstatusoutput("sudo echo 'mount 192.168.122.1:/mnt/{}' /media/{} >>nfs.sh    ".format(n,n))
print commands.getstatusoutput("sudo chmod +x nfs.sh")
print commands.getstatusoutput("sudo tar cvf   ../html/nfs.tar     nfs.sh")

print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1:/nfs.tar'>"






