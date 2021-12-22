import pandas as pd
import pyodbc as pyc

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
    data_frame = pd.read_sql_query(sql_query_input, con=cnxn)

    return data_frame