import mlab
from Module.river import River

mlab.connect()

print("ALL RIVERS IN AFRICA:")
all_river_list = River.objects
river_list_print = []
for item in all_river_list:
    if item['continent'] =="Africa":
        river_list_print.append(item['name'])
print (river_list_print)

print("ALL RIVERS IN SOUTH AMERICA WITH LENGTH < 1000 km:")
river_list_print_condition = []
for item in all_river_list:
    if item['length'] < 1000 and item['continent'] == 'S. America':
        river_list_print_condition.append(item['name'])
print (river_list_print_condition)
#



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
