import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
url="url_for_scrapping"
req=requests.get(url)  #gets response from website as object
print(req)
soup=BeautifulSoup(req.text,'html.parser')  #Convert object to text as html
print(soup)
Modeltable=soup.find('table')     #finds table tag in html, for multiple tables pass attribute like class or id
df=pd.read_html(Modeltable.prettify())
print(df[0])    #list to dataframe

#For manually converting html sting
# columns=Modeltable.find('thead')   #finds head tag inside table
# tr=columns.find('tr')
# td=tr.find_all("th")       #returns list of th  within tr
# row_data=Modeltable.find("tbody")
# tr_data=row_data.find_all("tr")        #returns list of tr with tbody
# a,b=[],[]
# for eachtr in tr_data:
#     each_row_data=eachtr.find_all("td")          #returns a list of th within tr
#     c=[]
#     for each in each_row_data:
#         c.append(each.text)    #converting each list item to text
#     b.append(c)
# for each in td:
#     a.append(each.text)      #for table head
# df=pd.DataFrame(b,columns=a)   #makes a dataframe with wach list in b as row with columns as per items in a list
# print(df)


