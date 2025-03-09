import requests
from bs4 import BeautifulSoup
from historical_assistant.main.models import War


def images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='lxml')

    # Найти все контейнеры новостей
    name_battle = soup.find_all('div', class_='page-body mb-[65px]')

    for container in name_battle:
        # Найти все p внутри текущего контейнера
        p_tags = container.find_all('p')
        p_nn = container.find_all('strong')
        p_tags.pop(1)
        p_tags.pop(1)
        c = 0
        n = 0
        i = 1

        for p_tag in p_tags[:len(p_tags)-1]:
            if p_tag.text.strip() != '':
                description = War(description = p_tag.text.strip())
                description.save()
                c += 1
        for p_tag in p_nn:
            if p_tag.text.strip() != '':
                if n != 23:
                    tit = War.objects.get(id=i)
                    tit.title = p_tag.text.strip()
                    tit.save()
                    print(p_tag.text.strip())
                    i += 1
                n += 1

url = 'https://histrf.ru/read/articles/velikaya-otechestvennaya-voyna-chast-1'
images(url)