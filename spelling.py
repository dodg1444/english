import requests
from bs4 import BeautifulSoup
import re
from pythonping import ping
user_agent =\
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent': user_agent}


def transcr(your_word):
    url = 'https://www.macmillandictionary.com/dictionary/british/' + str(your_word)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_by_tag = soup.find("span", {"class": "PRON show_less"})
    match = re.findall('\>(.*?)\<', str(soup_by_tag))
    return match[2]


def usage(your_sentence):
    if ' ' in your_sentence:
        your_sentence = your_sentence.replace(" ", "+")
    url = 'https://context.reverso.net/translation/english-russian/' + str(your_sentence)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    parse = soup.find_all(class_="example")
    reg_en = re.compile("[^a-zA-Z' ]")
    reg_ru = re.compile('[^а-яА-Я ]')
    result_dict = {}
    for i in range(0, 5):
        result = ''
        match = re.findall('\>(.*?)\<', str(parse[i]).replace('\n', ' '))
        for elem in match:
            if elem != '':
                result += elem
        result.split()
        result_0 = ' '.join(result.split())
        result_ru = reg_ru.sub('', result_0).replace('  ', '')
        result_en = reg_en.sub('', result_0).replace('  ', '')
        result_dict[result_en] = result_ru
    for key in result_dict:
        print("%s -> %s" % (key, result_dict[key]))


in_progress = True
print("Type 'stop' to stop (Wow i wouldn't figured it out on my own)")
while in_progress:
    print('\n', 'Type "0" for transcription and "1" for usage', '\n')
    input_ = input()
    if input_ == '0':
        print('Input your fucking word')
        word = input()
        if len(word) > 3:
            lenght = 2 * len(word) + 12
        else:
            lenght = 2 * len(word) + 13
        separator = str()
        for i in range(0, lenght):
            separator = separator + str('-')
        try:
            trancscripted = transcr(word)
            print(separator)
            print('|', word, ' --> ', trancscripted, ' ', '|')
            print(separator)
        except IndexError as error:
            print("Dude, that's messed up")
    if input_ == '1':
        print('Input your sentence')
        sentence = input()
        usage(sentence)
    if input_ == "stop" or input_ == "Stop":
        in_progress = False
        print("Okay, asshole")
