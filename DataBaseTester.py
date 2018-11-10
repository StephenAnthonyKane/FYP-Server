from PostHandler import PostHandler
from GetHandler import GetHandler
import json

getHandler = GetHandler()
postHandler = PostHandler()

x = { "UID": "123456", "URL": "www.test.com","TLM": "", "EID": "", }
newEntry = json.dumps(x)
postHandler.Handle(newEntry)

AllRecords = getHandler.Handle(21)
for x in AllRecords:
    print(x)
