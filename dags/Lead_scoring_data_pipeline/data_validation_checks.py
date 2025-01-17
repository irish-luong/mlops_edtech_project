"""
Import necessary modules
############################################################################## 
"""
import os
import sqlite3
import pandas as pd

from Lead_scoring_data_pipeline import constants, schema


###############################################################################
# Define function to validate raw data's schema
############################################################################### 

def raw_data_schema_check():
    '''
    This function check if all the columns mentioned in schema.py are present in
    leadscoring.csv file or not.

   
    INPUTS
        DATA_DIRECTORY : path of the directory where 'leadscoring.csv' 
                        file is present
        raw_data_schema : schema of raw data in the form oa list/tuple as present 
                          in 'schema.py'

    OUTPUT
        If the schema is in line then prints 
        'Raw datas schema is in line with the schema present in schema.py' 
        else prints
        'Raw datas schema is NOT in line with the schema present in schema.py'

    
    SAMPLE USAGE
        raw_data_schema_check
    '''
    try:
         leadscoring_file_path = os.path.join(constants.DATA_DIRECTORY, constants.FILE_LEADSCORING)
         print("Load data from ", leadscoring_file_path)
         df = pd.read_csv(leadscoring_file_path, index_col=[0])    
         if sorted(schema.raw_data_schema) == sorted(df.columns) :
             print('Raw datas schema is in line with the schema present in schema.py')
         else :
             print('Raw datas schema is NOT in line with the schema present in schema.py')
    except Exception as e:
         print (f'Exception thrown in raw_data_schema_check : {e}')
   

###############################################################################
# Define function to validate model's input schema
############################################################################### 

def model_input_schema_check():
    '''
    This function check if all the columns mentioned in model_input_schema in 
    schema.py are present in table named in 'model_input' in db file.

   
    INPUTS
        DB_FILE_NAME : Name of the database file
        DB_PATH : path where the db file should be present
        model_input_schema : schema of models input data in the form oa list/tuple
                          present as in 'schema.py'

    OUTPUT
        If the schema is in line then prints 
        'Models input schema is in line with the schema present in schema.py'
        else prints
        'Models input schema is NOT in line with the schema present in schema.py'
    
    SAMPLE USAGE
        raw_data_schema_check
    '''
    try:
        db_path = os.path.join(constants.DB_PATH, constants.DB_FILE_NAME)
        print("SQLite database path ", db_path)
        cnx = sqlite3.connect(db_path)
        df = pd.read_sql('select * from model_input', cnx)          
        cnx.close()
        if sorted(schema.model_input_schema) == sorted(df.columns) :
            print('Models input schema is in line with the schema present in schema.py')
        else :
            print( 'Models input schema is NOT in line with the schema present in schema.py')
    except Exception as e:
        print (f'Exception thrown in model_input_schema_check : {e}')
        raise e
    

    
    
