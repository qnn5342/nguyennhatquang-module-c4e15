from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def showdetails(username):
    username = username
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
    },]
    display_list = []
    error_message= {"message":"No data was found"}
    for user in user_list:
        if user['username'] == username:
            display_list.append(user)
            break
    else:
            error_message['username'] = username
            display_list.append(error_message)
    print(display_list)
    return render_template('namedetail_list.html', articletitles=username, display_list= display_list, username = username)
    return display_list

if __name__ == '__main__':
  app.run(debug=True)
