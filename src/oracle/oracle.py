import cx_Oracle

class MyOracle:
    
    def __init__(self, user, passwd, dsn):
        self.DB = cx_Oracle.connect(user, passwd, dsn)
#         print(type(self.DB))
        self.cursor = self.DB.cursor()
    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        self.DB.close()
    def get_DB_version(self):
        return self.DB.version
    
    def create_table(self, schema, tablename, columns_data_type):
        try:
            sql = 'CREATE TABLE ' + schema + '.' + tablename + ' (' + columns_data_type + ' )'
            self.cursor.execute(sql)
            return 'table create successfully'
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            print('Error Code:', error_obj.code)
            print('Error Message:', error_obj.message)
            raise
            
    def select_table(self, tablename):
        try:
            sql = 'SELECT table_name FROM user_tables WHERE table_name = \'' + tablename + '\''
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except cx_Oracle.DatabaseError as e:
            error_obj, = e.args
            print('Error Code:', error_obj.code)
            print('Error Message:', error_obj.message)
            raise
#             return error_obj.code