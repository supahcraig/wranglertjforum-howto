from bs4 import BeautifulSoup
import requests

# To overcome the 403 error:
# https://scrapeops.io/web-scraping/playbook/403-forbidden-error-web-scraping/


HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
URL = 'https://wranglertjforum.com/forums/tj-how-to-guides.109/page-1'
page = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')

threads = soup.find_all("div", class_="structItem-title")
thread_list = []
for thread in threads:

    for child in thread.contents:
        if child.name == 'a':
            thread_name = child.contents[0]
            link = thread['uix-href']

            thread_list.append({'thread': thread_name, 'link': link})


for thread in thread_list:
    print(thread['link'])
