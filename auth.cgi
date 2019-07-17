#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
user=x.getvalue('u')
password=x.getvalue('p')

if  user  ==  'root'  and  password  == 'mypass' :
	print  "authentication Done  redirecting to new page"


else  :
	print   "bad  authentication  details !!"
	print  "<meta http-equiv='refresh' content='2;url=http://127.0.0.1/cloudr/index.html'/>"
