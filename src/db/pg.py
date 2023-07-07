import psycopg2


class Conectar:

    # init constructor about class Conectar
    def __init__(self): 
        self.connection = psycopg2.connect(
        host="localhost",
        database="enterprise",
        user="postgres",
        password="zayro"
        )


    # test connecto to database
    def testDb(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                database="enterprise",
                user="postgres",
                password="zayro"
            )

            print("connect to the database \n")

            cursor = self.connection.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cursor.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cursor.fetchone()
            print(db_version)
            cursor.close()
            self.connection.close()

        except (Exception, psycopg2.Error) as error:
            print("Error fetching data from PostgreSQL table", error)
            print("Unable to connect to the database")

    # can select row to database
    def select(self, sql, params):
        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (params))
            return cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            print("Error fetching data from PostgreSQL table", error)
            print("Unable to connect to the database")        
    
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed \n")
    
             
    def insert(self, sql, params):
        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (params))
            return cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            print("Error fetching data from PostgreSQL table", error)
            print("Unable to connect to the database")        
    
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed \n")
    
      
        
        

# Instance of Class
#p1 = Conectar()

#NOTE - Example Print beauty
# data = p1.select("select jsonb_pretty(row_to_json(t)::jsonb) FROM (select * from demo.prueba limit 10) t", [])

#NOTE - Example Print row_to_json
#data = p1.select("select (to_jsonb(t)::jsonb) FROM (select * from demo.prueba limit 10) t", [])


"""
my_data = {'created_at': '', 'id': '', 'author_id': '...', 'text': '...'}
cur.execute(
    "INSERT INTO tweets VALUES(%(created_at)s, %(id)s, %(author_id)s, %(text)s)",
    my_data
)
"""