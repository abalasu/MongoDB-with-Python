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

# DELETE DOCUMENTS
#
# As with other CRUD methods, you can delete a single document 
# or all documents that match a specified filter. To delete all 
# of the documents in a collection, pass an empty filter to 
# the delete_many() method. In this example, we'll delete two of 
# the recipes.
#
# The query filter passed to delete_many uses $or to look for documents
# in which the "name" field is either "elotes" or "fried rice".
print('Delete One')
my_result = my_collection.delete_one({{ "name": "dosa" }})
print("I deleted %x records." %(my_result.deleted_count))
print("\n")


# DELETE DOCUMENTS
#
# As with other CRUD methods, you can delete a single document 
# or all documents that match a specified filter. To delete all 
# of the documents in a collection, pass an empty filter to 
# the delete_many() method. In this example, we'll delete two of 
# the recipes.
#
# The query filter passed to delete_many uses $or to look for documents
# in which the "name" field is either "elotes" or "fried rice".
print('Delete Many')
my_result = my_collection.delete_many({ "$or": [{ "name": "elotes" }, { "name": "fried rice" }]})
print("I deleted %x records." %(my_result.deleted_count))
print("\n")
