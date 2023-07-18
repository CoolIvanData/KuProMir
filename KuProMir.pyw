#            <=>-< KuProMir >-<=>
# Проект со всеми его ветвями начет в 2021г.
# С того момента он сменил уже 2 названия, кардинально менялась логика и дизайн.
# Всё менялось, кроме автора и цели...
# И теперь есть - KuProMir
# 
# KuProMir:
#  Это проект в котором использованы (мои) передовые знания
#  Это проект в котором впервые был задействован GitHub
#  Это проект в котором впервые была создана иконка
#  Это проект в котором я развивался вместе сним 
# 
# 
# автор проекта: 
#               CoolIvanData (21,05,2010)
#   
# Проект принадлежит:
#                    CIDADM(не офиц. команда программистов)


#импортирую библиотеки
import tkinter as tk
from tkinter import *
from cProfile import label
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from time import sleep
#конец




#создаю окно
window = Tk()
#название окна
window.title("KuProMir")
#размеры окна
window.geometry('232x200+250+300')
#Цвета окна
window.config(bg='white')






#оси по которым будет двигаться перо
#горизональ
x = 0
#вертикаль
y = 0

pol_per = 0 #положение пера 0=поднято 1=опущино
color_per = "черный" #цвет пера поумолчанию
hd = 1 #Поумолчанию  ход пера
error = 0 #Кол-во ошибок
kod_osn_shert = 'использовать Чертежник \nалг \nнач  \n'#Основа для чертежника
kod_osn_robot = 'использовать Робот \nалг \nнач  \n'#Основа для чертежника
kod =  '' #Что нужно вставить в окно с кодом
nom_str = 4 #Номер строки куда вставить
razm_shrifta = 10
color_per_dizin = 'green'
rezim = 1 #1 = Чертежник; 2 = Робот;

#Параметры кнопок 
razm_knopok = 26 #Размер ширины и высоты

xcentre = .24 #Расположение центра по горизонтали
ycentre = .40 #Расположение центра по вертикали 
xleft = .13 #Расположение Левого ряда по горизонтали
xright = .35 #Расположение Правого ряда по горизонтали
yupper = .27 #Расположение Верхнего ряда по вертикали
ylower = .53 #Расположение Нижнего ряда по вертикали




def pod_per(): #Логиика поднятия пера
    global pol_per
    pol_per += 1
def opy_per(): #Логиика ведения пера
    global pol_per
    pol_per -= 1

#Логиика кардинат пера
def ver(): #Логиика смещения кардинат пера в верх
    global y
    y += hd

def niz(): #Логиика смещения кардинат пера в низ
    global y
    y -= hd

def lev(): #Логиика смещения кардинат пера в лево
    global x
    x -= hd

def pra(): #Логиика смещения кардинат пера в вправо
    global x
    x += hd





# функции для обработки пунктов меню
# Пункт меню: Создать
def new_win_shert():
  global kod
  global text
  global nom_str
  global pol_per
  global color_per
  global close_win
  win = Toplevel(window)
  win.title("Чертежник")
  #min.minsize(width=250+500, height=220+300)
  win.geometry('250x220+485+300')
  kod = ''
  nom_str = 4
  text = ScrolledText(win, width=33, font='Gropled, 9'#, fg='green', bg='black'
                      )
  text.insert('1.0', kod_osn_shert)
  text.pack(fill=BOTH, side=LEFT, expand=True)
  text.insert(f'{nom_str}.0', kod)
  text.insert(END, "кон")
  btn_per = Button(window, text="⨷", fg='red', bg='black', command=clicked_per)
  btn_per.grid(column=5, row=5, ipady=1, ipadx=1)
  btn_per.place(relx = xcentre, rely = ycentre, width=razm_knopok, height=razm_knopok)
  pol_per = 0
  color_per = "черный" #цвет пера
  win.resizable(width=False, height=True)

  for kod in range(1):
    sleep(1)
    win.update() 

# Пункт меню: Выход
def close_window():
  window.destroy()


#Увеличить размер шрифта
def yvel_razm():
  global razm_shrifta
  razm_shrifta += 1
 

#уменьшить размер шрифта
def ymen_razm():
  global razm_shrifta
  razm_shrifta -= 1

# Пункт меню: Справка
def about():
  win = Toplevel(window)
  win.geometry("150x120")
  Label(win, text='''Название программы:
   KuProMir ''').pack()
  Label(win, text='''Версия программы 
2.9.3.1''').pack()
  Label(win, text='''Написанна программа на
Python''').pack()
  Label(win, text="Автор: CoolIvanData").pack()
  win.resizable(width=False, height=False)

# Пункт меню: О программе
def about1():
  win = Toplevel(window)
  win.geometry("154x120")
  text = ScrolledText(win, width=33, font=f'Gropled, 10')
  text.insert('1.0', ''' 
   
    
     
      
       
        
         #fhlibhjp'lp{"NPBOv/yoj'ih;ugliyutcjyxhtsrdfi6h8uj9i'9h;ugoyxr7d80upih/.lhvkgxyrud8p9[oj/i;l]}
          
           
            
             
              
               
                 ''')
  text.pack(fill=BOTH, side=LEFT, expand=True)


# создаем объект меню на главном окне
m = Menu(window)

# окно конфигурируется с указанием меню для него
window.config(menu=m)

# создается пункт меню с размещением на основном меню (m)
fm = Menu(m#, bg='black', fg='red'
          )
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Открыть...")
fm.add_command(label="Создать код", command=new_win_shert)
fm.add_command(label="Сохранить...")

# вложенное меню
nfm = Menu(fm#, bg='black', fg='red'
           )
fm.add_cascade(label="Import      →", menu=nfm)
nfm.add_command(label="Image")
nfm.add_command(label="Text")

fm.add_command(label="Выход", command=close_window)

# второй пункт меню
km = Menu(m#, bg='black', fg='green'
          )
m.add_cascade(label="Код", menu=km)
km.add_command(label="Новый код Чертежника",  command=new_win_shert)
km.add_command(label="Новый код Робота")


# третий пункт меню
hm = Menu(m)
m.add_cascade(label="?", menu=hm)
hm.add_command(label="Справка", command=about)
hm.add_command(label="О программе", command=about1)

#---------------------------------------------------------------------------------------------------------------

def st_t_print():
    global kod
    global text
    global nom_str
    kod = f'сместиться в точку({x},{y})\n'
    text.insert(f'{nom_str}.0', kod) 
    nom_str += 1





def clicked_ver():
    ver()
    st_t_print()
    

def clicked_niz():
    niz()
    st_t_print()

def clicked_lev():
    lev()
    st_t_print()

def clicked_pra():
    pra()
    st_t_print()


def clicked_ver_pra():
    ver()
    pra()
    st_t_print()

def clicked_niz_lev():
    niz()
    lev()
    st_t_print()

def clicked_lev_ver():
    lev()
    ver()
    st_t_print()

def clicked_pra_niz():
    niz()
    pra()
    st_t_print()


def clicked_per():
    global kod
    global text
    global  nom_str
    if pol_per == 0:
        pod_per()
        btn_per = Button(window, text="⨷", fg='green', bg='black', command=clicked_per) 
        btn_per.grid(column=5, row=5, ipady=1, ipadx=1)
        btn_per.place(relx = xcentre, rely = ycentre, width=razm_knopok, height=razm_knopok)
        kod = 'опустить перо\n'
        text.insert(f'{nom_str}.0', kod)
        nom_str += 1
    elif pol_per == 1:
        opy_per()
        btn_per = Button(window, text="⨷", fg='red', bg='black', command=clicked_per)
        btn_per.grid(column=5, row=5, ipady=1, ipadx=1) 
        btn_per.place(relx = xcentre, rely = ycentre, width=razm_knopok, height=razm_knopok)
        kod = 'поднять перо\n'
        text.insert(f'{nom_str}.0', kod)
        nom_str += 1


lbl = Label(window, text="KuProMir", font=("Gropled", 29), bg='white', fg='black')
lbl.grid(column=0, row=0)
lbl.place(relx = .01, rely = .01)

avt = Label(window, text="CoolIvanData", font=("Gropled", 9), bg='white', fg='black')
avt.grid(column=0, row=0)
avt.place(relx = .65, rely = .92)

txt = Entry(window,width=5, bg='white', fg='black')  
txt.grid(column=4, row=3, ipady=5, ipadx=10)
txt.place(relx = .81, rely = .74, relwidth=0.50, relheight=.09)


rown1 = Label(window, text='''

''', bg='white')
rown1.grid(column=1, row=2)
rown2 = Label(window, text='                     ', bg='white') 
rown2.grid(column=2, row=3)
rown3 = Label(window, text='     ', bg='white')


#                                            Код вылезаюшего списка: 
languages = ['черный','зеленый','желтый','красный','фиолетовый','оранжевый','синий','голубой','белый']
# по умолчанию будет выбран первый элемент из languages
languages_var = StringVar(value=languages[0]) 



combobox = ttk.Combobox(textvariable=languages_var, values=languages, width=12, state="readonly")
combobox['state'] = 'readonly'
combobox.grid(column=10, row=10)
combobox.place(relx = .59 , rely = .83)
#Плашка из списка по умолчанию
combobox.current(0)

# Что выбрал пользователь =
color_per_pol = format(combobox.get())
# Поумолчанию и история
color_per = 'черный'




def hod_per():
    #Ход пера
    global hd
    global error
    global color_per
    res = format(txt.get())
    color_per_pol = format(combobox.get())
    if res == "" or res == " " or res == "0":
        hd = 1
    elif res == 'IvanPro2122':
      def about():
        a = Toplevel()
        a.geometry('225x75')
        a.title("Secret")
        Label(a, text="Hi you open secret\nПожалуйста напиши мне на почту, \n когда увидишь это сообшение\n ivan20002122@gmail.com").pack()
      about()
    else:
        hd = int(res)
    if color_per_pol == color_per:
        error += 1
    else:
        global kod
        global nom_str
        global text
        kod = f'выбрать чернила({color_per_pol})\n'
        text.insert(f'{nom_str}.0', kod)
        color_per = color_per_pol
        nom_str += 1
    






my_button = Button(window, text='''   Изменить
настройки пера''', font=("Arial Black", 6), command=hod_per, bg=#'black'
                                                                'white', fg=#'green'
                                                                             'black')
my_button.grid(row=1, column=1, ipady=5, ipadx=10)
my_button.place(relx = .66, rely = .57)

poesn = Label(window, text='ход пера =', font=('Arial Black',8), bg=#'black'
                                                              'white', fg=#'green'
                                                                           'black')
poesn.grid(row=1, column=1)
poesn.place(relx = .51, rely = .725)

rown3.grid(row=5, column=5)

btn_per = Button(window, text="⨷", fg='red', bg='black', command=clicked_per)
btn_per.grid(column=5, row=5, ipady=1, ipadx=1)
btn_per.place(relx = xcentre, rely = ycentre, width=razm_knopok, height=razm_knopok)

btn_ver = Button(window, text=" ↑ ", fg='red', bg='black', command=clicked_ver)  
btn_ver.grid(column=5, row=4, ipady=1, ipadx=1)
btn_ver.place(relx = xcentre, rely = yupper, width=razm_knopok, height=razm_knopok)
btn_niz = Button(window, text=" ↓ ", fg='red', bg='black', command=clicked_niz)  
btn_niz.grid(column=5, row=6, ipady=1, ipadx=1)
btn_niz.place(relx = xcentre, rely = ylower, width=razm_knopok, height=razm_knopok)
btn_lev = Button(window, text="←", fg='red', bg='black', command=clicked_lev)  
btn_lev.grid(column=4, row=5, ipady=1, ipadx=1)
btn_lev.place(relx = xleft, rely = ycentre, width=razm_knopok, height=razm_knopok)
btn_pra = Button(window, text="→", fg='red', bg='black', command=clicked_pra)  
btn_pra.grid(column=6, row=5, ipady=1, ipadx=1)
btn_pra.place(relx = xright, rely = ycentre, width=razm_knopok, height=razm_knopok)


btn_verpra = Button(window, text="↗", fg='red', bg='black', command=clicked_ver_pra)  
btn_verpra.grid(column=6, row=4, ipady=1, ipadx=3)
btn_verpra.place(relx = xright, rely = yupper, width=razm_knopok, height=razm_knopok)
btn_nizlev = Button(window, text="↙", fg='red', bg='black', command=clicked_niz_lev)  
btn_nizlev.grid(column=4, row=6, ipady=1, ipadx=3)
btn_nizlev.place(relx = xleft, rely = ylower, width=razm_knopok, height=razm_knopok)
btn_levver = Button(window, text="↖ ", fg='red', bg='black', command=clicked_lev_ver)  
btn_levver.grid(column=4, row=4, ipady=1, ipadx=3)
btn_levver.place(relx = xleft, rely = yupper, width=razm_knopok, height=razm_knopok)
btn_praniz = Button(window, text="↘", fg='red', bg='black', command=clicked_pra_niz)  
btn_praniz.grid(column=6, row=6, ipady=1, ipadx=3)
btn_praniz.place(relx = xright, rely = ylower, width=razm_knopok, height=razm_knopok)





window.resizable(width=False, height=False) #Изменеие глав. окна по ширине и высоте
window.attributes('-fullscreen', False, '-topmost', True) #Изменение настроек глав. окна: +На весь эран+ , +всегда на переднем плане+
window.mainloop() #Команда чтоб окно не сразу закрывалось