import requests
from bs4 import BeautifulSoup
import string
import re
from datetime import datetime, timedelta
import pandas as pd
import pandas_datareader.data as web

""" 
logic:
1. scrape code from the web by request
2. For loop with code in FT to get data
3. Save it in table and send to database
Storing the code status: append code into code 

# for append being pass to pandas and show in tables

"""

# Execution           

# Part 1: Getting the US Stock Code 

codes = []                                 # store table being store from the web
letters = list(string.ascii_uppercase)
for letter in letters:
    url = f"https://eoddata.com/stocklist/NASDAQ/{letter}.htm"
    req = requests.get(url)
    soup = BeautifulSoup(req.content)
    
    # filter with special pattern: stockquote/NASDAQ/...
    tags = soup.find_all("a", href=re.compile("/stockquote/NASDAQ/"))

    for t in tags: 
        if (t.string is not None):
            if (len(t.string) >= 2 or t.string != "HOME"):
                codes.append(t.string)

#-----------------------------------------------------------------------------------------------

# Part 2: Access data from pandas

count = 0
endDate = datetime.now()                   # Due to current time system (your computer)
startDate = endDate - timedelta(days=1)    # Two days before current date (your computer)

str_endDate = endDate.strftime("%Y-%m-%d")         # date object to string   
str_startDate = startDate.strftime("%Y-%m-%d")     

codeStatus = {
    "code":[],  
    "codeOpen ($)":[],
    "codeClose ($)":[],
    "codeVolume":[]
    }


for code in codes:
    count += 1
    data = web.DataReader(code, "yahoo", str_startDate, str_endDate)
    # 要最新果日 (SCRARPE TIME: 香港時間 2022/01/29 01:20 AM, 但用"2022-01-28", "2022-01-29" 會顯示出27, 28 日的價(可能是時差問題))
    
    # Attracting the number of rows from the dataset
    for i in range(data.shape[0]):
        stockOpen = data["Open"][i]
        stockClose = data["Close"][i]
        stockVolume = data["Volume"][i]
   
        codeStatus["code"].append(code)
        codeStatus["codeOpen ($)"].append(stockOpen)
        codeStatus["codeClose ($)"].append(stockClose)
        codeStatus["codeVolume"].append(stockVolume)
    
#-----------------------------------------------------------------------------------------------


# Part 3: Convert Dict to DataFrame and export to CSV file

df = pd.DataFrame(codeStatus)
df.to_csv(f"stockList_{str_endDate}.csv", index=False)

print("Mission complete !")
print(f"Number of stock access: {count}")

