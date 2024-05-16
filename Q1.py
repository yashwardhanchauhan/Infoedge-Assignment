import requests, sys
from bs4 import BeautifulSoup
import pandas as pd

url = "https://dell.wd1.myworkdayjobs.com/wday/cxs/dell/External/jobs"

params = {
    "appliedFacets": {
        "Location_Country": [
            "c4f78be1a8f14da0ab49ce1162348a5e"
        ]
    },
    "limit": 20,
    "offset": 0,
    "searchText": ""
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://dell.wd1.myworkdayjobs.com',
    'priority': 'u=1, i',
    'referer': 'https://dell.wd1.myworkdayjobs.com/en-US/External?Location_Country=c4f78be1a8f14da0ab49ce1162348a5e',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-calypso-csrf-token': '585e7c54-e344-45ea-85fc-1e397b2d54d0',
}

def extract(url,params,headers):
  """
  Method to extract response from the url by sending POST request
  :param url: url to send post request
  :param params: raw json data  
  :param headers: Request Header dictonary values
  """
  try:
    response = requests.post(url, json=params,headers=headers)
    
    if response.status_code == 200:
        res = response.json()
        return res
    else:
        print('Failed to send POST request. Status code:', response.status_code)
        sys.exit()

  except requests.exceptions.RequestException as e:
    print('Error:', e)
    
    
print("Q1 Execution Started!!!!")    
res=extract(url,params,headers)
total_jobs= res['total']
page=0
data = {
    "Job Title":[],
    "Location":[],
    "Req ID":[], 
    "Link":[]
    }
while page<total_jobs:
    for i in res['jobPostings']:
        if i.get('title') :
            data["Job Title"].append(i['title']),
            data["Location"].append(i['locationsText'])
            data['Req ID'].append(i['bulletFields'][0])
            data["Link"].append(url+i['externalPath'])
            
    params['offset']+=20
    res=extract(url,params,headers)
    page+=20
df = pd.DataFrame(data)
df.to_excel("Q1_output.xlsx", index=False)
print("Q1 Execution Completed..Check Q1_output.xlsx file")