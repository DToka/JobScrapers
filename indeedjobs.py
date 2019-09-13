# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# get the data
searchInput = "junior-software"
url="https://www.indeed.ca/jobs?q=junior+software&l=Toronto%2C+ON"

data=requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
job = []
jobLink = ""
jobTitle = ""
jobSummary = ""
for divJ in soup.find_all('div',{'data-tn-component':'organicJob'}):
    for divT in divJ.find_all('div',{'class':'title'}):
        for aT in divT.find_all('a'):
            jobTitle=aT.attrs.get('title')
            print(jobTitle)
            jobLink='www.indeed.ca'+aT.attrs.get('href');
    for divS in divJ.find_all('div',{'class':'summary'}):
        jobSummary=divS.text
    jobString=jobTitle+" "+jobSummary+" "+jobLink+"\n"
    job.append(jobString)

job = '\n'.join(job)

print(job)
