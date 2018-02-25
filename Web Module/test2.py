username = input("Input username: ")
user_list= { "Quang Nguyen":{ "Name": "Nguyen Nhat Quang"
, "Age":"21", "Gender":"Male", "Interest":"Football",
},
"Thu Nguyen":{"Name": "Nguyen Thi Thu"
, "Age":"37", "Gender":"Female", "Interest":"Play",
},
"Quy Nguyen": { "Name": "Dinh Quy"
, "Age":"20", "Gender":"Male", "Interest":"Laughing",
},
"tuananhkid":{ "Name": "Nguyen Tuan Anh"
, "Age":"19", "Gender":"Male", "Interest":"No interest",
},
}
display_list = []
error_message= "No data was found"
if username in user_list:
  display_list.append(user_list[username])
else:
  display_list.append(error_message)

print(display_list)
