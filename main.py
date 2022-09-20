#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

SHEET_END="https://api.sheety.co/8d8bd9e1daea2ae85b7b1cd31024a980/flightDeals/prices"
SHEET_KEY="sjajdannenened"
sheet_headers={"Authorization":f"Bearer {SHEET_KEY}"}

response=requests.get(url=SHEET_END,headers=sheet_headers)
print(response.json())