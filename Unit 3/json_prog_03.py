import requests
import json
import sqlite3

DB_FILE = './Unit 3/food_trucks.db'

def jprint(obj):
    # display formatted data only if retreval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))

    # if retrieval not success, dsiplay error number
    else:
        print(f"{obj.status_code} error in API call")

def create_table(filename, tablename, sqlcommand):
    # connect to database file (will create if non-existant)
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()
        
        # removes previous table and data
        cursor.execute(f"DROP TABLE IF EXISTS {tablename};")

        # create empty table
        cursor.execute(sqlcommand)

### MAIN PROGRAM ###

# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

#jprint(trucks_data)

# --- create database tables ---
# truck table
create_truck_table = """
                        CREATE TABLE Trucks (
                            truck_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            category TEXT NOT NULL,
                            website TEXT);
                        """

create_table(DB_FILE,"Trucks",create_truck_table)