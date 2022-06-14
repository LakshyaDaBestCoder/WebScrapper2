from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')
trTags = star_table[7].find_all('tr')

temp_list= []
for tr in trTags:
    tdTags = tr.find_all('td')
    for tdTag in tdTags:
        row = tdTag.text.rstrip()
        temp_list.append(row)

names = []
distance =[]
mass = []
radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

headers = ['Name','Distance','Mass','Radius']  
df = pd.DataFrame(list(zip(names,distance,mass,radius,)),columns=headers)
print(df)

df.to_csv('lightestStars.csv', index=True, index_label="id")