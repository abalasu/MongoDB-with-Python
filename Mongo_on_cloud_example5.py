import pymongo
from connect_to_mongo import connect_to_mongo

client = connect_to_mongo()

# use a database named "myDatabase"
db = client.myDatabase
print('Connection Established ', db)
# use a collection named "recipes"
my_collection = db["chefs"]
print(my_collection)

# Aggregate function with 1 stage - 
# Stage 1 - Groups records together based on rating and counts the rating for each group ($sum does the addition and 1 is a literal used, this gets
agg_result = my_collection.aggregate([
                                      {"$group" : {"_id":"$rating",
                                                   "Count": {"$sum": 1}}}                          
                                      ])
print('group')                                                   
for i in agg_result:
    print(i)

# Aggregate function with 1 stage - 
# Stage 1 - Match acts like a filter. Here documents having a rating of 4 and above are extracted
agg_result = my_collection.aggregate([
                                      {"$match" : {"rating": {"$gte":4}}}                          
                                      ])
print('match')                                                   
for i in agg_result:
    print(i)

# Aggregate function with 1 stage 
# Stage 1 - addFields - add's new fields to the output
agg_result = my_collection.aggregate([
                                      {"$addFields" : 
                                       {"avg-rating": 3.5}
                                      }                          
                                      ])
print('addFields')                                                   
for i in agg_result:
    print(i)

# Aggregate function with many stages - 
# Stage 1 - Projects only the columns age and rating. Any column with a 0 will be dropped to the next stage
# Stage 2 - Groups records together based on rating and finds the average age for each of the ratings
# Stage 3 - Sorts the output of Stage 1 (1 - ascending, -1 - descending)
# Stage 4 - Limits only the first 2 records to the output
agg_result = my_collection.aggregate([
                                      {"$project": {"age":1, "rating":1}},
                                      {"$group" : {"_id":"$rating",
                                                   "avg_age": {"$avg": "$age"}}},
                                      {"$sort" : {"avg_age": -1}},
                                      {"$limit": 2}
                                      ])
print('Aggregated functions 1')                                                   
for i in agg_result:
    print(i)

# Aggregate function with many stages - 
# Stage 1 - Projects only the columns age and rating. Any column with a 0 will be dropped to the next stage
# Stage 2 - Counts the number of records from Stage 1
agg_result = my_collection.aggregate([
                                      {"$project": {"age":1, "rating":1}},
                                      {"$count" : "Total_Doc_Cnt"}
                                      ])
print('Aggregated functions 2')                                                   
for i in agg_result:
    print(i)
