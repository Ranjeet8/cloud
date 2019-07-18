#!/usr/bin/python

import os,cgitb,cgi,commands,time,sys

cgitb.enable()

print "content-type:text/html"
print ""

# Recv Choice from choice.html.
data=cgi.FieldStorage()
os=data.getvalue('os')


if os == 'live_os' :
	print "Nice choice"
	print "<a href='http://127.0.0.1/cloudr/live_os.html'>"
	print "<br>"
	print "<br>"
	print "Click to get Live OS"
	print "</a>"

elif os == 'install_os' :
	print "Nice choice"
	print "<a href='http://127.0.0.1/cloudr/install_os.html'>"
	print "<br>"
	print "<br>"
	print "Click to get Install OS"
	print "</a>"

elif os == 'installed_os' :
	print "Nice choice"
	print "<a href='http://127.0.0.1/cloudr/input_os.html'>"
	print "<br>"
	print "<br>"
	print "Click to get Installed_os"
	print "</a>"

