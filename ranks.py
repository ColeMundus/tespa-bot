# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:27:50 2018

@author: ryans
"""
import requests
from bs4 import BeautifulSoup
def analyze(team):
    #r = requests.get('https://compete.tespa.org/tournament/111/team/23056')
    r = requests.get(team)
    #print(r.text[0:500])
    soup = BeautifulSoup(r.text, 'html.parser')
    players = len(soup.find_all('td', attrs={'class':'compete-player-name'}))
    #results = soup.find_all('table', attrs={'class':'compete-table'})
    results = soup.find_all('td')
    #print(results)
    #print(len(results))
    battletag = []
    battletag2 = []
    sr = []
    avg = 0
    count = 0
    for player in range(1, players+1):
        battletag.append(results[player*7 -5])
        battletag2.append(str(battletag[player-1]).strip('/<td>'))
    for player2 in battletag2:
        #print(player2)
        #search = 'https://www.overbuff.com/players/pc/' + player2.replace('#','-')
        #search = 'https://playoverwatch.com/en-us/career/pc/' + player2.replace('#','-')
        #print(search)                                                         
        #r2 = requests.get('https://www.overbuff.com/players/pc/' + player2.replace('#','-'))    
        r2 = requests.get('https://playoverwatch.com/en-us/career/pc/' + player2.replace('#','-'))
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        #print('https://www.overbuff.com/players/pc/' + player2.replace('#','-'))
        #print(r2.text[0:100])
        #results2 = soup2.find_all('span', attrs={'class':'player-skill-rating'})
        results2 = soup2.find('div', attrs={'class':'u-align-center h5'})
        sr1 = str(results2)
        sr1 = sr1.strip('<div class="u-align-center h5">')
        sr1 = sr1.strip('/')
        sr1 = sr1.strip('<')
        #print(player2)
        #print(sr1)
        #print(results2)
        if sr1 != 'No':
            avg += int(sr1)
            count += 1
        playerandsr = str(player2 + ': ' + sr1 + '      ')
        sr.append(playerandsr)
    avg = round(avg/count)
    sr.append('Average SR: ' + str(avg))
    stringer = '\n'.join(map(str, sr))
    return(stringer)

def findSR(name):
    newName = name.replace('#','-')
    r = requests.get('https://playoverwatch.com/en-us/career/pc/' + newName)
    soup = BeautifulSoup(r.text, 'html.parser')
    sr = soup.find('div', attrs={'class':'u-align-center h5'})
    sr = str(sr)
    sr = sr.strip('<div class="u-align-center h5">')
    sr = sr.strip('/')
    sr = sr.strip('<')
    #for image in soup.find('div', attrs={'class':'competitive-rank'}):
        #print(image.get('src'))
        #images = str(image.get('src'))
    #image = str(image)
    #image = image.strip('imgsrc=')
    #print(image)
    outputter = str(name + ': ' + sr)
    return(outputter)
    
def test():
    array = [1,2,3,4]
    string = '\n'.join(map(str, array))
    return(string)