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

# FIND All DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 
print('Find All')
result = my_collection.find()
if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")  
else:
  print("No documents found.")

print("\n")

# FIND Many DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 
print('Find Many in Recipe')
result = my_collection.find({"ingredients": "egg"})

if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")  
else:
  print("No documents found.")

print("\n")

# We can also find a single document. Let's find a document
# that has the string "potato" in the ingredients list.
print('Find One')
my_doc = my_collection.find_one({"ingredients": "dhall"})

if my_doc is not None:
  print("A recipe which uses dhall:")
  print(my_doc)
else:
  print("I didn't find any recipes that contain 'dhall' as an ingredient.")
print("\n")

# We can also multiple documents using the $ conditions - here rating is 4 and above and age is 50 and above

my_collection = db["chefs"]

print('Find Many in Chef')
result = my_collection.find({"rating": {"$gte":4}, "age":{"$gte":50}})

if result:    
  for doc in result:
    my_name = doc['name']
    my_cusine_count = len(doc['cusine'])
    my_age = doc['age']
    my_rating = doc['rating']
    print('Chef', my_name, " aged ", my_age, " prepares ", my_cusine_count, " cusines and is rated ", my_rating, " stars.")
else:
  print("No documents found.")

print("\n")

# We can also multiple documents using the $ conditions - here rating is 5 and above or the age is above 50

my_collection = db["chefs"]
print('Find Many in Recipes')

result = my_collection.find({"$or": [{"rating": {"$gte":5}}, {"age":{"$gte":40}}]})
if result:
  for doc in result:
    my_name = doc['name']
    my_cusine_count = len(doc['cusine'])
    my_age = doc['age']
    my_rating = doc['rating']
    print('Chef', my_name, " aged ", my_age, " prepares ", my_cusine_count, " cusines and is rated ", my_rating, " stars.")
else:
  print("No documents found.")

print("\n")

# Querying using the $in operator

print('Find Many in Recipes')
my_collection = db["recipes"]
result = my_collection.find({"ingredients": {"$in": ['rice', 'dhall', 'olive oil']}})
if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")
    print('And the ingredients are ')
    for ing in doc['ingredients']:
      print(ing)
else:
  print("No documents found.")

print("\n")

# Querying using the $nin (Not In) operator

print('Find Many in Recipes')
my_collection = db["recipes"]
result = my_collection.find({"ingredients": {"$nin": ['rice', 'dhall', 'olive oil']}})
if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")
    print('And the ingredients are ')
    for ing in doc['ingredients']:
      print(ing)
else:
  print("No documents found.")

print("\n")

# Querying Arrays using [] to pull documents with a complete match

print('Find Recipes with specific ingredients ')
my_collection = db["recipes"]
result = my_collection.find({"ingredients": ["rice", "dhall", "oil", "ghee"]})
if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")
    print('And the ingredients are ')
    for ing in doc['ingredients']:
      print(ing)
else:
  print("No documents found.")

print("\n")

# Querying Arrays using $all to pull documents where ingredients are both rice and oil

print('Find Recipes with specific ingredients ')
my_collection = db["recipes"]
result = my_collection.find({"ingredients": {"$all": ["rice", "oil"]}})
if result:    
  for doc in result:
    my_recipe = doc['name']
    my_ingredient_count = len(doc['ingredients'])
    my_prep_time = doc['prep_time']
    print(my_recipe, " has ", my_ingredient_count, " ingredients and takes ", my_prep_time, " minutes to make.")
    print('And the ingredients are ')
    for ing in doc['ingredients']:
      print(ing)
else:
  print("No documents found.")

print("\n")

