from medoo import Medoo




class Database:
    # For other arguments, please refer to the original connect function of each client.
    def __init__(self):        
        print("Init DB")        
        self.conn =  Medoo(dbtype='pgsql', user='postgres', password='zayro', host='localhost', database='enterprise', logging=True)
    
    def select(self, table, fields, where=None):
        field = ', '.join(fields)
        if where is not None and type(where) is dict:
            condition = where
                
        else:
            condition = None
            
        rs = self.conn.select(table, field, condition)
        print(rs.export('json'))
 


db = Database()
table = 'demo.prueba'
fields = ['phone', 'name']
db.select(table, fields, {'name': 'Nakia'})


