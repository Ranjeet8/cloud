#!/usr/bin/python

import os,cgi,commands

print "content-type:text/html"
print ""

recv=cgi.FieldStorage()
x=recv.getvalue('pass')
print x
if x == 'py':
	print "Nice choice"
	commands.getoutput('sudo docker start d19334213cde')
	ip=commands.getoutput('sudo docker exec -i d19334213cde hostname -I')
	print ip
	print "<a href='https://127.0.0.1:4200'>"
	print "click here and user code1 and password 123"
	print "</a>"
"""
elif x == 'pl':
	print "Nice choice"'<br>'
	ip=commands.getoutput('sudo docker -exec -it d19334213cde  hostname -i')
	print ip
	print "<a href='http://'+ip+':4200'>"
	print "click here and user code1 and password 123"
	print "</a>"

elif x == 'rb':
	print "Nice choice"
	ip=commands.getoutput('sudo docker -exec -it d19334213cde  hostname -i')
	print ip
	print "<a href='http://'+ip+':4200'>"
	print "click here and user code1 and password 123"
	print "</a>"


elif x == 'go':
	print "Nice choice"
	ip=commands.getoutput('sudo docker -exec -it d19334213cde hostname -i')
	print ip
	print "<a href='http://'+ip+':4200'>"
	print "click here and user code1 and password 123"
	print "</a>"

"""
