import random


with open('man_name', 'r') as f:
    name_man = [i.rstrip() for i in f]
with open('woman_name', 'r') as f:
    name_woman = [i.rstrip() for i in f]
with open('top_second_names', 'r') as f:
    name_second = [i.rstrip() for i in f]


def woman():
    count = 1
    while count < 100:
        print(random.choice(name_woman) + ' ' + random.choice(name_second) + 'а')
        count += 1

def man():
    count = 1
    while count < 100:
        print(random.choice(name_man) + ' ' + random.choice(name_second))
        count += 1

def launch():
        user_input = input()
        types[user_input]()

types = {"m":man,
         "w":woman
        }

print('Имя женщины или мужчины? Введи w или m: ')

try:
    launch()
except:
    print("Введен неверный ответ")
