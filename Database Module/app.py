from flask import Flask, render_template

from Module.service import Service

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
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    services= Service.objects(gender=gender, yob__lte = '1998', height__gte = "160", address__contains = "Hanoi")
    return render_template('search.html', all_services= services)




if __name__ == '__main__':
  app.run(debug=True)
