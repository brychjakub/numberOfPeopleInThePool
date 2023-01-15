import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, date
import pandas as pd
import schedule
import time


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


def intoCsv():
            day_data = [[current_time, numberOfPeopleInThePool]]
            df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
            result = pd.concat([df1])
            result.to_csv(f'{day}.csv', index=False, mode="a")

schedule.every(5).minutes.do
schedule.every(5).minutes.do(intoCsv)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
