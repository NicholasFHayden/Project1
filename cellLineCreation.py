'''
Created on Nov 18, 2017

@author: Alex Levin
'''
import MySQLdb
from smtplib import prompt
import json

def main():
    user = prompt("Enter Username for DB: ")
    password = prompt("Enter PassWord for DB: ")
    dbName = prompt("Enter DB name: ")
    data = getData()
    table = parseData(data)
    createDB(user, password, dbName)
    
    
def getData():
    data = open("data.txt", "r")
    data = json.loads(data)
    return data

def parseData(data):
    pass
    allData = []
    rowOfData = {}
    i = 0
    for item in data:
        rowOfData['ID'] = i ##Auto Increment an ID
        rowOfData['size'] = item['size']
        rowOfData['culture'] = item['culture']
        rowOfData['seq'] = item['seq']
        rowOfData['cell'] = item['cell']
        rowOfData['advSus'] = item['advSus']
        rowOfData['subtype'] = item['subtype']
        rowOfData['time'] = item['time']
        rowOfData['productsheets'] = item['productsheets']
        rowOfData['application'] = item['application']
        rowOfData['institution'] = item['institution']
        rowOfData['pubs'] = item['pubs']
        rowOfData['type'] = item['type']
        rowOfData['tissue'] = item['tissue']
        i = i + 1
        
        allData.append(rowOfData.copy())
    ##Got all data in an arary now
    return allData

def createDB(user, password, dbName):
    db = MySQLdb.connect("localhost", user, password, dbName)
    cursor = MySQLdb.cursors.Cursor()
    cursor.execute("DROP TABLE IF EXISTS alldata")
    ## NEED DATA TYPES TO ASSIGN FOR DATA TABLES
    cursor.execute("CREATE TABLE alldata(ID INTEGER PRIMARY KEY, type TEXT, size TEXT, culture TEXT, seq TEXT, cell TEXT, advSus TEXT, subtype TEXT, time TEXT, productsheets TEXT, application TEXT, institution TEXT, pubs TEXT, tissue TEXT) ")
    ###Need To create the DB
    cursor.close()
    db.commit()
    
def insertValues():
    pass
    
if __name__ == '__main__':
    main()