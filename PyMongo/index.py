from pymongo import MongoClientclient = MongoClient('mongodb://localhost:27017/')db = client['mydb']article = {"author": "mbr-sagor",           "about": "Introduction to MongoDB and Python",           "tags":               ["mongodb", "python", "pymongo"]}articles = db.articles# result = articles.insert_one(article)# print(f"First article key is: {result.inserted_id}")print(db.list_collection_names())# print(articles.find_one())for article in articles.find():    print(article)