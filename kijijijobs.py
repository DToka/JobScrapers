# -*- coding: utf-8 -*-
"""
DToka September 2019
Kijiji Scraper for jobs
"""

import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://www.kijiji.ca/b-jobs/city-of-toronto/developer/k0c45l1700273')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# put job information into jobs
job = []
jobTitle=""
jobLink=""
jobDesc=""
for tables in soup.find_all('table', class_=lambda x: x != 'urgent'):
    for pa in tables.find_all('td',{'class':'description'}):
        for a in pa.find_all('a'):
            jobTitle=a.text
            jobLink=a.attrs.get('href')
            #if jobLink start with / append kijiji to front
        for p in pa.find_all('p',{'class':None}):
            jobDesc=p.text
        jobstring=JobTitle+" "+JobDesc+" "+JobLink
        job.append(jobstring)

job = '\n'.join(job)

print(job)
