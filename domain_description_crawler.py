import requests
import json
import itertools
import argparse
from bs4 import BeautifulSoup


#Enter a list of domains user the format "domain.com"
domains = ['goal.com']

for domain in domains:

    try:
        crawl_domain = 'http://www.{}'.format(domain)
        response = requests.get(crawl_domain)
        text = response.text
        soup = BeautifulSoup(text, features= 'lxml')

        #This block sifts through the DOM of the domain for the <meta> data
        #description tag of the website
        metas = soup.find_all('meta')
        meta_data = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]

        if len(meta_data) < 1:
            print('No description can be pulled for {}'.format(domain))
            print('Please go to the actual site')

        else:
            print('\n{} description:\n'.format(domain))
            print('{}\n'.format(meta_data[0]))

    except Exception as error:
        print(error)
        print('Crawl FAILED: Please try the naming convention of "domain.com"')
        continue

print('Done')
