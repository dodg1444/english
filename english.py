from random import randint
from sys import exit
from time import sleep
from threading import Thread
words_all = ['''''', '''word - слово''']

words_dict = {}


def making_dict(words):
    for line in words.splitlines():
        splline = line.split(' - ', 1)
        words_dict[splline[0]] = splline[1]


def english_def(dict1, dict2, words):
    while len(dict1) > 0:
        rand = randint(1, len(dict1))
        chosen_word = dict1.keys()
        key_list = list(chosen_word)
        print(key_list[rand - 1])
        g = str(input())
        if g in str(dict2.keys()):
            print('Right answer: ', dict1[key_list[rand - 1]])
            try:
                del dict1[dict2[g]]
            except KeyError:
                pass
            print('Words left: ', len(dict1))
        else:
            print('Wrong answer; ', dict1[key_list[rand - 1]])
        if g == 'list':
            print(words)


def act_1(word_list, word_dict):
    making_dict(word_list)
    reversed_words_dict = {words_dict[k]: k for k in words_dict}
    english_def(word_dict, reversed_words_dict, word_list)
    print('Good job!')
    exit()


def act_0(word_list, word_dict):
    making_dict(word_list)
    reversed_words_dict = {words_dict[k]: k for k in words_dict}
    english_def(reversed_words_dict, word_dict, word_list)
    exit()


def listing(some_list):
    counter = 0
    while counter != len(some_list):
        if len(some_list[counter]) > 1:
            print('### Page {}, amount of words: {} ###'.format(counter, some_list[counter].count('-')), '\n', words_all[counter], '\n')
        counter += 1


def timer(k):
    k = int(k)
    while main_thread.is_alive():
        k += 1
        sleep(1)
    print('Time spent:', k, 'seconds')
    if k in range(0, 60):
        print('Weelll done!', '\n', 'Keep it up!')
    if k in range(61, 75):
        print('Your assessment is B', '\n', 'Been better')
    if k in range(76, 90):
        print('It is C. Nothing to be proud, actually')
    if k >= 91:
        print('Go read books, kid')


def start():
    main_thread.start()
    timer_thread.start()


def big_list():
    print('Type the numbers of the pages where to start and end ')
    start_from = input()
    end_on = input()
    if end_on == 'last':
        end_on = len(words_all)
    big_listing = '''crutch - костыль'''  # It actually is
    for i in range(int(start_from), int(end_on)):
        if len(words_all[i]) > 0:
            big_listing = big_listing + '\n' + words_all[i]
    return big_listing


def threading(function, kwargs1, kwargs2):  # Not ready yet
    main_thread = Thread(target=function, name='t1',
                         kwargs={'word_list': kwargs1, 'word_dict': kwargs2})
    timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
    start()


print('Enter number of the page and language (1- from english to russian; 0-from russian to english)')
print('Do you wanna see any pages? ')
action = str(input())
if 'yes' in action:
    print('Which of them? ')
    number_of_page = input()
    if 'all' in number_of_page:
        listing(words_all)
    else:
        if int(number_of_page) >= len(words_all):
            print('Are you fucking blind or what?', '\n', 'There is no such page, start over')
        else:
            print(words_all[int(number_of_page)])
elif action not in 'yes':
    print('Well, you\'re welcome. Go on. ')
#elif (action is 'yes') == 0:
#    print('Well, you\'re welcome. Go on. ')

action = str(input())
if len(action) == 2:
    if int(action[0]) <= (len(words_all) - 1):
        if action[1] == '0':
            main_thread = Thread(target=act_0, name='t1',
                                 kwargs={'word_list': words_all[int(action[0])], 'word_dict': words_dict})
            timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
            start()
        elif action[1] == '1':
            main_thread = Thread(target=act_1, name='t1',
                          kwargs={'word_list': words_all[int(action[0])], 'word_dict': words_dict})
            timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
            start()
elif len(action) == 3:
    if int(action[0:2]) <= (len(words_all)-1):
        if action[2] == '0':
            main_thread = Thread(target=act_0, name='t1',
                          kwargs={'word_list': words_all[int(action[0:2])], 'word_dict': words_dict})
            timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
            start()
        elif action[2] == '1':
            main_thread = Thread(target=act_1, name='t1',
                          kwargs={'word_list': words_all[int(action[0:2])], 'word_dict': words_dict})
            timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
            start()

elif 'exam' in action:
    if action[-1] == '0':
        big_list = big_list()
        main_thread = Thread(target=act_0, name='t1',
                             kwargs={'word_list': big_list, 'word_dict': words_dict})
        timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
        start()
    if action[-1] == '1':
        big_list = big_list()
        main_thread = Thread(target=act_1, name='t1',
                             kwargs={'word_list': big_list, 'word_dict': words_dict})
        timer_thread = Thread(target=timer, name="t2", kwargs={"k": "0"})
        start()
