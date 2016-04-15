#-*- coding: cp866 -*-

import time
import pandas as pd
import  urllib2
import re
import matplotlib.pyplot as plt
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
    out = open(filename, 'w')
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
    frame_columns = df.columns.values
    for i in range(0, len(df.columns.values)):
        frame_columns[i] = re.sub('[^A-Za-z0-9]+', '', frame_columns[i])
    df.columns = frame_columns
    df = df.loc[(df['VHI'] != -1)]
    print df[:3]
    if year:
        Max = maxVHI(df,year)
        Min = minVHI(df,year)
        print('Найменше значення VHI: {}\n Найб?льше значення VHI: {}\n'.format(Min,Max))
    return df
def csv(filename,*year):
    df = pd.read_csv(filename, index_col=False, header=1)
#    df = df.rename(columns={'': ''})
    if year:
        show(df,year)
    else:
        show(df)
    return df

def plott(df):
    frame = df.loc[(df['year'] == 2015)]
    y = frame[['VHI']]
    x = frame[['week']]
    plt.plot(x,y)
    plt.show()
target_dir = 'C:/workspace'
region = target_dir + '/' + 'DATE_' + time.strftime('%Y.%m.%d')
now = '_' + 'TIME_' + time.strftime('%H.%M.%S')
mainurl = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
txt = '.txt'
filename = region + now
choose = 0
region_list = ['В?нницька','Волинська','Дн?пропетровська','Донецька','Житомирська','Закарпатська','Запор?зька','?вано-Франк?вська','Київська',
'К?ровоградська','Луганська','Льв?вська','Миколаївська','Одеська','Полтавська','Р?венська','Сумська','Терноп?льська',
'Харк?вська','Херсонська','Хмельницька','Черкаська','Черн?вецька','Черн?г?вська','Республ?ка Крим']
region_num = {
    'В?нницька':'24',
    'Волинська':'25',
    'Дн?пропетровська':'5',
    'Донецька':'6',
    'Житомирська':'27',
    'Закарпатська':'23',
    'Запор?зька':'26',
    '?вано-Франк?вська':'7',
    'Київська':'11',
    'К?ровоградська':'13',
    'Луганська':'14',
    'Льв?вська':'15',
    'Миколаївська':'16',
    'Одеська':'17',
    'Полтавська':'18',
    'Р?венська':'19',
    'Сумська':'21',
    'Терноп?льська':'22',
    'Харк?вська':'8',
    'Херсонська':'9',
    'Хмельницька':'10',
    'Черкаська':'1',
    'Черн?вецька':'3',
    'Черн?г?вська':'2',
    'Республ?ка Крим':'4',
}
i = 0
print('Област? : \n')
for name in region_list:
    i = i + 1
    print ('{}. {}'.format(i,name))

while choose>25 or choose<1:
    choose = int(input('Обер?ть необх?дний рег?он (1-25): '))
    answer = region_list[choose-1]
    answer = search_num(answer)
download(answer)
yn = True
while yn:
    print('1. За какой год Вы хотите узнать мин макс VHI?\n 2. Зчитати файл з фрейму\n 3. Знайти VHI <15\n')
    ans = int(input('вийти(4),Введ?ть вар?ант: '))
    if ans==2:
        a = csv(filename)
        # show(a)
        plott(a)
    if ans==1:
        year = int(input('За какой год Вы хотите узнать мин макс VHI: '))
        print(year)
        a = csv(filename)
        show(a)
        Max = maxVHI(a,year)
        Min = minVHI(a,year)
        print('Найменше значення VHI: {}\n Найб?льше значення VHI: {}\n'.format(Min,Max))
    if ans==3:
        a = csv(filename)
        a = show(a)
        VHI(a)
    if ans==4:
        print('Ok, Bye.')
        break
