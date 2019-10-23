import schedule
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
import time
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from xml.etree import ElementTree as ET
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(json.dumps(xmltodict.parse(xml)))
def getstocksummary(godowname,arr):
    xml ="""<ENVELOPE>
        <HEADER>
            <TALLYREQUEST>Export Data</TALLYREQUEST>
        </HEADER>
        <BODY>
            <EXPORTDATA>
                <REQUESTDESC>
                    <STATICVARIABLES>
                        <!--Specify the GodownName here-->
                        <DSPGODOWNNAME>{}</DSPGODOWNNAME>
                        <!--If Detailed format is required, then specify YES otherwise NO-->
                        <EXPLODEFLAG>Yes</EXPLODEFLAG>
                        <!--Expand All levels-->
                        <EXPLODEALLLEVELS>Yes</EXPLODEALLLEVELS>
                    </STATICVARIABLES>
                    <!--Specify the Report Name here-->
                    <REPORTNAME>Godown Summary</REPORTNAME>
                </REQUESTDESC>
            </EXPORTDATA>
        </BODY>
    </ENVELOPE>""".format(godowname)
    headers = {'Content-Type': 'application/xml'}
    # set what your server accepts
    response=requests.post('http://localhost:9002', data=xml, headers=headers).text
    result=xmltodict.parse(response)
    print(result)
    #print(len(result['ENVELOPE']['DSPACCNAME']))
    #print(json.dumps(result['ENVELOPE']['DSPACCNAME'],indent=4,sort_keys=True))
    #pp.pprint(result)
    #pp.pprint(json.dumps(xmltodict.parse(response)))
    #date      
    date = datetime.datetime.now()
    print(date)

    headings = ("SKU", "Stock Location", "Report Year", "Report Month"," Report Day", "Closing Quantity") 
    print(headings)

    savedFilename = date.strftime("Stock-summary-%d-%m-%y") 
    print(savedFilename)

    root_path=os.environ['USERPROFILE']
    save_path =root_path+'/Desktop/'

    completeName = os.path.join(save_path, savedFilename +".csv")
    print(completeName)


    try:
        prodList =len(result['ENVELOPE']['DSPACCNAME'])
        print(prodList)
        print(result['ENVELOPE']['DSPACCNAME'][0]['DSPDISPNAME'])
        for i in range(prodList):
            prodName =result['ENVELOPE']['DSPACCNAME'][i]['DSPDISPNAME']
            #print(prodName)
            #print(result['ENVELOPE']['DSPSTKINFO'][i]['DSPSTKCL']['DSPCLQTY'])
            clsQty =result['ENVELOPE']['DSPSTKINFO'][i]['DSPSTKCL']['DSPCLQTY']
    #split data (num2Cls = numCls[0].split(' ');var num3Cls = num2Cls[0];)
            numCls=clsQty.split()[0]
            #print(numCls)
            #print(len(arr))
            for j in range(len(arr)):
                #print(arr[j]['reatailor_name'])
                #print(j)
                if arr[j]['reatailor_name']==prodName:
                    sku = arr[j]['SKU']
                    #print("{}".format(arr[j]['reatailor_name']))
                    #print(arr[j]['SKU'])
                    values =  str(sku) + "," + godowname+ "," +date.strftime('%Y')+ "," +date.strftime('%m')+ ","+date.strftime('%d')+ ","+ numCls     
                    print(values)
                    
                    csvRow = [values]
                    #print(csvRow)
                    
                    with open (completeName, "a",newline='') as file:
                        headings = ("SKU", "Stock Location", "Report Year", "Report Month"," Report Day", "Closing Quantity") 
                        writer = csv.writer(file, delimiter=' ', quotechar=' ', dialect='excel')
                        writer.writerow(csvRow)
                    #file1 = open(completeName, "w")
                    #csvwriter = csv.writer(file1)


        cred = open('E:\Tally Connector\Tally-connector-6d187b87ff6d.json', 'rb').read()
        credJson=json.loads(cred)
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credJson)
        client = storage.Client(credentials=credentials, project='tally-connector')
        bucket = client.get_bucket('tally-connector')
        blob = bucket.blob('myfile')
        blob.upload_from_filename('C:/Users/91908/Desktop/Tally/project/stock-summary-23-10-19.csv')
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
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)
        
print(arr)
with open(jsonFilePath, "w") as jsonFile:
     jsonFile.write(json.dumps(arr, indent = 4))
print()


checkForGodowns = True
godownNames=[]
for gdwns in range(len(arr)):

    if checkForGodowns:
            print(arr[gdwns]['Godownname'])    
            gdwnName = arr[gdwns]['Godownname']
            
            if (len(gdwnName)>0):
               godownNames.append(gdwnName)
               
               
    else:
        checkForGodowns = False
        break
print(godownNames)
for g in  godownNames:
    getstocksummary(g,arr)

   

def job():
    getstocksummary(g,arr)
    reader = csv.DictReader(open("cron.csv"))
    for raw in reader:
        print(raw)

schedule.every(2).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:53").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)








        
 
      


