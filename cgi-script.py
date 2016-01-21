#!/usr/bin/env python
import os,json,cgi

print "Content-type: text/html"
#print "Location: http://google.com"
print
print "<HTML><h1><BODY>Hello, world!</h1>"
print "<form method = 'post'><INPUT NAME = 'x'> </form>"

form = cgi.FieldStorage()

print "<P>X was:" +cgi.escape(str(form.getvalue('x')))
print "</BODY></HTML>"
