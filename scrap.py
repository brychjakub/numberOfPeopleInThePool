import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime, date
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler


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

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', seconds=10)
def intoCsv():
    if day == "Monday":
            day_data = [[current_time, numberOfPeopleInThePool]]
            df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
            result = pd.concat([df1])
            result.to_csv('monday.csv', index=False, mode="a")

                    

    if day == "Tuesday":
            day_data = [[current_time, numberOfPeopleInThePool]]
            df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
            result = pd.concat([df1])
            result.to_csv('tuesday.csv', index=False, mode="a")

                    

    if day == "Wednesday":
            day_data = [[current_time, numberOfPeopleInThePool]]
            df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
            result = pd.concat([df1])
            result.to_csv('wednesday.csv', index=False, mode="a")


    if day == "Thursday":
        day_data = [[current_time, numberOfPeopleInThePool]]
        df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
        result = pd.concat([df1])
        result.to_csv('thursday.csv', index=False, mode="a")


    if day == "Friday":
        day_data = [[current_time, numberOfPeopleInThePool]]
        df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
        result = pd.concat([df1])
        result.to_csv('Friday.csv', index=False, mode="a")


    if day == "Satturday":
        day_data = [[current_time, numberOfPeopleInThePool]]
        df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
        result = pd.concat([df1])
        result.to_csv('Satturday.csv', index=False, mode="a")


    if day == "Sunday":
        day_data = [[current_time, numberOfPeopleInThePool]]
        df1 = pd.DataFrame(day_data, columns=['Time', 'Number of people'])
        result = pd.concat([df1])
        result.to_csv('sunday.csv', index=False, mode="a")



scheduler.start()
