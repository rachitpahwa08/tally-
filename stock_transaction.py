import schedule
import time
import datetime
#import xml2json
import requests
import optparse
import csv
import json
import pandas as pd
import os.path
import xmltodict
import pprint
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials

from xml.etree import ElementTree as ET
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(json.dumps(xmltodict.parse(xml)))
def getSummaryInDetail(fromDate, toDate, ledgerName):
    xml ="""<ENVELOPE>
                     <HEADER> 
                           <TALLYREQUEST>Export Data</TALLYREQUEST> 
                       </HEADER> 
                       <BODY> 
                           <EXPORTDATA> 
                           <REQUESTDESC> 
                           <STATICVARIABLES> 
                               <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>  
                                 <EXPLODEALLLEVELS>YES</EXPLODEALLLEVELS> 
                           <!-- Specify the period here --> 
                          <SVFROMDATE>{}</SVFROMDATE> 
                           <SVTODATE>{}</SVTODATE> 
                           <ISITEMWISE>YES</ISITEMWISE> 
                           <!--Show billwise is set to Yes --> 
                           <DBBILLEXPLODEFLAG>YES</DBBILLEXPLODEFLAG> 
                           <DBINVEXPLODEFLAG>Yes</DBINVEXPLODEFLAG>       
                           <!-- Option Show Voucher Numbers also = Yes --> 
                           <EXPLODEVNUM>YES</EXPLODEVNUM> 
                            <VOUCHERTYPENAME>Sale</VOUCHERTYPENAME> 
                           <!-- Specify the Ledger Name here --> 
                           <LEDGERNAME>{}</LEDGERNAME> 
                           <DSPSHOWTRANS>YES</DSPSHOWTRANS> 
            		   </STATICVARIABLES> 
                           <REPORTNAME>Ledger Vouchers</REPORTNAME> 
                            </REQUESTDESC> 
                           </EXPORTDATA> 
                       </BODY> 
                       
                       
                   </ENVELOPE>""".format(fromDate, toDate, ledgerName)
    headers = {'Content-Type': 'application/xml'}
    # set what your server accepts
    
    response=requests.post('http://localhost:9002', data=xml, headers=headers).text
    result=xmltodict.parse(response)
    #print(result)
   
    #print(len(result['ENVELOPE']['DSPEXPLVCHNUMBER']))
    #print(json.dumps(result['ENVELOPE']['DSPEXPLVCHNUMBER'],indent=4,sort_keys=True))
    #pp.pprint(json.dumps(xmltodict.parse(xml)))
    date = datetime.datetime.now()
    #print(date)

    savedFilename = date.strftime("Transactions-%d-%m-%y")
    #print(savedFilename)

    root_path=os.environ['USERPROFILE']
    save_path =root_path+'/Desktop/'

    completeName = os.path.join(save_path, savedFilename +".csv")
    print(completeName)

    try:
        transaction =len(result['ENVELOPE']['DSPEXPLVCHNUMBER'])
        #print(transaction)
        #print(result['ENVELOPE']['DSPEXPLVCHNUMBER'][0])
        for i in range(transaction):
            transactionID =result['ENVELOPE']['DSPEXPLVCHNUMBER'][i]
            #print(transactionID)
            #split transactionID
            trans = transactionID.split()
            #print(trans)
            transactionType = result['ENVELOPE']['DSPVCHTYPE'][i]
            #print(transactionType)
            ledger = result['ENVELOPE']['DSPVCHLEDACCOUNT'][i]
            #print(ledger)
            quantity = result['ENVELOPE']['DSPVCHBILLEDQTY'][i]
            #print(quantity)
            #split quantity
            quantity = quantity.split(' ')
            number = quantity[0]
            unit = quantity[1]
            prodName = result['ENVELOPE']['DSPVCHSTOCKITEM'][i]
            #print(prodName)
            transaction = "";
            docRef = "";
            source = "";
            destination = "";
            
                   
            for j in range(len(arr)):
                #print(arr[j]['reatailor_name'])
                #print(j)
                if arr[j]['reatailor_name']==prodName:
                    sku = arr[j]['SKU']
                    #print("{}".format(arr[j]['reatailor_name']))
                    #print(arr[j]['SKU'])

                    if transactionType == 'Sale' or transactionType == "Rcpt" :
                        source = "Godown"
                        destination = ledger
                        transaction = "OUT"
                        docRef = 'Sale Transaction'
                    
                    elif transactionType == 'Purc' or transactionType == 'Purchase' or transactionType == 'Pymt' or transactionType == 'Payment':
                        transaction = "IN"
                        docRef = 'GRN Transaction'
                        source = ledger
                        destination = "Godown"
                    
                    fileData = str(transactionID) + "," + str(transaction) + "," + source + "," + destination + "," + str(sku) + "," + number + "," + unit + "," + date.strftime("%y-%m-%d") + "," + docRef
                    #print(fileData)


                    csvRow = [fileData]
                
                    print(csvRow)

                    
                    with open (completeName, "a",newline='') as file:
                        headers = ["Transaction ID", "Transaction Type (In/Out/Return)", "Source", "Destination", "SKU", "Quantity", "Unit", "Year", "Month", "Date", "Document Ref"]
                        writer = csv.writer(file, delimiter=' ', quotechar=' ', dialect='excel')
                        writer.writerow(csvRow)
                        #writer.writerow()
                    #file1 = open(completeName, "w")
                    #csvwriter = csv.writer(file1)

        cred = open('E:\Tally Connector\Tally-connector-6d187b87ff6d.json', 'rb').read()
        credJson=json.loads(cred)
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credJson)
        client = storage.Client(credentials=credentials, project='tally-connector')
        bucket = client.get_bucket('tally-connector')
        blob = bucket.blob('myfile')
        blob.upload_from_filename('C:/Users/91908/Desktop/Tally/project/Transactions-23-10-19.csv')
        if(blob.public_url):
            print("file uploded successfully")

    
                    

                    
    except TypeError:
        print('nothing')



csvFilePath = "config.csv"
jsonFilePath = "file.json"
arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    fieldsname = ("reatailor_name","SKU","Godownname")
    csvReader = csv.DictReader(csvFile,fieldsname)
    #print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)
        
#print(arr)
with open(jsonFilePath, "w") as jsonFile:
     jsonFile.write(json.dumps(arr, indent = 4))
#print()
        




# Main
fromDate = "20190301"
toDate = "20190731"
getSummaryInDetail(fromDate,toDate,"Sales")
#fromDate = date.strftime("%y%m%d"), toDate = date.strftime("%y%m%d")
def job():
    getSummaryInDetail(fromDate, toDate, ledgers)
    
with open('cron.csv', 'r') as f:
    res=f.read()
    minutes=res.split(",")[1].split('"')[0]
    hours=res.split(",")[0][1:]
    #print(miniutes+" "+hours)
    
schedule.every(2).minutes.do(job)
schedule.every().hour.do(job)
print(hours+" "+minutes)
schedule.every().day.at("{}:{}".format(hours,minutes)).do(job)

while 1:
    schedule.run_pending()

fields = ("Transaction ID", "Transaction Type (In/Out/Return)", "Source", "Destination", "SKU", "Quantity", "Unit", "Year", "Month", "Date", "Document Ref")
ledgers = ['Purchase', 'Sales', 'Payment'] ;



   
    
fieldsWritten = True
if fieldsWritten:
          for i in range(len(ledgers)):
              #print(arr[i]['ledgers'])
              getSummaryInDetail(fromDate, toDate, ledgers)
          

else:
    fieldsWritten = False
#this is code for cron that is static one how i call that time here?


