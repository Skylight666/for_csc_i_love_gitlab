# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from tkinter import *
import tldextract
import os.path
import os
from tkinter import filedialog
import shutil # удаление файлов

# Сделать отчиску папки
# Несколько полей для ссылок
# df.rename
# объединение таблиц
# словари

DICT_CONST = {
'Квалификация' : ['Квалификац'],
'Форма обучения' : ['Форм'],
'Срок обучения' : ['Срок'],
'Специальность' : ['Направлен', 'Cпециально']
}

def change(ke,  dict_with_words=DICT_CONST):
    for k, v in dict_with_words.items():
        if ke in v:
            return k
        return ke

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def clear_button():
    global folder_path
    folder_path.set('')

def get_tables():
    global folder_path

    url = text1.get('1.0', END)

    res = urllib.request.urlopen(url).read().decode('utf-8')

    dom = tldextract.extract(url).domain
    print(dom)

    if not os.path.exists(dom):
        os.makedirs(dom)


    if folder_path.get():
        dom = folder_path.get()
    else:
        dom = os.path.join(os.getcwd(), dom)

    for i, df in enumerate(pd.read_html(url, header=0)):
        for_rename = {k : change(k) for k in df.columns}
        if ''.join(str(i) for i in df.columns).lower().find('напра') >= 0: # search in dict
            df.iloc[5:].rename(columns=for_rename).to_excel(os.path.join(dom, 'table_for_merge_%s.xlsx' % i), index=False)
        df.iloc[5:].rename(columns=for_rename).to_excel(os.path.join(dom, 'garbagbe_%s.xlsx' % i), index=False)


root=Tk()
text1=Text(root,height=7,width=60,font='Arial 14')
text1.pack()
button1=Button(root,text='ok',width=25,height=5,bg='black',fg='red',font='arial 14', command=get_tables)
button1.pack()
folder_path = StringVar()
button2 = Button(text="Browse", command=browse_button)
button2.pack()
button3 = Button(text="Clear path", command=clear_button)
button3.pack()


root.mainloop()
