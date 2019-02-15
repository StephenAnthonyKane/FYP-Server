from MongoDB import MongoDB

mongo = MongoDB('mongodb://localhost:27017/', "mydatabase")



data = { 'BeaconID' : "b9407f30-f5f8-466e-aff9-25556b57fe6d" , 'Xcord' : 245 , 'Ycord' : 25 }
mongo.SaveNewEntry('BeaconInformation', data)

data = { 'BeaconID' : "acfd065e-c3c0-11e3-9bbe-1a514932ac01" , 'Xcord' : 620 , 'Ycord' : 25 }
mongo.SaveNewEntry('BeaconInformation', data)

#data = { 'BeaconID' : uid , 'Xcord' : 245 , 'Ycord' : 470 }
#data = { 'BeaconID' : uid , 'Xcord' : 620 , 'Ycord' : 470 }