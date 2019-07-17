#!/usr/bin/python

import os,cgitb,cgi,commands,time,sys

cgitb.enable()

print "content-type:text/html"
print ""

# Recv Choice from choice.html.
data=cgi.FieldStorage()
choice=data.getvalue('get')


if choice == 'saas' :
	print "<b><i>Software as a Service</i></b>"
	print "<a href='http://127.0.0.1/cloudr/services.html'>"
	print "<br>"
	print "<br>"
	print "<i>Click to get Services<i>"
	print "</a>"

elif choice == 'staas' :
	print "<b><i>Storage as a Service</i></b>"
	print "<a href='http://127.0.0.1/cloudr/staas.html'>"
	print "<br>"
	print "<br>"
	print "<i>Click to get Storage<i>"
	print "</a>"

elif choice == 'iaas' :
	print "<b><i>Infrastructure as a Service</i></b>"
	print "<a href='http://127.0.0.1/cloudr/iaas.html'>"
	print "<br>"
	print "<br>"
	print "<i>Click to get Infrastructure<i>"
	print "</a>"

elif choice == 'paas' :
	print "<b><i>Plateform as a Service</i></b>"
	print "<a href='http://127.0.0.1/cloudr/paas.html'>"
	print "<br>"
	print "<br>"
	print "<i>Click to get Plateform<i>"
	print "</a>"
else :
	print "Wrong input"
	print "<a href='http://127.0.0.1/cloudr/services.html'>"
	print "<br>"
	print "<br>"
	print "Try again"
	print "</a>"
