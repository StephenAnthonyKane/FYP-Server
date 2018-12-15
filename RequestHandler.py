#!/usr/bin/python

from GetHandler import GetHandler
from PostHandler import PostHandler
import time
import cgi
import cgitb
import os

cgitb.enable()
arguments = cgi.FieldStorage()
requestMethod = os.environ['REQUEST_METHOD']

print("Content-Type: text/html\r\n\r\n")
print("<html><body>")
print('<p>'+requestMethod+'</p>')

if(requestMethod == 'GET'):
   print('GET request recived')
   getHandler = GetHandler()
   t = getHandler.Handle(arguments)
   print(t)

if(requestMethod == 'POST'):
   print('POST request recived')
   postHandler = PostHandler()
   postHandler.Handle(arguments)

print("</body></html>")

