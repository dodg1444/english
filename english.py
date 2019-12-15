from random import randint
from sys import exit
from time import sleep
from threading import Thread
words_all = ['''''', '''wrist - запястье # list of your words
cultivate - возделывать, культивировать
catchy - броский
compose - сочинять
enormous - огромный 
intrigued - заинтригованный
investigate - исследовать
jealous - завистливый
realize - осознавать
revise - пересмотреть
nixed - отверг
folks - родственники
lousy - поршивый
particular - конкретный
possession - владение
act - действие
adjust - регулировать, приспосабливать
canvas - холст
chalk - мел
cloth - ткань, одежда''', '''kettle - чайник
nail - ноготь, гвоздь
needle - игла
receipt - квитанция
sail - парус
screw - винт
thread - нить
throat - горло
thumb - большой палец руки, листать
hook - крюк, вербовать
horn - рог
pipe - труба
plate - пластина, тарелка
plow - пахать, плуг
stem - стебель, происходить
spade - лопата
sponge - губка
pot - горшок
tray - поднос
pump - насос, качать''', '''whip - кнут, хлестать
account - счет
committee - комитет
degree - уровень, градус, степень
desire - желание
amount - количество
amusement - развлечение
approval - одобрение
apparatus - аппарат
attraction - достопримечательности, привлечение
authority - власть, полномочие
brass - медь, руководство
burst - порыв, взрыв
comparison - сравнение
cork - пробка
cough - кашель
curve - кривая, изгиб
distribution - распределение
doubt - сомнение
debt - долг
digestion - пищеварение
expansion - расширение''', '''harbor - убежище, порт, укрывать
measure - мера, измерять
observation - наблюдение
fold - сложить, складка
grain - зерно
grip - рукоятка, зажимать
firmly - твердо, крепко
insect - насекомое
ink - чернила
mind - ум, возражать
mist - туман
insurance - страховка
linen - льняной, полотно
liquid - жидкость, жидкий
ornament - украшение, украшать''','''excess - лишний
paste - вставить, наклеить
plant - завод, растение, сажать
polish - лак, полировать
rate - темп, скорость
ray - луч
representative - представитель
rub - резина
scale - шкала
servant - слуга
sign - знак, подписывать
slip - промах, скользить
slope - склон
smash - разгром, громить
sneeze - чихать
nap - дремать
stage - этап
statement - заявление
steam - пар
stitch - стежок, шить
stretch - протяжение, растягивать
substance - вещество''','''off - прочь, от
on - на
though - хотя
chief - главный
fertile - плодородный
hang - висеть
past - мимо, прошлый
acid - кислота
fixed - неподвижный
conscious - сознательный''','''equal - равный
frequent - частый
hollow - пустота
probable - возможный
porter - портье
powder - порошок, напудрить
prose - проза''','''tax - налог, облагать налогом
tin - банка
vessel - судно, сосуд
redundant - лишний
twist - поворот, крутить
thick - толстый, густо
violent - жестокий
responsible - ответственный
stiff - жесткий
bitter - горький, жестокий''','''cruel - жестокий
delicate - нежный, тонкий
feeble - слабый
foolish - глупый
loose - свободный
solid - твердый
delicious - вкусный''','''abolish - отменять
addiction - зависимость
amateur - любитель
ambassador - посол
apron - фартук
arrange - организовывать
arrogant - высокомерный
boast - хвастаться
canteen - столовая
celebrity - знаменитость''','''confidence - уверенность
contribute - делать вклад
tribute - дань
correspondence - переписка
craving - страстное желание
crawl - ползать
dedication - верность
dedicate - посвящать
descend - спускаться
deteriorate - ухудшать''','''dismiss - отклонять
dissolve - расстворять
district - район
elaborate - разрабатывать
embarrassment - помеха
emergency - критическое положение
entourage - окружение
evidence - доказательство
extinction - вымирание
famine - голод''','''flood - потоп
generosity - щедрость
gluttony - обжорство
hiccup - икота
humiliate - унижать
interpret - толковать
maintain - поддерживать
mature - зрелый
naughty - непослушный
persuade - убеждать''','''clay - глина
violation - нарушение
negotiate - вести переговоры
contrition - раскаяние
truly - действительно
attend - посещать
nasty - противный
promotion - продвижение
prosecutor - прокурор
quarrel - ссора''','''rapport - хорошее отношение
referee - судья
reference book - справочник
rehearsal - репетиция
remarkable - значительный
resentment - негодование
ruthless - безжалостный
satchel - сумка
spokesman - представитель
squeeze - сжимать''','''stationary - неизменный
sufficient - достаточный
superstition - суеверие
surveyor - землемер
suspect - подозревать
vain - тщеславный
valuable - ценный
withdraw - извлекать
obsession - одержимость
rust - ржаветь''','''confess - признаваться
felony - уголовное преступление
circumstances - обязательства
untenable - ненадежный
rattle - погремушка, греметь
mortgage - ипотечный кредит
spank - шлепок, шлепать
offence - обида, преступление
restroom - уборная
make a sense - иметь смысл''','''noble - благородный
impose - навязывать
aware - знать
envy - зависть, завидовать
acquainted - знакомый
witness - свидетель
mascot - талисман
capable - способный
groom - жених
bride - невеста''','''bargain - сделка
douse - окунать
compassion - сострадание
curious - любопытный
decent - порядочный
bugger - мудак
embrace - объятия, охватывать
spit it out - выкладывай
roam - странствовать
odd - странный''','''eternity - вечность
renege - отрекаться
steep - крутой
torture - пытка, пытать
abandon - покинуть
parley - переговоры
oblivion - забвение
lately - недавно
abasement - унижение
abhor - ненавидеть''','''abrasive - резкий
absolution - освобождение
abstain - воздерживаться
abstemious - скромный
affinity - сродство
affliction - страдание
relent - смягчать
avert - отводить
shatter - разбить
glimmer - мерцание, мерцать''','''affluent - изобильный
alacrity - готовность
excitement - волнение
envelope - конверт
fir tree - ель
dandelion - одуванчик
ham - ветчина
alleviate - облегчать
ambiguous - двусмысленный
animosity - враждебность''','''spot - пятно, определить
demand - требовать
whiskers - бакенбарды
handkerchief - носовой платок
waist - талия
dining - обеденный
properly - должным образом
deaf - глухой
be around - быть рядом
louse - вошь''','''brusque - бесцеремонный, грубый
capricious - капризный
charisma - харизма
upset - опрокидывать
boldness - смелость
complicity - соучастие
comprehensive - всесторонний
concoct - состряпать
counterfeit - подделка
covert - убежище''','''start for - отправляться в
pour - наливать
cellar - погреб
gust - порыв
remembering - запоминающийся
shave - брить
resign - уходить в оставку
reckless - безрассудный
foil - фольга
insult - оскорбление, оскорблять''','''bigot - фанатик
sight - вид
pile - куча
bilk - жулик, обманывать
billow - лавина
beg - просить
purse - кошелек
gleam - мерцать
sober - трезвый
tremble - дрожать''','''broth - бульон
upside down - кверху дном
to faint - потерять сознание
cower - сжиматься
will - воля
I wonder - интересно
afford - позволить себе
distraction - отвлечение
violate - нарушать
scuff - протереться''','''creditable - похвальный
cringe - раболепствовать
cryptic - загадочный
deceive - обманывать
deception - обман
peel - корка
dizzy - головокружительный
broth - бульон
tremble - дрожать
no clue - без понятия''','''consistent - последовательный
talon - коготь
funky - трусливый
chew - жевать
charming - очаровательный
robust - крепкий
ditch - угробить, губить
burden - бремя
loony - чокнутый
catch up - догонять''','''engage - вовлекать
occasion - повод
seal - печать, запечатывать
foretell - предсказывать
errand - поручение, командировка
villainy - злодейство
treason - измена
impale - прокалывать
swirling - завихрение
dubious - сомнительный''','''sorcery - колдовство
heels - каблуки
sprightly - оживленно
filthy - отвратительный
maim - калечить
attain - достигать
quench - утолять жажду
anxious - тревожный
I fancy - мне кажется
giddiness - головокружение''','''cherish - лелеять
behold - созерцать, вот
startle - напугать
intentionally - намеренно
encounter - столкновение, сталкиваться
foreign currency - иностранная валюта
epiphany - прозрение
shy - застенчивый, робкий
lure - приманка, завлекать
demise - кончина''','''blend - смесь, смешивать
decay - распад, распадаться
expel - исключать
fickle - непостоянный
possess - владеть
predisposition - предрасположение
detention - заключение под стражу
wit - остроумие
fascinating - очаровательный
grasp - схватывание, понять''','''menace - угроза, угрожать
rebellion - бунт, восстание
prod - тычок, подталкивать
persistence - упорство
banish - прогонять
dimple - ямочка
ancestors - предки
pester - донимать
contest - конкурс
imply - подразумевать''','''tip - подсказка, чаевые
immediately - немедленно
humid - влажный
midget - карлик
yell - вопить, кричать
inception - начало
conjure - колдовать
vicious - злобный
fraud - мошенник
innocent - невинный''','''haste - поспешность
chores - хлопоты
prosperity - процветание
revelation - откровение
consequence - последствие
remedy - средство, лекарство
boar - кабан
intimidate - запугивать
haunt - преследовать
avalanche - лавина, обвал''','''treacherous - предательский, коварный
sane - здравомыслящий
fornicate - блудить
wicked - круто, клево
abduct - похищать
partake - принимать участие
bona_fide — добросовестный
consider - рассматривать возможность
wack - псих
eviction - выселение
stroll - прогулка''','''affair - дело
propose - предлагать
merely - просто
wrap - обертка, заворачивать
contenders - претенденты
couch - диван
stove - плита
serenity - спокойствие
dork - придурок
apparently - по всей видимости''','''renovation - ремонт
feign - симулировать
vigilant - бдительный
cubs - детеныши
obey - подчиниться
deliberately - сознательно
jeopardize - подвергать опасности
meticulous - дотошный
endure - терпеть
ferocious - свирепый''','''bleak - мрачный
frolic - резвость, резвиться
evenly - равномерно
sin - грех, грешить
legit - законный
conform - соответствовать
lush - пышный
fidget - непоседа, ерзать
elusive - неуловимый
inevitable - неизбежный''','''exhausted - истощен
sweep - сметать
seduce - соблазнять
malware - вредоносные программы
flaw - недостаток
sobbing - рыдания
neat - опрятный
fugitive - беглец
commitment - обязательство
obtain - получать''','''caveat - предостережение
sore - огорченный, воспаленный
desperate - отчаянный
gullible - доверчивый
peek - заглядывать
devastating - разрушительный, опустошительный
complicit - замешанный
implicit - неявный
explicit - явный
gently - осторожно''','''mishap - несчастье
prophet - пророк
hasty - поспешный
preoccupied - озабоченный
bruise - синяк
enchanted - околдовывать, очаровывать
tidings - новости
my condolences - мои соболезнования
courtesy - вежливость
interfere - вмешиваться''','''mock - высмеивать
precise - точный
virtuous - добродетельный
prudence - предусмотрительность
disruption - нарушение, срыв
contaminate - загрязнять, осквернять
get along - ладить
gossipy - болтливый
capacity - вместимость
insane - ненормальный, безумный''','''threshold - порог, предел
vulnerability - уязвимость
vast - простор, обширный
assignment - задание, назначение
intertwine - переплетаться, закручиваться
nod - кивок, кивать
delight - восторг, восхищаться
enlighten - просветить
substitute - замена
nausea - тошнота''', '''worship - поклонение, поклоняться
severe - тяжелый, серьезный
preach - прововедовать
considerate - внимательный, тактичный
exhilarate - веселить, оживлять
obnoxious - противный
mischief - вред
venture - авантюра, осмеливаться
lucrative - прибыльный
tailor - портной''', '''sincerity - честность
diligent - прилежный
grief - горе
resolve - разрешить
condemn - осуждать, обрекать
devotion - преданность
avail - польза
delicacy - лакомство
rambunctious - раздражительный
acumen - сообразительность''', '''willing - готов
truce - передышка
splendid - замечательный
stalk - преследовать
accompany - сопровождать
inferior - низший
assault - нападение, нападать
steer - управлять
entity - объект
sophisticated - утонченный''', '''repent - каяться
quaint - причудливый
pry - подглядывать
essentially - по существу
adversary - противник, состязательный
mitigate - смягчать, уменьшать
stork - аист
shindig - шумная вечеринка
cuss - ругаться
modest - скромный''', '''cohabitant - сожитель
cohabit - сожительствовать
perv - извращенец
evasive - уклончивый
unease - беспокойство
profound - глубокий
overwhelmed - перегруженный
behoove - надлежать
inbound - входящий
outbound - исходящий''', '''interception - подслушивание, перехват
accustomed - привыкший
hood - капюшон, капот
pace - расхаживать
efficient - эффективный
harassment - домогательство
clarify - прояснить
haystack - стог сена
perceptive - восприимчивый
observe - наблюдать''', '''aptitude - способность
hence - следовательно
fallacy - заблуждение
ponder - обдумать
testament - завет
porcupine - дикобраз
pedestrian - пешеход
crate - коробка
blurry - размыто
squint - прищуриваться''', '''infestation - заражение, нашествие
postpone - откладывать
uncanny - зловещий
docile - пассивный
tenacious - упорный
ambiance - атмосфера
perplexed - озадачен
masseuse - массажист
narrate - рассказывать, озвучивать
kidnap - похищать''', '''perturbation - возмущение
accomplished - свершившийся, опытный
equity - равенство
ennui - скука
covenant - соглашение
dicey - рискованный
in lieu of - вместо
notch - метка, зарубка
can't put my finger on you - не могу понять тебя
attorney - адвокат''', '''stand by - ожидать
grifter - развод, афера
ordinance - постановление, указ
overhaul - пересмотр, перестройка
prowler - вор, бродяга
heap - груда, куча
coy - застенчивый, робкий 
camcorder - видеокамера
incorrigible - неисправимый
soaring - парящий, высокий''', '''concise - краткий, сжатый
gory - окрававленный
standoff - противостояние, тупик
cleanse - очистить, диета
count on me - рассчитывать на меня
stumble - спотыкаться
con man - аферист
boisterous - шумный
disgruntled - недовольный, рассерженный
pledge - обещание, обещать''']

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
