# Import Libraries
from os import path
from pykml import parser
from pykml import util
from lxml import etree
import csv

# Specify KML File
kml_file = 'C:\Python27\Scripts\Candidates.kml'
with open(kml_file) as f:
     doc = parser.parse(f).getroot()

# Parsed output Manipulation

m = 'A'
Candidate = []

# Clear CSV
# ``w+''  Open for reading and writing.  The file is created if it does not
# exist, otherwise it is truncated.  The stream is positioned at
# the beginning of the file.

with open('D:/Candidates.csv','w+') as csvfile:
    csvfile.close()
# Write Headers
headers = ['Name', 'Longitude', 'Latitude']
with open('D:/Candidates.csv','a+') as csvfile:
    Writer = csv.writer(csvfile,delimiter=',',lineterminator ='\n')
    Writer.writerow(headers)
csvfile.close()

# Write Placemarks
for e in doc.Document.Folder.Placemark:
    
    with open('D:/Candidates.csv','a+') as csvfile:
        name = 'Candidate ' + m
        coor = [e.Point.coordinates.text.split(',')]
        Writer = csv.writer(csvfile,delimiter=',',lineterminator ='\n')
        Writer.writerow([name,coor[0][0],coor[0][1]])
        m  = chr(ord(m)+ 1)

        
       
    


