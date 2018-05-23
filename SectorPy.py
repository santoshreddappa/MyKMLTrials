# list Imports

import os,csv,math,pykml

# Define Variables

openDirectory = raw_input('Enter directory where your Site Data.csv file is: ')
saveDirectory = openDirectory
siteData=[]
headers = []

while not(os.path.isdir(openDirectory)):
    print "Directory does not exist"
    openDirectory = raw_input('Enter directory where your Site Data.csv file is: ')
openDirectory += '\Site Data.csv'

with open(openDirectory,'r') as csvfile: 
    csv_reader =csv.reader(csvfile, dialect='excel',delimiter=',')
    for row in csv_reader:
        siteData.append(row)
    csvfile.close

siteData[0].append('Upper Bound')
siteData[0].append('Lower Bound')


