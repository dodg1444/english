from random import randint
from sys import exit
import time
from os import name, system
import requests
from bs4 import BeautifulSoup
import re
user_agent =\
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent': user_agent}


file = open("list.txt", "r")
words_file = file.readlines()

file_transcription = open("transcription.txt", "r")
transcripted_words_file = file_transcription.readlines()


def split_it(some_list, sep):
	new_list = []
	for i in range(len(some_list)):
		splited = some_list[i].split(sep)
		new_list.append(splited)
	return new_list


def english(some_list, language):
	if language == 'en':
		while len(some_list) != 0:
			rand = randint(0, len(some_list)-1)
			chosen_word = some_list[rand][0]
			print(chosen_word, ' [{}]'.format(transcripted_words_dict[chosen_word]))
			word = input()
			words = []
			words = word.split(' ')
			if ' ' in word:
				words.append(word)
			len1 = len(str(some_list))
			for k in range(len(words)):
				if words[k] == 'skip':
					del some_list[rand]
					break
				if words[k] in str(some_list):
					try:
						for j in range(len(some_list[rand])):
							if words[k] == some_list[rand][j]:
								if words[k] > some_list[rand][0]:
									del some_list[rand][j]
									if len(some_list[rand]) == 1:
										del some_list[rand]
					except IndexError:
						pass
			len2 = len(str(some_list))				
			if len1 != len2:
				try:
					if chosen_word == some_list[rand][0]:
						print('Correct! One more: ', some_list[rand][1])
					else:
						print('Correct! ')
				except IndexError:
					print('Correct! ')
			elif len1 == len2:
				try:	
					print('Wrong: ', some_list[rand][1], some_list[rand][2])
				except IndexError:
					print('Wrong: ', some_list[rand][1])				
			print('Words left: ', len(some_list),'\n')

	elif language == 'ru':
		while len(some_list) != 0:
			rand = randint(0, len(some_list)-1)
			chosen_word = ''
			if len(some_list[rand]) == 3:
				chosen_word = some_list[rand][0] + ' ' + some_list[rand][1]
			else:
				chosen_word = some_list[rand][0]
			print(chosen_word)
			eng_word = some_list[rand][-1]
			word = input()
			words = []
			words = word.split(' ')
			if ' ' in word:
				words.append(word)
			len1 = len(str(some_list))
			for k in range(len(words)):
				if words[k] == 'skip':
					del some_list[rand]
					break
				if words[k] in str(some_list):

					try:
						if words[k] == eng_word:
							del some_list[rand]
					except IndexError:
						pass
			len2 = len(str(some_list))				
			if len1 != len2:
				try:
					if some_list[rand][0] in chosen_word:
						print('Correct!  {} [{}]'.format(some_list[rand][1], transcripted_words_dict[eng_word]))
					else:
						print('Correct! [{}]'.format(transcripted_words_dict[eng_word]))
				except IndexError:
					print('Correct! [{}]'.format(transcripted_words_dict[eng_word]))

			elif len1 == len2:
				try:
					print('Wrong: {} [{}]'.format(some_list[rand][-1], transcripted_words_dict[some_list[rand][-1]]))
				except KeyError:
					print('Wrong: {} [None]'.format(some_list[rand][-1]))
		
			print('Words left: ', len(some_list),'\n')



def reversed_list(some_list):
	for i in range(len(some_list)):
		some_list[i].reverse()
	return some_list


def check(some_list):
	for i in range(len(some_list)):
		for j in range(len(some_list[i])):
			if some_list[i][j] == '':
				del some_list[i]


def listing(some_list):
	counter = 0
	while counter != len(some_list):
		if len(some_list[counter]) > 1:
			print('### Page {}, amount of words: {} ###'.format(counter, some_list[counter].count('\n')), '\n', word_list[counter], '\n')
		counter += 1


def making_list(source_list, output_list, amount_of_w0rds):
	string = ''
	k = 0
	while True:
		try:
			for i in range(k, k+amount_of_w0rds):
				string += source_list[i]
			k += amount_of_words
			output_list.append(string)
			string = ''
		except IndexError:
			break
	return output_list


def making_dict(words, dictionary):
	for line in words.splitlines():
		splline = line.split(' - ', 1)
		dictionary[splline[0]] = splline[1]
	return dictionary


def usage(your_sentence):
	if ' ' in your_sentence:
		your_sentence = your_sentence.replace(" ", "+")
	url = 'https://www.collinsdictionary.com/dictionary/english/' + str(your_sentence)
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, features="html.parser")
	parse = soup.find_all(class_="quote")
	parse_synonyms = soup.find_all(class_="form ref")
	reg_en = re.compile("[^a-zA-Z' ]")
	list_of_sentences = []
	synonyms = ''

	for i in range(0, 10):
		try:
			match = re.findall('\>(.*?)\<', str(parse_synonyms[i]).replace('\n', ' '))
			for elem in match:
				if elem != '':
					synonyms += elem+' '
		except IndexError:
			pass

	for i in range(0, 1):
		sentence = ''
		try:
			match = re.findall('\ (.*?)\.<', str(parse[i]).replace('\n', ' '))
			if len(match) == 0:
				print('No sentences for: {}\n'.format(your_sentence))
				return None, None 
			for elem in match:
				if elem != '':
					sentence += elem
			result = sentence.split(">")
			list_of_sentences.append(result[1].lstrip().rstrip())
		except IndexError:
			break

	return synonyms, list_of_sentences


def test(the_list):
	list_of_sentences = []
	synonym_dict = {}
	to_be_deleted = []
	del the_list[-1]
	for i in range(len(the_list)):
		clear_screen()
		print("Loading... Words left: {}".format(len(the_list)-i-1))
		synonyms, list_of_sentences_0 = usage(the_list[i])
		if synonyms and list_of_sentences_0 != None:
			synonym_dict[the_list[i]] = synonyms
			list_of_sentences.append(list_of_sentences_0)
		else:
			to_be_deleted.append(i)
	step = 0
	for i in range(len(to_be_deleted)):
		del the_list[to_be_deleted[i]-step]
		step += 1
	clear_screen()

	while len(list_of_sentences) != 0:
		#print("Here is the dict ----> ", synonym_dict)
		#print("Here is the list ----> ", list_of_sentences)
		#print("Here is the the_list ----> ", the_list)

		random_int = randint(0, len(list_of_sentences)-1)
		if len(list_of_sentences[random_int]) > 1:
			random_int_0 = randint(0, len(list_of_sentences[random_int])-1)
		else:
			random_int_0 = 0
		print(list_of_sentences[random_int][random_int_0].replace(the_list[random_int], '???'))
		input_word = input()
		print('\n')
		if input_word == "hint":
			print('########## Synonyms ##########')
			print(synonym_dict[the_list[random_int]])
			print('##############################\n')
		if input_word == the_list[random_int]:
			print('Correct\n')
			del list_of_sentences[random_int]
			del the_list[random_int]
		elif input_word != 'hint':
			print("Wrong\n")
		print('Words left: {}'.format(len(list_of_sentences)))
	print("Done!\n")


def config_msg():
	print('######## Configuration ########')
	print('Group size: ', amount_of_words)
	print('Amount of words: ', len(words_file))
	print('###############################')


def options(some_list, action, language):
	making_dict(transcripted_words_all[int(action)], transcripted_words_dict)
	some_list = split_it(some_list, '\n')
	some_list = split_it(some_list[int(action)], ', ')
	if language == 'ru':
		reversed_list(some_list)
	check(some_list)
	start_time = time.time()
	english(some_list, language)
	finish_time = str(time.time()-start_time)
	for i in range(len(finish_time)):
		if finish_time[i] == '.':
			print('Time spent: {} seconds'.format(finish_time[0:i+3]))
			break


def clear_screen():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

helpmsg = 'Usage: [xy], where x - number of a page, y - translation direction\number(1 - from english to russian; 0 - from russian to english)\n\n\
chsize [size]		change size of word groups to [size]\n\
show [number]		shows content of the group [number or all]\n\
config 			prints current configuration\n\
exit			guess what\n\
help 			shows this message\n\
clear			clears screen (actually just makes 50 enters\n\
test [number]		test yourself with examples and synonyms (type hint)\n\
\n\n\n\
Hint: You can skip a word by typing <skip> as a translation'


amount_of_words = 10
word_list = []
transcripted_words_dict = {}
transcripted_words_all = []


making_list(words_file, word_list, amount_of_words)
making_list(transcripted_words_file, transcripted_words_all, amount_of_words)

config_msg()

while True:
	action = str(input())
	print('\n')
	input_pair = action.split(' ')
	if len(input_pair) == 2:

		if input_pair[0] == 'chsize':
			amount_of_words = int(input_pair[1])
			word_list = []
			transcripted_words_all = []
			making_list(words_file, word_list, amount_of_words)
			making_list(transcripted_words_file, transcripted_words_all, amount_of_words)

		if input_pair[0] == 'show':
			if input_pair[1] == 'all':
				listing(word_list)
			else:
				number_of_page = input_pair[1]
				print('------------LIST-------------')
				print(word_list[int(number_of_page)])
				print('--------TRANSCRIPTION--------')
				print(transcripted_words_all[int(number_of_page)])

		if input_pair[0] == 'test':
			some_list = split_it(word_list, '\n')
			some_list = split_it(some_list[int(input_pair[1])], ', ')
			some_list_0 = []	 
			for i in range(len(some_list)):
				some_list_0.append(some_list[i][0])
			test(some_list_0)

	elif len(input_pair) == 1:
		if action == 'help':
			print(helpmsg)
		if action == 'exit':
			print('Good bye, old sport')
			time.sleep(1)
			exit()
		if action == 'config':
			config_msg()
		if action == 'clear':
			clear_screen()
		else:
			if len(action) == 2:
				if action[1] == '0':
					options(word_list, action[0], 'ru')
				elif action[1] == '1':
					options(word_list, action[0], 'en')
			if len(action) == 3:
				if action[2] == '0':
					options(word_list, action[0:2], 'ru')
				elif action[2] == '1':
					options(word_list, action[0:2], 'en')
			if len(action) == 4:
				if action[3] == '0':
					options(word_list, action[0:3], 'ru')
				elif action[3] == '1':
					options(word_list, action[0:3], 'en')

file.close()
file_transcription.close()