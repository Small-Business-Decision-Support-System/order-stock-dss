# database.py — handles the connection to our PostgreSQL database

import psycopg2  
# psycopg2 is the library that lets Python communicate with PostgreSQL

def get_connection():
    # this function creates a new connection to the database every time it's called
    conn = psycopg2.connect(
        host="localhost",        
        database="inventory_db",
        user="postgres",         
        password="your_password" 
        #Sedra will give me this
    )
    return conn  
    
