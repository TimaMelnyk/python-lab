#-*- coding: utf-8 -*-
import os
import sys
import time
import pandas as pd
import  urllib2

def maxVHI(df, year):
    print(df[(df['year']==year)])
    x = df[(df['year']==year)]
    return x['VHI'].max()
def minVHI(df, year):
    x = df[(df['year']==year)]
    return x['VHI'].min()
def VHI(df):
    print(df[(df['VHI']< 15)])

def download(choose):
    print('Downloading...')
    if not choose:
        print('Bye')
    if choose<10:
        url = mainurl + '0{}'.format(choose) + txt
    else:
        url = mainurl + '{}'.format(choose) + txt
    vhi_url = urllib2.urlopen(url)
    out = open(filename,'wb')
    out.write(vhi_url.read())
    out.close()
    print('Done')
def search_num(answer):
    for reg,val in region_num.items():
        if answer == reg:
            answer = val
            break
    print(answer)
    return answer
def show(df,*year):
    print df[:3]
    if year:
        Max = maxVHI(df,year)
        Min = minVHI(df,year)
        print('Найменше значення VHI: {}\n Найбільше значення VHI: {}\n'.format(Min,Max))
def csv(filename,*year): 
    df = pd.read_csv(filename, index_col=False, header=1)
#    df = df.rename(columns={'': ''})
    if year:
        show(df,year)
    else:
        show(df)
    return df

target_dir = '/home/tima/VHI'
region = target_dir + os.sep + 'DATE:' + time.strftime('%Y.%m.%d')
now = '_' + 'TIME:' + time.strftime('%H:%M:%S')
mainurl = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
txt = '.txt'
filename = region + now
choose = 0
region_list = ['Вінницька','Волинська','Дніпропетровська','Донецька','Житомирська','Закарпатська','Запорізька','Івано-Франківська','Київська',
'Кіровоградська','Луганська','Львівська','Миколаївська','Одеська','Полтавська','Рівенська','Сумська','Тернопільська',
'Харківська','Херсонська','Хмельницька','Черкаська','Чернівецька','Чернігівська','Республіка Крим']
region_num = {
    'Вінницька':'24',
    'Волинська':'25',
    'Дніпропетровська':'5',
    'Донецька':'6',
    'Житомирська':'27',
    'Закарпатська':'23',
    'Запорізька':'26',
    'Івано-Франківська':'7',
    'Київська':'11',
    'Кіровоградська':'13',
    'Луганська':'14',
    'Львівська':'15',
    'Миколаївська':'16',
    'Одеська':'17',
    'Полтавська':'18',
    'Рівенська':'19',
    'Сумська':'21',
    'Тернопільська':'22',
    'Харківська':'8',
    'Херсонська':'9',
    'Хмельницька':'10',
    'Черкаська':'1',
    'Чернівецька':'3',
    'Чернігівська':'2',
    'Республіка Крим':'4',
}
i = 0
print('Області : \n')
for name in region_list:
    i = i + 1
    print ('{}. {}'.format(i,name))

while choose>25 or choose<1:
    choose = int(input('Оберіть необхідний регіон (1-25): '))
    answer = region_list[choose-1]
    answer = search_num(answer)
download(answer)
yn = True
while yn:
    print('1. За какой год Вы хотите узнать мин макс VHI?\n 2. Зчитати файл з фрейму\n 3. Знайти VHI <15\n')
    ans = int(input('вийти(4),Введіть варіант: '))
    if ans==2: 
        csv(filename)
    if ans==1:
        year = int(input('За какой год Вы хотите узнать мин макс VHI: '))
        print(year)
        a = csv(filename)
        Max = maxVHI(a,year)
        Min = minVHI(a,year)
        print('Найменше значення VHI: {}\n Найбільше значення VHI: {}\n'.format(Min,Max))
    if ans==3:
        a = csv(filename)
        VHI(a)
    if ans==4:
        print('Ok, Bye.')
        break






















#print(df[(df['year']==2000) & (df['week']==18)])

# if len(comment) == 0:
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' + \
#              comment.replace(' ','+') + '.zip'

# if not os.path.exists(today):   # Проверка и создание папки
#     os.mkdir(today)
#     print('Папка создана')
# else:
#     print('Catalog has already exist')

# df[(df['year']==2000) & (df['week']==18)]

# zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
# if os.system(zip_command) == 0:
#     print('zip file was created like',target)
# else:
#     print("ERROR")