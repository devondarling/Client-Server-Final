from pymongo import MongoClient

from bson.objectid import ObjectId

class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):

        # Initializing the MongoClient. This helps to 

        # access the MongoDB databases and collections. 

        self.client = MongoClient('mongodb://%s:%s@localhost:51821/?authMechanism=DEFAULT&authSource=AAC' % (username,password))

        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create(self,data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            if self.database.animals.find(data):
                return True
            else: 
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Read method to implement the R in CRUD    
    def read(self,data):
        if data is not None:# if data isn't empty, query database for key value pair
            return self.database.animals.find(data,{"_id":False}) # Store query results (Cursor)
        else:
            #exception for empty parameter
            raise Exception("Nothing to save, because data parameter is empty")

# Read all method
    def readAll(self,data):
        #Returns find results. Removes _id for pandas
        return self.database.animals.find(data,{"_id":False})
    
# Update method to implement the U in CRUD    
    def update(self,data,updatedData):
        if data is not None: # if data isn't empty, update documents in database
            records_affected = self.database.animals.update_many(data,{"$set":updatedData})  # data and updatedData should be dictionaries 

            if records_affected is not None: #if data was inserted, return true, otherwise return false
                print(records_affected.raw_result)
                for document in self.database.animals.find(updatedData):
                    print(document)
            else: 
                raise Exception("Error With Update")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
# Delete method to implement the D in CRUD    
    def delete(self,data):
        if data is not None:
            results = self.database.animals.delete_one(data)
            if results is not None:
                print(results.raw_result)
            else:  
                raise Exception("Error With Delete")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
            