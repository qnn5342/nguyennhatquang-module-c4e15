import mlab
from Module.service import Service
mlab.connect()

##1 way
# import bson

# get_id= Service.objects.get(id=bson.objectid.ObjectId( '5a955cfcdec2186b4c3e559b'))
#


all_services = Service.objects()

##Finding ID
get_id = Service.objects.get(id= '5a955cfcdec2186b4c3e559b')

print(get_id.to_mongo())

##Deleting ID
get_id.delete()
print(get_id.to_mongo())
