#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "content-type:text/html"
print   ""

data=cgi.FieldStorage()
#  recv software name from  services.html    
software=data.getvalue('saas')

if  software   ==   'firefox' :
	print   "wait for  firefox  "
	print  "<a href='http://127.0.0.1/cgi-bin/firefox.py'>"
	print   "click to get  firefox "
	print    "</a>"
	
elif  software  ==   'gedit' :
	print   "wait for  texteditor  "
	print  "<a href='http://127.0.0.1/gedit.sh'>"
	print   "click to get  gedit "
	print   "</a>"

elif  software  ==   'vlc' :
	print   "wait for  media player  "

elif  software  ==   'calc' :
	print   "wait for  calcccc  "
else :
	print "Wrong Input"
	execfile('servicess.py')

