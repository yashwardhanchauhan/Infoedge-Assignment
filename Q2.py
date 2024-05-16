import requests 
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://jobs.bentley.com/search"
data = {
    "Title":[],
    "Location":[],
    "Date":[]
}
def jobcount(URL):
  """
  Method to extract the total count of the Job
  :param URL : URL to webscrap job count
  return count
  """
  r = requests.get(URL)  
  soup = BeautifulSoup(r.content, 'html.parser') 
      
  s = soup.find('span',class_='paginationLabel') 
  count=int(s.find_all('b')[1].string)
  return count
def info(URL):
  """
  :param URL : URL to webscrap entire response
  return res
  """
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html.parser') 
  s = soup.find_all('tr',class_='data-row')
  for i in s:
    record = i
    res=record.find('a',class_="jobTitle-link").string
    loc = record.find('span',class_="jobLocation")
    loc1= loc.find('span',class_="jobLocation")
    date = record.find('span',class_='jobDate').string
    data['Title'].append(res)
    data['Location'].append(str(loc1.string).strip())
    data['Date'].append(date.strip())


print("Q2 Exection Started!!!!")   
count = jobcount(URL)
info(URL)
i=25
while i < count:
  url=f"https://jobs.bentley.com/search?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=10&startrow={i}"
  info(url)
  i+=25
data=pd.DataFrame(data)
data.to_excel('Q2_output.xlsx',index=False)
print("Q2 Execution Completed..Check Q2_output.xlsx file")  