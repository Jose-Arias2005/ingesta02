import mysql.connector
import csv
import boto3

mydb = mysql.connector.connect(
    host="3.89.235.4",
    port=8005,
    user="root",
    password="Utec",
    database="tienda"
)

print(mydb)
dbQuery = 'SELECT * FROM fabricantes;'
filename = "fabricantes.csv"
cursor = mydb.cursor()
cursor.execute(dbQuery)
rows = cursor.fetchall()
fp = open(filename, 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
