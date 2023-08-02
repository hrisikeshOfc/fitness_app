from src.constants import *
from src.mongodb_operations import DbOperations

class WorkoutData:

    def __init__(self):
        self.db = DbOperations(database_name=DATABASE_NAME)


    def insert_workout(self, records):
        self.db.insert_records(
            collection_name=WORKOUT_COLLECTION_NAME,
            records=records)
        
    def delete_workout(self,
                       video_id:str):
        self.db.delete_records(
            collection_name=WORKOUT_COLLECTION_NAME,
            query={"id": video_id}
        )

    def get_all_workouts(self):
        
        try:
            return self.db.find_all_records(
                collection_name=WORKOUT_COLLECTION_NAME)

        except Exception as e:
            print(e)

    def get_workout_today(self):
        records = self.db.find_all_records(collection_name=WORKOUT_COLLECTION_NAME)
        
        if records:
            return list(records)
        return None
    
    def insert_workout_today(
            self,
            workout_record:dict
    ):
        
        self.db.insert_records(
            collection_name=WORKOUT_TODAY_COLLECTION_NAME,
            records= workout_record
        )
    
    def update_workout_today(
            self,
            workout_record:dict,
            insert = False ):

        if insert:
                
            self.db.insert_records(
                collection_name=WORKOUT_TODAY_COLLECTION_NAME,
                records= workout_record
            )
           













    




        
    


    