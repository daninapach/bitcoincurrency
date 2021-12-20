from fastapi import FastAPI
import requests
import json
from datetime import datetime
import os
import uvicorn

# load environment variables
port = os.environ["PORT"]

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"website run successfully"}

@app.get("/bitCoin/{currency}")
async def bitcoin_rate(currency):
    #url api for currency
    try: 
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.exceptions.RequestException as e:
        return "Wrong Website"

    now = datetime.now() # current date and time
    try: 
        data = response.json()
    except Exception as e:
        with open('Failed.py', 'w') as file:
            file.write(now.strftime("%m/%d/%Y, %H:%M:%S") +  " > json: " + str(e))
        return "Wrong Web Site"
    try:
        #get rate by Currency
        return (currency + ": " + data['bpi'][currency]['rate'] + " " + data['bpi'][currency]['description'])
    except Exception as e:
        with open('Failed.py', 'w') as file:
            file.write("response: " + str(e))
        return "Web Site Down"

  
  
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(port), reload=True)


    
