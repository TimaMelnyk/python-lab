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
        print('������� ���祭�� VHI: {}\n ����?��� ���祭�� VHI: {}\n'.format(Min,Max))
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
region_list = ['�?����쪠','������쪠','��?�ய��஢�쪠','�����쪠','��⮬���쪠','����௠��쪠','�����?�쪠','?����-�࠭�?��쪠','�����쪠',
'�?஢��ࠤ�쪠','�㣠��쪠','��?��쪠','���������쪠','����쪠','���⠢�쪠','�?����쪠','���쪠','��୮�?���쪠',
'���?��쪠','���ᮭ�쪠','����쭨�쪠','��ઠ�쪠','���?���쪠','���?�?��쪠','���㡫?�� �ਬ']
region_num = {
    '�?����쪠':'24',
    '������쪠':'25',
    '��?�ய��஢�쪠':'5',
    '�����쪠':'6',
    '��⮬���쪠':'27',
    '����௠��쪠':'23',
    '�����?�쪠':'26',
    '?����-�࠭�?��쪠':'7',
    '�����쪠':'11',
    '�?஢��ࠤ�쪠':'13',
    '�㣠��쪠':'14',
    '��?��쪠':'15',
    '���������쪠':'16',
    '����쪠':'17',
    '���⠢�쪠':'18',
    '�?����쪠':'19',
    '���쪠':'21',
    '��୮�?���쪠':'22',
    '���?��쪠':'8',
    '���ᮭ�쪠':'9',
    '����쭨�쪠':'10',
    '��ઠ�쪠':'1',
    '���?���쪠':'3',
    '���?�?��쪠':'2',
    '���㡫?�� �ਬ':'4',
}
i = 0
print('������? : \n')
for name in region_list:
    i = i + 1
    print ('{}. {}'.format(i,name))

while choose>25 or choose<1:
    choose = int(input('����?�� �����?���� ॣ?�� (1-25): '))
    answer = region_list[choose-1]
    answer = search_num(answer)
download(answer)
yn = True
while yn:
    print('1. �� ����� ��� �� ��� 㧭��� ��� ���� VHI?\n 2. ���� 䠩� � �३��\n 3. ����� VHI <15\n')
    ans = int(input('����(4),����?�� ���?���: '))
    if ans==2:
        a = csv(filename)
        # show(a)
        plott(a)
    if ans==1:
        year = int(input('�� ����� ��� �� ��� 㧭��� ��� ���� VHI: '))
        print(year)
        a = csv(filename)
        show(a)
        Max = maxVHI(a,year)
        Min = minVHI(a,year)
        print('������� ���祭�� VHI: {}\n ����?��� ���祭�� VHI: {}\n'.format(Min,Max))
    if ans==3:
        a = csv(filename)
        a = show(a)
        VHI(a)
    if ans==4:
        print('Ok, Bye.')
        break
