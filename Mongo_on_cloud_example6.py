import pymongo
from connect_to_mongo import connect_to_mongo

client = connect_to_mongo()

# use a database named "myDatabase"
db = client.myDatabase
print('Connection Established ', db)
# use a collection named "recipes"
my_chefs = db["chefs"]
my_ratings = db["rating"]
print(my_chefs)
print(my_ratings)
print('Chef Rating')
x = my_chefs.find()
for i in x:
    print(i['rating'])
print('Rating Master')    
x = my_ratings.find()
for i in x:
    print(i['rating'], i['explanation'])
# Left outer join using the $lookup function
# Aggregate function with many stages - 
# Stage 1 - Projects only the columns age and rating. Any column with a 0 will be dropped to the next stage
# Stage 2 - Groups records together based on rating and finds the average age for each of the ratings
# Stage 3 - Sorts the output of Stage 1 (1 - ascending, -1 - descending)
# Stage 4 - Limits only the first 2 records to the output
agg_result = my_chefs.aggregate([{'$lookup': {
                                    'from': "my_ratings",
                                    'localField': "rating",
                                    'foreignField': "rating",
                                    'as': "explanation" }
                                    }]
                                )
print('Aggregated functions 1')                                                   
for i in agg_result:
    print(i)