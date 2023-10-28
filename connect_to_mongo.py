from pymongo import MongoClient, errors
from sys import exit

# Replace the placeholder data with your Atlas connection string in your data file. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.

# If Mongo is locally installed then use the below
# client = MongoClient('localhost', 27017)

def connect_to_mongo():
    fp = open('d:/pythondata/mongoconnectionstring.txt','r')
    connection_string = fp.read()
    fp.close()
    try:
      client = MongoClient(connection_string)
  
# return a friendly error if a URI error is thrown 
    except errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        exit(1)

    return client