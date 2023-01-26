login = input('Введите логин -> ')
print(login + ',', 'добро пожаловать в игру')
print('Запущен балансировщик игры')

lt = int(input('Введите сколько лт в бою -> '))
lt_shells = int(input('Введите сколько снарядов находится в одном лт -> '))

st = int(input('Введите сколько ст в бою -> '))
st_shells = int(input('Введите сколько снарядов находится в одном ст -> '))

tt = int(input('Введите сколько тт в бою -> '))
tt_shells = int(input('Введите сколько снарядов находится в одном тт -> '))

lt_total_shells = lt * lt_shells
st_total_shells = st * st_shells
tt_total_shells = tt * tt_shells

print(lt_total_shells, 'снарядов в лт')
print(st_total_shells, 'снарядов в ст')
print(tt_total_shells, 'снарядов в тт')

# Продвинутый уровень
lt_speed = int(input('Введите скорость км/ч лт -> '))
st_speed = int(input('Введите скорость км/ч ст -> '))
tt_speed = int(input('Введите скорость км/ч тт -> '))

print('через 4 часа лт проедет', lt_speed*4, 'км')
print('78 километров ст проедет через', 78/st_speed, 'часов')
time = int(input('Введите время -> '))
print('через', time, 'часов тт проедет', tt_speed * time, 'км')

print(12*lt_speed, 'км проедет лт за 12 часов')
print(12*st_speed, 'км проедет ст за 12 часов')
print(12*tt_speed, 'км проедет тт за 12 часов')