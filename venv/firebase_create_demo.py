import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAVNufq7JxzS8NpSWpC1NbtU4e9jYEDZq8",
    "authDomain": "pyrebaserealtimedbdemo-53bdd.firebaseapp.com",
    "databaseURL": "https://pyrebaserealtimedbdemo-53bdd-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "pyrebaserealtimedbdemo-53bdd",
    "storageBucket": "pyrebaserealtimedbdemo-53bdd.appspot.com",
    "messagingSenderId": "105874355523",
    "appId": "1:105874355523:web:57e453bc7652b1ef006bf6",
    "measurementId": "G-E3W6RWNL7R"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#push data
#data={"users":[{"name":"Charan","age":20,"address":["Aravindanagar","Mysore"]},
               #  {"name":"Diksha","age":26,"address":["Dattagalli","Mysore"]}
               # ]}

#Pushing single document
data = {"name":"Charan","age":20,"address":["Aravindanagar","Mysore"]}
db.child("Branch").child("Engineering").child("Employees").set(data)
#db.push(data)

#create your own key
#data = {"name":"Bharath","age":25,"address":["Lakshmipuram","Mysore"]}
#db.child("Bharath").set(data)

