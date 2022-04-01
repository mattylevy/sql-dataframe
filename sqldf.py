import pandas as pd
import pyodbc as pyc

def get_sql(file_name):
  '''Opens sql file and returns query as a string'''
  file = open(file_name, 'r')
  sql_string = file.read()
  file.close()

def SQL_df(sql_query_input, driver, server_name):
  
    # SQL server connection
    conn_str = (
        r'Driver=%s;'
        r'Server=%s;'
        r'Database=Runtime;'
        r'Trusted_Connection=yes;'
        % (driver, server_name))
    
    cnxn = pyc.connect(conn_str)

    # SQL to DataFrame
    data_frame = pd.read_sql_query(sql_query_input, con=cnxn) # ,params = (x, y, n) use params argument to pass variables to SQL query

    return data_frame
