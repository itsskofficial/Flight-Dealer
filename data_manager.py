import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        sheet_end="https://api.sheety.co/8d8bd9e1daea2ae85b7b1cd31024a980/flightDeals/prices"
        sheet_key="sjajdannenened"
        sheet_headers={"Authorization":f"Bearer {sheet_key}"}

    def retrive_data(self):
        response=requests.get(url=self.sheet_end,headers=self.sheet_headers)
        return response["prices"]
        


