from flask import Flask, render_template

from Module.customer import Customer

import mlab

mlab.connect()


app = Flask(__name__)


@app.route('/customer')
def search():
    customers= Customer.objects(gender=1, contacted= False)[0:10]
    return render_template('customer.html', all_customer= customers)




if __name__ == '__main__':
  app.run(debug=True)
