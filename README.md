# cloud
deploying private cloud
#!/usr/bin/python

import os,cgi,commands,time,sys,cgitb

print "content-type:text/html"
print ""

# This is for recv data from cloudR
recv=cgi.FieldStorage()
user=recv.getvalue('u')
password=recv.getvalue('p')

if user == 'root' and password == 'redhat1' :
	print "<b><i>Access Granted</i><b>"
	print "<a href='http://192.168.122.1/cloudR/choice.html'>"
	print "<br>"
	print "<br>"
	print "<i>Click here to access cloudR<i>"
	print "</a>"
else :
	print "<b><i>Bad Authentication</i></b>"
	print "<a href='http://192.168.122.1/cloudR/ranjeet8.html'>"
	print "<br>"
	print "<br>"
	print "<i>Please login again</i>"
	print "</a>"
