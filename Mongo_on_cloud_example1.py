import pymongo
import sys
from connect_to_mongo import connect_to_mongo

client = connect_to_mongo()

# use a database named "myDatabase"
db = client.myDatabase
print('Connection Established ', db)
# use a collection named "recipes"
my_collection = db["recipes"]

recipe_documents = [{ "name": "elotes", "ingredients": ["corn", "mayonnaise", "cotija cheese", "sour cream", "lime"], "prep_time": 35 },
                    { "name": "loco moco", "ingredients": ["ground beef", "butter", "onion", "egg", "bread bun", "mushrooms"], "prep_time": 54 },
                    { "name": "patatas bravas", "ingredients": ["potato", "tomato", "olive oil", "onion", "garlic", "paprika"], "prep_time": 80 },
                    { "name": "fried rice", "ingredients": ["rice", "soy sauce", "egg", "onion", "pea", "carrot", "sesame oil"], "prep_time": 40 },
                    { "name": "dosa", "ingredients": ["rice", "dhall", "oil", "ghee"], "prep_time": 10 },
                    { "name": "biriyani", "ingredients": ["meat", "rice", "yogurt", "onion", "butter", "spices", "tomato"], "prep_time": 120 }
                    ]

# drop the collection in case it already exists
try:
  my_collection.drop()  

# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("Error occured while dropping the recipe collection")
  sys.exit(1)

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(recipe_documents)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("Error occured while inserting multiple documents into the recipe collection")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("I inserted %x documents." %(inserted_count))

  print("\n")

my_collection = db["chefs"]

chef_documents = [{ "name": "peter james", "age": 45, "cusine": ["german", "spanish"], "rating": 4 },
                    { "name": "anand prakash", "age": 55, "cusine": ["indian", "italian"], "rating": 5 },
                    { "name": "ram sam", "age": 32, "cusine": ["indian", "malay"], "rating": 3 },
                    { "name": "gordon green", "age": 62, "cusine": ["american", "turkish"], "rating": 4 }
                    ]

# drop the collection in case it already exists
try:
  my_collection.drop()  

# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("Error occured while dropping chef collection")
  sys.exit(1)

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(chef_documents)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An error occured while inserting multiple documents to the chef collection")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("I inserted %x documents." %(inserted_count))

  print("\n")

chef_document = { "name": "gagan singh", "age": 45, "cusine": ["punjabi", "south indian"], "rating": 2 }
# INSERT DOCUMENT
#
# You can insert individual documents using collection.insert_one().

try: 
 result = my_collection.insert_one(chef_document)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An Error occured while writing a new document to the chef collection ")
  sys.exit(1)
else:
  print("Inserted 1 record successfully")

print("\n")

my_collection = db["rating"]

chef_ratings = [{ "rating": 1, "explanation": "Starter"},
                  { "rating": 2, "explanation": "Junior"},
                  { "rating": 3, "explanation": "Senior"},
                  { "rating": 4, "explanation": "Expert"},
                  { "rating": 5, "explanation": "Master"}
                    ]

# drop the collection in case it already exists
try:
  my_collection.drop()  

# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("Error occured while dropping rating collection")
  sys.exit(1)

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(chef_ratings)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An error occured while inserting multiple documents to the chef collection")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("I inserted %x documents." %(inserted_count))

  print("\n")
