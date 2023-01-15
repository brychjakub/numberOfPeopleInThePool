import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, date
import pandas as pd


today = date.today()
date = today.strftime("%d/%m/%Y")
day = today.strftime("%A")
print(day,date)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)

res = requests.get("https://www.kravihora-brno.cz/kryta-plavecka-hala")
soup = BeautifulSoup(res.text, "html.parser")

#HTML class where is the info I need
found = soup.select(".field__item")[3]

#exact <p>tag with my info
pTag = str(found.find_all("p")[-1])

#extracting the exact info 
numberOfPeopleInThePool = (re.findall(r'\d+', pTag))[0]
print(numberOfPeopleInThePool)

"""
if day == "Monday":
        monday_data = [['Time', 'Number of people'],
                    ['09:00', 20],
                    ['10:00', 25],
                    ['11:00', 30]]

if day == "Tuesday":
    tuesday_data = [['Time', 'Number of people'],
                ['09:00', 15],
                ['10:00', 20],
                ['11:00', 25]]

if day == "Wednesday":
    wednesday_data = [['Time', 'Number of people'],
                  ['09:00', 10],
                  ['10:00', 15],
                  ['11:00', 20]]
sunday_data = [current_time, numberOfPeopleInThePool]



df1 = pd.DataFrame(monday_data, columns=['Time','Number of people'])
df1.insert(0,'Day', 'Monday')

df2 = pd.DataFrame(tuesday_data, columns=['Time','Number of people'])
df2.insert(0,'Day', 'Tuesday')

df3 = pd.DataFrame(wednesday_data, columns=['Time','Number of people'])
df3.insert(0,'Day', 'Wednesday')

df4 = pd.DataFrame(sunday_data, columns=[current_time, numberOfPeopleInThePool])

result = pd.concat([df4])

result.to_csv('data.csv', index=False, mode="a")
"""


