import requests
import time 

token = "Your token"
i = 0
groupeid = input("Group dm ID : ") 
headers = {
    'authorization': token,
    'content-type': 'application/json',
}

regions = ["japan", "europe"]
while i <= 2:
    data = {"region": regions[i]}
    response = requests.patch(f'https://discord.com/api/v9/channels/{groupeid}/call', headers=headers, json=data)
    print(response.text)
    time.sleep(0.7)
    i += 1
    if i == 2:
        i = 0
