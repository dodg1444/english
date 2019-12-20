import requests
from bs4 import BeautifulSoup
import re


def transcr(your_word):
    url = 'https://www.macmillandictionary.com/dictionary/british/'+str(your_word)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_by_tag = soup.find("span", {"class":"PRON show_less"})
    match = re.findall('\>(.*?)\<', str(soup_by_tag))
    return match[2]


print('What?')
while True:
    word = input()
    if len(word) > 3:
        lenght = 2*len(word)+12
    else:
        lenght = 2*len(word)+13
    separator = str()
    for i in range(0, lenght):
        separator = separator+str('-')
    try:
        trancscripted = transcr(word)
        print(separator)
        print('|', word, ' --> ', trancscripted, ' ', '|')
        print(separator)
    except IndexError as error:
        print("Dude, that's messed up")