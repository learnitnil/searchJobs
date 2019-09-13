'''
This script for search for jobs in the specified websites using specified keywords
'''
import requests
import json
from bs4 import BeautifulSoup

jobSites = [
    {
        'key' : 'findaphd',
        'url' : 'https://www.findaphd.com'
    },
    {
        'key' : 'academicpositions',
        'url' : 'https://academicpositions.co.uk'
    },
    {
        'key' : 'jobs-uk',
        'url' : 'https://www.jobs.ac.uk'
    },
    {
        'key' : 'academic transfer',
        'url' : 'https://www.academictransfer.com'
    },
    {
        'key' : 'acadeimicgates',
        'url' : 'https://www.academicgates.com'
    },
    {
        'key' : 'univesitypositions',
        'url' : 'https://www.universitypositions.eu'
    }
]

keywords = ['internet of things']

def checkForJobs(site,keyword) :
    url = ''
    if site['key'] == 'findaphd' :
        # filters are non-european student and 30 results per page
        url = site['url'] + '/phds/non-eu-students/?01w0&PP=30&Keywords='+keyword.replace(' ','+')

    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    allResults = soup.find_all("div", class_="resultsRow")
    for result in allResults :
        courseInfo = result.find("a",class_="courseLink")
        try :
            print(courseInfo.get_text())
        except :
            print('unable to get text info')

for site in jobSites :
    for keyword in keywords :
        checkForJobs(site,keyword)
