import requests
from bs4 import BeautifulSoup
from historical_assistant.main.models import War


def images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='lxml')


    name_battle = soup.find_all('div', class_='page-body mb-[65px]')

    for container in name_battle:
        # Найти все p внутри текущего контейнера
        p_tags = container.find_all('h2')
        p_nn = container.find_all('p')
        c = 0
        n = 0
        i = 80

        for p_tag in p_tags:
            if p_tag.text.strip() != '':
                tit = War(title=p_tag.text.strip(), id=i)
                tit.save()
                c += 1
                i += 1
        for p_tag in p_nn[2:len(p_nn)-1]:
            if p_tag.text.strip() != '':
                discr = War.objects.get(id=i)
                discr.description = p_tag.text.strip()
                discr.save()
                i += 1
                n += 1

url = 'https://histrf.ru/read/articles/zavershayushchiy-period-velikoy-otechestvennoy-voyny-1944-1945-gg-i-sovetsko-yaponskaya-voyna-1945-goda-osnovnye-daty-k-ege'
images(url)