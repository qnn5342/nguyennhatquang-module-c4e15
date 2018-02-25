username = "Quang Nguyen2"
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
    else:
        display_list.append(error_message)
        break
print(display_list)
