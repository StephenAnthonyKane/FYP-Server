from PostHandler import PostHandler
from GetHandler import GetHandler
import json

getHandler = GetHandler()
postHandler = PostHandler()


mylist = [
    { "UID": "1", "RSS": "1"},
    { "UID": "2", "RSS": "2"},
    { "UID": "3", "RSS": "3"},
    { "UID": "4", "RSS": "4"},
    { "UID": "5", "RSS": "5"},
    { "UID": "6", "RSS": "6"},
    { "UID": "7", "RSS": "7"}
]
jarray=  json.dumps(mylist)
jobj= {"Beacons": jarray}

newEnteries = json.dumps(jobj)

postHandler.Handle(jobj)

AllRecords = getHandler.Handle('UID=1')
print(AllRecords)
