# from bs4 import BeautifulSoup

# soup = BeautifulSoup()

# import requests

# def fetchAndSaveToFile(url, path):
#     r = requests.get(url)
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(r.text)

# url = "https://timesofindia.indiatimes.com/city/delhi"
# fetchAndSaveToFile(url, "data/times.html")

from bs4 import BeautifulSoup
import requests
import time 

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml') #(information that I want to scrape, parser)
    # a parser is a component that interprets the HTML/XML content and converts it into a formal that BeautifulSoup can work with.
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index, job in enumerate(jobs):
        # enumarate function is going to allow us to iterate over the index of the jobs list and also the job content itself
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'More Info: {more_info} \n')
            print(f'File saved: {index}')        
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)