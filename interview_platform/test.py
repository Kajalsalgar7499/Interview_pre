from database.connection import users_collection

data = {
    "name": "Kajal",
    "email": "kajal@gmail.com",
    "password": "123456"
}

result = users_collection.insert_one(data)

print(result.inserted_id)