import json
import requests


token = "ton token"
i = 0
groupeid = input("Rentre l'id du groupe que tu veux down : ") 
headers = {
    'authorization': token,
    'content-type': 'application/json',

}
regions = ["japan", "europe"]
while i <= 2:
    data = {"region": regions[i]}
    json_object = json.dumps(data, indent = 4)
    response = requests.patch(f'https://discord.com/api/v9/channels/{groupeid}/call', headers=headers, data=json_object)
    print(response.text)
    i += 1
    if i == 2:
        i = 0
