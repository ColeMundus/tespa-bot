# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

def analyze(team):
    s = BeautifulSoup(requests.get(team, headers=headers).content, 'html.parser')
    team_name = s.find(class_='hdg-em').text
    bnet = [t.find_next('td').text for t in s.find_all(class_='compete-player-name')]
    average = []
    stringer = f'{team_name} player ratings\n'
    stringer += '-'*(len(stringer)-1) + '\n'
    for player in bnet:
        p = BeautifulSoup(requests.get(f"https://www.overbuff.com/players/pc/{'-'.join(player.split('#'))}?mode=competitive", headers=headers).content, 'html.parser')
        try:
            skill_rating = int(p.find(class_='player-skill-rating').text)
            average.append(skill_rating)
        except:
            skill_rating = 'NA'
        top_played = [t.find_all('a')[1].text for t in p.find_all(class_='player-hero') if len(t.find_all('a')) > 1 and t.find_all('a')[1].text != ''][:5]
        stringer += f'{player:<20} | {skill_rating:>4} | {", ".join(top_played)}\n'
    stringer += f'Average Team SR: {sum(average)//len(average)}\n'
    return stringer

def findSR(name):
    p = BeautifulSoup(requests.get(f"https://www.overbuff.com/players/pc/{'-'.join(name.split('#'))}?mode=competitive", headers=headers).content, 'html.parser')
    try:
        skill_rating = p.find(class_='player-skill-rating').text
    except:
        skill_rating = 'NA'
    return f'{name}: {skill_rating}'
