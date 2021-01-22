import sys
import csv
from datetime import date
from bs4 import BeautifulSoup
from core.views import add_record
from core.services import get_map_result

site_name=""
fileread = "txgidocs.csv"
filewrite = "C:\\Users\\SSD\\Desktop\\testmeta.csv"
today=date.today()
fileds = ["S.No","Date", "Name", "Keyword", "City", "Position"]
result = []
with open(fileread, 'r') as fr:  
    csvdata = csv.reader(fr)
    header = next(csvdata)
    print(header)
    sn = 0
    for row in csvdata:
        site_name=row[2]       
        keyword = row[3]  
        city = row[4]      
        found=get_map_result(site_name,keyword,city)
        print(found)        
        sn = sn+1
        result.append([sn, today, site_name,  keyword, city, found])
with open(filewrite, mode="w") as fw:
    csv_write = csv.writer(fw)
    csv_write.writerow(fileds)
    csv_write.writerows(result)

