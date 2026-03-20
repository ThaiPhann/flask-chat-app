from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://test:test@chatapp.s0yqt9e.mongodb.net/?appName=ChatApp")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")

def save_user(username, email, password):
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({'_id': username,
                                 'email': email,
                                 'password': hashed_password})
    
save_user('Kyle','Kyle123@yopmail.com','12345678')