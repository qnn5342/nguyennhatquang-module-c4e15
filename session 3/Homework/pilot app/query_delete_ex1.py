import mlab
from Module.service import Service
from flask import request

mlab.connect()

##ex1
all_services = Service.objects

print(all_services)
#
all_services.delete()
print (get_id)
print (Service.objects.with_id(service_id))















# all_services = Service.objects()
#
# first_service = all_services[0]
# last_service = all_services[11]
#
# print(first_service['name'])
#
# print(last_service['name'])
# #
# print(find.to_mongo())
#
# if find is not None:
#     # find.delete()
#     find.update(set__status= True)
#     find.reload()
#     print(find.to_mongo())
# else:
#     print("Not found")
