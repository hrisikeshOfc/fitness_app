from pymongo import MongoClient
import certifi

import os 

ca = certifi.where()

class ConnectDB:
    def __init__(self,
                 database_name:str,
                 ):
        
        self.database_name = database_name

    def connect_database(self):
        mongodb_url = os.getenv("MONGO_DB_URL")
        client = MongoClient(mongodb_url, tlsCAFile=ca)
        return client[self.database_name]
    



class DbOperations(ConnectDB):

    def __init__(self, database_name: str):
        super().__init__(database_name)

        self.database = self.connect_database()

    def insert_records(self,
                       collection_name:str,
                       records:dict):
        try:
            self.database[collection_name].insert_one(records)
        except Exception as e:
            print(e)

    def delete_records(self,
                       collection_name:str,
                       query:dict):
        
        self.database[collection_name].delete_one(query)

    def find_all_records(self,
                         collection_name:str,
                         ):
        records = list(self.database[collection_name].find({}))
        if records:
            return records
        return None

    

        



            
    





        

