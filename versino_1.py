name = input('Как вас зовут? -> ')
print('Привет', name + '!')
print(name, ', давай поиграем в World of Tanks', sep='')

my_tanks = int(input('Сколько танков у вас в ангаре -> '))
favorite = input('На каких танках ты предпочитаешь играть? -> ')

print('Вас зовут: ', name, '. У вас ', my_tanks, ' танков и вы предпочитаете играть на ', favorite, sep='')

print('Начнем игру!')
my_choice = input('На каком виде техники вы собираетесь играть? (лт, ст, тт, пт, пт-сау) -> ')

print('Запущен балансировщик игры')
green_lt = int(input('Сколько лт в команде зеленых -> '))
red_lt = int(input('Сколько лт в команде красных -> '))
green_st = int(input('Сколько ст в команде зеленых -> '))
red_st = int(input('Сколько ст в команде красных -> '))
green_tt = int(input('Сколько тт в команде зеленых -> '))
red_tt = int(input('Сколько тт в команде красных -> '))
green_pt = int(input('Сколько пт в команде зеленых -> '))
red_pt = int(input('Сколько пт в команде красных -> '))
green_pt_say = int(input('Сколько пт-сау в команде зеленых -> '))
red_pt_say = int(input('Сколько пт-сау в команде красных -> '))

green_tanks = green_lt + green_st + green_tt + green_pt + green_pt_say
red_tanks = red_lt + red_st + red_tt + red_pt + red_pt_say
all_tanks = green_tanks + red_tanks

print('Количество танков в команде зеленых:', green_tanks)
print('Количество танков в команде красных:', red_tanks)
print('Всего танков в игре:', all_tanks)

from time import sleep

start = int(input('Сколько секунд до начало игры -> '))
sleep(start)
print('Игра началась! В бой!')
time = int(input('Сколько времени будуте продолжаться бой -> '))
sleep(time)
print('Игра завершилась. Вы победили!!!')
