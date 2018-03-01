import mlab
from Module.service import Service

mlab.connect()

all_services = Service.objects()

first_service = all_services[0]
last_service = all_services[11]

print(first_service['name'])

print(last_service['name'])
