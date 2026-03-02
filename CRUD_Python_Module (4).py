# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'aacpassword' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(
            f"mongodb://{username}:{password}@localhost:27017/aac"
        )
        self.database = self.client['aac']
        self.collection = self.database['animals']

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """
        Inserts a document into the animals collection

        :param data: dictionary of key/value pairs
        :return: True if successful, False otherwise
        """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print(f"Insert failed: {e}")
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        """
        Queries documents from the animals collection

        :param query: dictionary of search criteria
        :return: list of documents or empty list
        """
        results = []

        try:
            cursor = self.collection.find(query)
            for document in cursor:
                results.append(document)
        except PyMongoError as e:
            print(f"Read failed: {e}")

        return results
    
        # Create method to implement the U in CRUD.
    def update(self, query, new_values):
        """
        Updates document(s) in the animals collection

        :param query: dictionary of search criteria
        :param new_values: dictionary of fields to update
        :return: number of documents modified
        """
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except PyMongoError as e:
                print(f"Update failed: {e}")
                return 0
        else:
            return 0

    # Create method to implement the D in CRUD.
    def delete(self, query):
        """
        Deletes document(s) from the animals collection

        :param query: dictionary of search criteria
        :return: number of documents deleted
        """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"Delete failed: {e}")
                return 0
        else:
            return 0