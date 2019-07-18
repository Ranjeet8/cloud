#!/usr/bin/python

import os,cgi,commands,time,sys,cgitb

cgitb.enable()

print "content-type:text/html"
print ""

# recv data from live_os.html

recv=cgi.FieldStorage()
name=recv.getvalue('name')
ram=recv.getvalue('ram')
cpu=recv.getvalue('cpu')
hdd=recv.getvalue('hdd')
port=recv.getvalue('port')

ins=commands.getstatusoutput('sudo virt-install --graphics vnc,listen=0.0.0.0,port={} --cdrom /var/lib/libvirt/images/kali-linux-2.0-amd64.iso --name {} --ram {} --vcpu {} --disk none'.format(port,name,ram,cpu))
print ins

u=commands.getstatusoutput("websockify -D --web=/usr/share/novnc 6086 0.0.0.0:{}".format(port))
