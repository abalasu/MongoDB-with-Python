import pymongo
import sys
from connect_to_mongo import connect_to_mongo

client = connect_to_mongo()

# use a database named "myDatabase"
db = client.myDatabase
print('Connection Established ', db)
# use a collection named "recipes"
my_collection = db["recipes"]
print(my_collection)

# UPDATE A DOCUMENT
#
# You can update a single document or multiple documents in a single call.
# 
# Here we update the prep_time value on the document we just found.
#
# Note the 'new=True' option: if omitted, find_one_and_update returns the
# original document instead of the updated one.
print('Update a document')
my_doc = my_collection.find_one_and_update({"ingredients": "potato"}, {"$set": { "prep_time": 72 }}, new=True)
if my_doc is not None:
  print("Here's the updated recipe:")
  print(my_doc)
else:
  print("I didn't find any recipes that contain 'potato' as an ingredient.")
print("\n")