from pony.orm import Database, db_session

 
db = Database()

# Set the database provider and connection details using a URL string


db.bind(provider='postgres', user='postgres', password='zayro', host='localhost', database='enterprise')

@db_session
def check_user():
    # Create the tables
    # db.generate_mapping(create_tables=True)
    # Execute a raw SELECT statement
    results = db.select("SELECT * FROM demo.prueba")

    # Print the results
    for row in results:
        print(row.name)
        
check_user()

