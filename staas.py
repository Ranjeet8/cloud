#!/usr/bin/python

import os,cgitb,cgi,commands,time,sys

cgitb.enable()

print "content-type:text/html"
print ""

data=cgi.FieldStorage()

# recv from staas.html

hdd=data.getvalue('storage')

if hdd == 'object' :
	print "<b><i>Nice Choice</i></b><b>"
	print "<a href='http://127.0.0.1/cloudr/staas_object.html'>"
	print "<br>"
	print "<br>"		
	print "<i>Click to get Object Storage</i>"
	print "</a>"

elif hdd== 'block' :
	print "<b><i>Nice choice</i></b>"
	print "<a href='http://127.0.0.1/cloudr/staas_block.html'>"
	print "<br>"
	print "<br>"	
	print "<i>Click to get Block Storage</i>"
	print "</a>"
