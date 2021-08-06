from os import sep
import requests
import pandas as pd
import csv
import numpy as np



class NseIndia:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def get_option_chain(self, symbol, indices=False):
        url = 'https://www.nseindia.com/api/option-chain-equities?symbol=' + symbol
        data = self.session.get(url,headers=self.headers).json()["records"]["data"]
        my_df = []
        for i in data:            
            for k, v in i.items():
                if k == "CE" or k == "PE":                    
                    info = v
                    info["instrumentType"] = k
                    if info["openInterest"] != 0:
                        # print(info["openInterest"])
                        my_df.append(info)
        my_df=pd.DataFrame(my_df)
        my_df.to_csv("RAW_DATA.csv", sep=',')

        import pandas as pd

  
  
# Reading the csv file
df_new = pd.read_csv('Names.csv')
  
# saving xlsx file
GFG = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(GFG, index = False)
  
GFG.save()

    #    with open('RAW_DATA.csv') as csvfile:
    #         csvReader = csv.reader(csvfile, delimiter=',')
    #         for row in csvReader:
    #             my_df.append(row)
    #     my_df=pd.DataFrame(my_df)
    #     my_df.to_csv("RAW_DATA1.csv", sep=',' ) 
        # my_df.to_excel("RAW_DATA.excel", sep=',')
        # my_df = pd.read_csv("RAW_DATA.csv", sep = ',')
        # my_df.to_csv('modifiedRAW_DATA.csv')

        

nse = NseIndia()
print(nse.get_option_chain("ACC"))



