from bs4 import BeautifulSoup
import requests
import time

while True:
    try:
        f = open('name.txt', 'r', encoding="utf-8")
        name = f.readline()
        web_page = requests.get(f'https://en.wikipedia.org/wiki/{name}')

        soup = BeautifulSoup(web_page.content, 'html.parser')
        para = soup.find_all('p')[2].get_text()
    except IndexError:
        pass

    f.close()

    f = open('bio.txt', 'w', encoding="utf-8")
    f.write(para)
    f.close()
    time.sleep(5)