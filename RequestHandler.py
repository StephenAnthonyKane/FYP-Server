#!/usr/bin/python

from GetHandler import GetHandler
from PostHandler import PostHandler
from FileLogger import FileLogger
import json
import cgi
import cgitb
import os

cgitb.enable()
arguments = cgi.FieldStorage()

requestMethod = os.environ['REQUEST_METHOD']
#requestMethod = 'GET'

#print("Content-Type: text/html\r\n\r\n")
#print("<html><body>")
#print('<p>'+requestMethod+'</p>')

print("Content-type: application/json")
print

if(requestMethod == 'GET'):
   getHandler = GetHandler()
   result = getHandler.Handle(arguments)
   print(json.dumps(result))

if(requestMethod == 'POST'):
   postHandler = PostHandler()
   postHandler.Handle(arguments)
   print('{ "Success":"true"}')

#print("</body></html>")