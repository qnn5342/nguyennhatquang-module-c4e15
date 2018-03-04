import mlab
from Module.service import Service
from flask import request

mlab.connect()

##ex1
all_services = Service.objects

print(all_services)
#
# all_services.delete()
# print (get_id)
print (Service.objects.with_id(service_id))

id_to_find = '5a9bc417dec2183f6cb171f9'
service_to_update= Service.objects().with_id(id_to_find)
# search = Service.objects.with_id(id_to_find)
if request.method == 'GET':
    return render_template('update_service.html', service_to_update = service_to_update)

elif request.method == 'POST':
    form = request.form
    if service_to_update is not None:
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        image = form['image']
        description = form['description']
        measurements = form['measurements']
        print(name, yob, phone, image, description, measurements)
        # service_to_update.update(set__name= form['name'],
        # set__yob= form['yob'],set__phone= form['phone'], set__image= form['image'], set__description= form['description'],set__measurements=form['measurements'])
        # #
        service_to_update.reload()
        print(service_to_update.to_mongo())
        return("Updated ")
    else:
        return("Not found")















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
