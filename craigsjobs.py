# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://toronto.craigslist.ca/d/software-qa-dba-etc/search/sof')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# put job information into jobs
job = []
jtitle=""
timer=""
jobstring=""

for pa in soup.find_all('p',{'class':'result-info'}):
    for a in pa.find_all('a',{'class':'result-title hdrlnk'}):
        jtitle=a.text+" "+a.attrs.get('href')
    for t in pa.find_all('time'):
        timer=t.attrs.get('title')
    jobstring=jtitle+" "+timer
    job.append(jobstring)

job = '\n'.join(job)

print(job)
