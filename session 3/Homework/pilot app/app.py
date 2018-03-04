from flask import Flask, render_template, redirect, url_for, request

from Module.service import Service
from random_data import *
import mlab

mlab.connect()


app = Flask(__name__)

# create collection
#
# service = Service(name='Hera Kieu Anh', yob= 1998, gender=0, height= 160, phone ='091234567', address='Hanoi', status=True)
#
# service.save()


@app.route('/')
def index():
    services= Service.objects
    return render_template('index2.html', all_services= services)

@app.route('/detail/<service_id>')
def detail(service_id):
    services_to_show= Service.objects.with_id(service_id)
    return render_template('detail.html', services_to_show= services_to_show)


@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services= services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        return "Not found"
    service_to_delete.delete()
    return redirect(url_for('admin'))

@app.route('/new_service', methods = ['GET','POST'])
def created():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        image = form['image']
        new_service = Service(name=name, yob = yob, phone = phone, address = "Ha Noi", status = True, gender = 1, height = 164, measurements= new_list(), description= char_list(), image = image)
        new_service.save()

        return "Saved"
        return redirect(url_for('admin'))

@app.route('/update_service/<service_id>',methods = ['GET','POST'])
def update(service_id):
    id_to_find = service_id
    service_to_update= Service.objects().with_id(id_to_find)
    # search = Service.objects.with_id(id_to_find)
    if request.method == 'GET':
        return render_template('update_service.html', service_to_update = service_to_update)

    elif request.method == 'POST':
        print (service_to_update)
        if service_to_update is not None:
            form = request.form
            name = form['name']
            yob = form['yob']
            phone = form['phone']
            image = form['image']
            description = form['description']
            measurements = form['measurements']
            height = form['height']
            # return (name + str(yob)+ str(phone) + str(image) + str(description) + str(measurements))
            service_to_update.update(set__name= name,
            set__yob= yob,set__phone= phone, set__image= image, set__height = height,set__description= description,set__measurements=measurements)
            service_to_update.reload()
            print(service_to_update.to_mongo())
            # return "Updated!!"
            return redirect(url_for('admin'))

        else:
            return("Not found")




if __name__ == '__main__':
  app.run(debug=True)
