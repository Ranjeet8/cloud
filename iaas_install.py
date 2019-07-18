#!/usr/bin/python

import os,cgi,commands,time,sys,cgitb,random

cgitb.enable()

print "content-type:text/html"
print ""

# recv data from install_os.html

recv=cgi.FieldStorage()
name=recv.getvalue('name')
cpu=recv.getvalue('cpu')
ram=recv.getvalue('ram')
hdd=recv.getvalue('hdd')


web_port=random.randint(5900,7000)

os_port=random.randint(5900,7000)

ins=commands.getstatusoutput('sudo virt-install --graphics vnc,listen=0.0.0.0,port={} --cdrom /var/lib/libvirt/images/generic-31.qcow2 --name {} --ram {} --vcpu {} --disk /dev/demo/test'.format(os_port,name,ram,cpu))
print ins

u=commands.getstatusoutput("websockify -D --web=/usr/share/novnc {} 0.0.0.0:{}".format(web_port,os_port))

