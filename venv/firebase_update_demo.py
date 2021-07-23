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

#Updating a single entry in the database
#db.child("Branch").child("Engineering").child("Employees")\
#    .update({"name":"Manju","age":26,"address":["Vivekanandanagar","Mysore"]})

#Updating multiple different entries in the DB
data = {"MfETJfLwPtDyxxdUwUY/users/0":{"address":["Vijayanagar","Mysore"]},
        "Bharath":{"age":30}}
db.update(data)