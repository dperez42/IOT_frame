# pip3 install psycopg2
# https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/

import psycopg2
import numpy as np
import time
# seed the pseudorandom number generator
from random import seed
from random import random
import sys

connection = psycopg2.connect(database="db",
                        host="localhost",
                        user="user",
                        password="password",
                        port="5432")

cursor = connection.cursor()

interval = 1                # intervalo de lectura
devices = int(sys.argv[1])  # número de sensores
seed(1)                     # seed random number generator
facts_table = 'sensors_facts'
last_table = "test"

tim = time.time()+interval
while 1:
    if (time.time()>tim+interval):
        i = 1
        print("sending")
        while i <= devices:
            record = (str(i), int(round(4 * random()*10,0)), time.time())
            print(record)
            r = np.array(record)

            # insert data en tabla de facts
            #sql_insert_query = """INSERT INTO test (ID, DATA) VALUES (%s,%s)"""
            #cursor.execute(sql_insert_query, record)
            #connection.commit()

            # update last data table
            sql_select_query = """SELECT ID FROM """ + last_table +""" where ID = %s"""
            cursor.execute(sql_select_query, (r[0],))
            result = cursor.fetchall()
            a = np.array(result)
            #print("nº resultados: ",a.size)

            if a.size == 0:
                sql_insert_query = """INSERT INTO """ + last_table +""" (ID, DATA, TIMESTAMP) VALUES (%s,%s,%s)"""
                cursor.execute(sql_insert_query, record)
                connection.commit()
                #print("insert")
            else:
            # Update single record now
                sql_update_query = """UPDATE """ + last_table +""" SET data = %s, timestamp = %s where id = %s"""
                cursor.execute(sql_update_query, (r[1],r[2],r[0]))
                connection.commit()
                #print("update")

            #query = "SELECT * FROM test"
            #cursor.execute(query)
            #response = cursor.fetchall()
            #print(response)

            #print(cursor.fetchone()) 
            i = i +1
        tim = time.time()