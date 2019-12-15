import requests
from bs4 import BeautifulSoup
import re


def transcr(your_word):
    url = 'https://www.wordreference.com/definition/'+str(your_word)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    s1 = str(soup).splitlines()
    match = 'placeholder'
    for elem in s1:
        if 'pronWR' in elem:
            match = re.search('\[(.*?)\]', elem).group(0)[1:-1]
            if match != 'placeholder':
                break
    if match == 'placeholder':
        raise Exception('no such word')
    else:
        return match


print('What?')
while True:
    word = input()
    if len(word) > 3:
        lenght = 2*len(word)+12
    else:
        lenght = 2*len(word)+13
    separator = str()
    for i in range(0,lenght):
        separator = separator+str('-')
    trancscripted = transcr(word).replace('<sup>', '').replace('</sup>', '').replace('<i>', '').replace('</i>', '').replace('<small>', '').replace('</small>', '')
    print(separator)
    print('|', word, ' --> ', trancscripted, ' ', '|')
    print(separator)
