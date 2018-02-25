from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def showdetails(username):
    User = username
    user_list= [{ "username": "Quang Nguyen", "Name": "Nguyen Nhat Quang"
    , "Age":"21", "Gender":"Male", "Interest":"Football",
    },
    { "username": "Thu Nguyen", "Name": "Nguyen Thi Thu"
    , "Age":"37", "Gender":"Female", "Interest":"Play",
    },
    { "username": "Quy Nguyen", "Name": "Dinh Quy"
    , "Age":"20", "Gender":"Male", "Interest":"Laughing",
    },
    { "username": "tuananhkid", "Name": "Nguyen Tuan Anh"
    , "Age":"19", "Gender":"Male", "Interest":"No interest",
    },
    ]
    return render_template('namedetail.html', articletitles=User, user_list=user_list)

if __name__ == '__main__':
  app.run(debug=True)
