import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

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
pTag = found.find_all("p")[-1]

#extracting the exact info 
numberOfPeopleInThePool = (str(pTag)[22:24])
print(numberOfPeopleInThePool)





