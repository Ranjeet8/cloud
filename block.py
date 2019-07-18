#!/usr/bin/python

import cgi
import commands
import cgitb

cgitb.enable()

print "content-type:text/html"
print   "\n"

s=cgi.FieldStorage()

name=s.getvalue('name')
size=s.getvalue('size')

#print  "lvcreate --name  {}  --size  {}  vg".format(name,size)
a=commands.getstatusoutput("sudo lvcreate --name "+name+" --size "+size+"  demo")
print a
e=commands.getstatusoutput("sudo touch /etc/tgt/targets.conf".format(name))
print e
k=commands.getstatusoutput("sudo chmod 777 /etc/tgt/targets.conf".format(name))
print k
g=open("/etc/tgt/targets.conf",mode='w')
g.write("<target {}>\n ".format(name))
g.write("               backing-store /dev/demo/{} \n".format(name))
g.write("</target>")
g.close()
b=commands.getstatusoutput("sudo systemctl restart tgtd")
print b
f=open("/var/www/cgi-bin/dev.py",mode='w')
f.write("#!/usr/bin/python \n")
f.write("import commands \n")
f.write("print commands.getstatusoutput('sudo yum install iscsi-initiator-utils')\n")
f.write("print commands.getstatusoutput('sudo man iscsiadm')\n")
f.write("print commands.getstatusoutput('sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1 --discover')\n")
f.write("print commands.getstatusoutput('sudo iscsiadm --mode node --targetname {} --portal 192.168.122.1 --login')\n".format(name))
f.write("print commands.getstatusoutput('python /root/dev.py')\n")
f.write("raw_input()\n")
f.close()
commands.getstatusoutput("sudo tar -cvf gf.tar dev.py ")
commands.getstatusoutput("sudo mv gf.tar /var/www/html")
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/gf.tar\">\n" 

                                                                                                      
