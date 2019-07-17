#!/usr/bin/python

import  cgi,os,commands,time,sys,cgitb

cgitb.enable()

print   "content-type:text/html"
print   ""

#  this is  for  rec data from  cloudr
recv=cgi.FieldStorage()
user=recv.getvalue('u')
password=recv.getvalue('p')

if  user  ==  'root'  and  password  ==   'redhat1'  :
	print   "Login  Done"
	print   "<br/>"
	print   "<br/>"
	print   "<a href='http://127.0.0.1/cloudr/services.html'>"
	print   "click here  to  Access  CLoudr"
	print   "</a>"

else  :
	print  "bad Auth  "
	print  "<a  href='http://127.0.0.1/cloudr/'>"
	print   "Click here to try  again"
	print   "</a>"

