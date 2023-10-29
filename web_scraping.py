from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def urls_scrabing(site):
    urls = []
    soup = BeautifulSoup(site.text, 'html.parser')
    urls_in_html = soup.find('div', class_ = 'panel-body content_body allow-overflow').find('table', class_ = 'table')
    for a in urls_in_html.find_all('a', href = True):
        urls.append('https://www.rottentomatoes.com/' + a['href'])
    return urls

site = requests.get('https://www.rottentomatoes.com/top/bestofrt/')
urls = urls_scrabing(site=site)

df_list = []
for movie_url in urls:
    supsite = requests.get(movie_url)

    soup = BeautifulSoup(supsite.text, 'html.parser')

    title = soup.find('title').contents[0][:-len(" - Rotten Tomatoes")]
    audience_score = str(soup.find('score-board'))[
                     len('<score-board audiencescore="'):len('<score-board audiencescore="') + 2]
    audience_count = soup.find('a', class_='scoreboard__link scoreboard__link--audience').contents[0]

    score_board_txt = str(soup.find('score-board'))
    a = score_board_txt.find('tomatometerscore="') + len('tomatometerscore="')
    b = score_board_txt.find('" tomatometerstate="certified-fresh">')
    tomatometer_score = score_board_txt[a:b]

    a2 = score_board_txt.find('slot="critics-count">') + len('slot="critics-count">')
    b2 = score_board_txt.find(' Reviews</a>')
    tomatometer_count = score_board_txt[a2:b2]

    df_list.append({'title': title, 'audience score': int(audience_score), 'audience count': audience_count,
                    'tomatometer score': int(tomatometer_score), 'tomatometer_count': tomatometer_count})

df = pd.DataFrame(df_list)

print(df.head())