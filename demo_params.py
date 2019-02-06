#!/usr/bin/python

# call using .../demo_params.py?nodeid=<nodeid>&data=<data> where <nodeid> and <data> are the required values

from GetHandler import GetHandler
from pymongo import MongoClient
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

getHandler = GetHandler()
#postHandler = PostHandler()

if(requestMethod == 'GET'):
   print('GET request recived')
   beaconUid = arguments['UID']
   getHandler.Handle(beaconUid)

if(requestMethod == 'POST'):
   print('POST request recived')
   beacons = arguments['beacons']
   postHandler.Handle(beacons)
   
#nodeid = "undefined"
#data = "undefined"


#print("Arguments are:<ul>")
#for i in arguments.keys():
#   print("<li>")
#   print(i)
#   print("=")
#   print(arguments[i].value)
#   print("</li>")
#   if i == "nodeid":
#      nodeid = arguments[i].value
#   elif i == "data":
#      data = arguments[i].value
#print("</ul>")

#client = MongoClient("localhost",27017)
#db = client.skane

#collection = db.testData
#now = time.time()

#row = { "timestamp":now, "nodeid":nodeid, "data":data }
#id = collection.insert_one(row).inserted_id
#print("Inserted id: ")
#print(id)

#print("<br>Contents of database are:<ul>")

#for doc in collection.find({}):
#   print("<li>")
#   print(doc)
#   print("</li>")
#print("</ul>")

print("</body></html>")

