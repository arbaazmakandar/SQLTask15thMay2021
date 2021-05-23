import mysql.connector as connection
import pandas as pandas
import csv

# #create database
mydb = connection.connect(host="localhost", user="root", passwd="12345",use_pure=True)
cursor = mydb.cursor()
query = "Create database CarbonNanoTubes;"
cursor.execute(query)
mydb.close()

#create table
mydb = connection.connect(host="localhost", database = 'CarbonNanoTubes ',user="root", passwd="12345", use_pure=True)
query = 'create table if not exists carbon1213(n1 varchar(20), n2 varchar(20), n3 varchar(20), n4 varchar(20), n5 varchar(20), n6 varchar(20), n7 varchar(20), n8 varchar(20))'
cursor = mydb.cursor()
cursor.execute(query)
with open('carbon_nanotubes.csv') as data:
    next(data)
    count = 0
    data_csv = csv.reader(data, delimiter = ";")
    for j in data_csv:
        if len(j[-1].split(','))<2:
            j[-1] = j[-1] + ', 0'
#             count+=1
#             print(j)
        try:
            query = 'insert into carbon1213 values(%s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(query,j)

        except Exception as e:
            print(e)
    print("all the data is inserted")
mydb.commit()    
