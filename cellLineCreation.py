'''
Created on Nov 18, 2017

@author: Alex
'''
import MySQLdb
from smtplib import prompt
import json

def main():
    user = prompt("Enter Username for DB: ")
    password = prompt("Enter PassWord for DB: ")
    dbName = prompt("Enter DB name: ")
    data = getData()
    
def getData():
    data = open("data.json", "r")
    data = json.loads(data)
    return data

def parseData(data):
    pass
    allData = []
    rowOfData = {}
    for item in data:
        rowOfData['Type'] = item['Type']
        rowOfData['Source'] = item['Source']
        rowOfData['Sequence'] = item['Sequence']
        rowOfData['Size'] = item['Size']
        rowOfData['Tissue'] = item['Tissue']
        rowOfData['CellGrowthTime'] = item['CellGrowthTime']
        rowOfData['Morphology'] = item['Morphology']
        rowOfData['CultureConditions'] = item['CultureConditions']
        rowOfData['AdherentVSuspended'] = item['AdherentVSuspended']
        rowOfData['Applications'] = item['Applications']
        
        allData.append(rowOfData.copy())
    ##Got all data in an arary now
    return allData

def createDB(user, password, dbName):
    db = MySQLdb.connect("localhost", user, password, dbName)
    ###Need To create the DB
    
if __name__ == '__main__':
    main()