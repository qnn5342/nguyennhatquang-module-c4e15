import mlab
from Module.customer import Customer
mlab.connect()



all_customer = Customer.objects()

##Finding ID
get_id = Service.objects.get(id= '5a955cfcdec2186b4c3e559b')

print(get_id.to_mongo())

##Deleting ID
get_id.delete()
print(get_id.to_mongo())
