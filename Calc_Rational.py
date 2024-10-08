import tkinter
from functools import partial
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from Rational import Rational

root = Tk()
root.title('Rational Calculator')
root.geometry('600x450')
root['bg'] = 'PaleVioletRed'
root.resizable(False, False)


#   функции для кнопок
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def add_1(event):
    if is_number(entry_numer_1.get()) and is_number(entry_denomin_1.get()) and is_number(entry_numer_2.get()) and is_number(entry_denomin_2.get()):
        numer_1 = int(entry_numer_1.get())
        denomin_1 = int(entry_denomin_1.get())
        numer_2 = int(entry_numer_2.get())
        denomin_2 = int(entry_denomin_2.get())
        showinfo('Result:', str(Rational(numer_1, denomin_1) + Rational(numer_2, denomin_2)))


def add_2(event):
    if is_number(entry_numer_1_2.get()) and is_number(entry_denomin_1_2.get()) and is_number(entry_num_1.get()):
        numer = int(entry_numer_1_2.get())
        denomin = int(entry_denomin_1_2.get())
        showinfo('Result', str(Rational(numer, denomin) + int(entry_num_1.get())))


def sub_1(event):
    if is_number(entry_numer_1.get()) and is_number(entry_denomin_1.get()) and is_number(entry_numer_2.get()) and is_number(entry_denomin_2.get()):
        numer_1 = int(entry_numer_1.get())
        denomin_1 = int(entry_denomin_1.get())
        numer_2 = int(entry_numer_2.get())
        denomin_2 = int(entry_denomin_2.get())
        showinfo('Result:', str(Rational(numer_1, denomin_1) - Rational(numer_2, denomin_2)))


def sub_2(event):
    if is_number(entry_numer_1_2.get()) and is_number(entry_denomin_1_2.get()) and is_number(entry_num_1.get()):
        numer = int(entry_numer_1_2.get())
        denomin = int(entry_denomin_1_2.get())
        showinfo('Result', str(Rational(numer, denomin) - int(entry_num_1.get())))


def mul_1(event):
    if is_number(entry_numer_1.get()) and is_number(entry_denomin_1.get()) and is_number(entry_numer_2.get()) and is_number(entry_denomin_2.get()):
        numer_1 = int(entry_numer_1.get())
        denomin_1 = int(entry_denomin_1.get())
        numer_2 = int(entry_numer_2.get())
        denomin_2 = int(entry_denomin_2.get())
        showinfo('Result:', str(Rational(numer_1, denomin_1) * Rational(numer_2, denomin_2)))


def mul_2(event):
    if is_number(entry_numer_1_2.get()) and is_number(entry_denomin_1_2.get()) and is_number(entry_num_1.get()):
        numer = int(entry_numer_1_2.get())
        denomin = int(entry_denomin_1_2.get())
        showinfo('Result', str(Rational(numer, denomin) * int(entry_num_1.get())))


def div_1(event):
    if is_number(entry_numer_1.get()) and is_number(entry_denomin_1.get()) and is_number(entry_numer_2.get()) and is_number(entry_denomin_2.get()):
        numer_1 = int(entry_numer_1.get())
        denomin_1 = int(entry_denomin_1.get())
        numer_2 = int(entry_numer_2.get())
        denomin_2 = int(entry_denomin_2.get())
        showinfo('Result:', str(Rational(numer_1, denomin_1) / Rational(numer_2, denomin_2)))


def div_2(event):
    if is_number(entry_numer_1_2.get()) and is_number(entry_denomin_1_2.get()) and is_number(entry_num_1.get()):
        numer = int(entry_numer_1_2.get())
        denomin = int(entry_denomin_1_2.get())
        showinfo('Result', str(Rational(numer, denomin) / int(entry_num_1.get())))


def pow(event):
    if is_number(entry_numer_1_2.get()) and is_number(entry_denomin_1_2.get()) and is_number(entry_num_1.get()):
        numer = int(entry_numer_1_2.get())
        denomin = int(entry_denomin_1_2.get())
        showinfo('Result', str(Rational(numer, denomin) ** int(entry_num_1.get())))


#   разделяем окно пополам
separator = Frame(root, bg="black", width=2)
separator.place(relx=0.5, rely=0, relheight=1)

#   лейблы для первой половины экрана
Label(text='Дробь на дробь', background='PaleVioletRed', font=('Arial', 11)).place(height=20, width=290, x=0, y=0)
Label(text='Введите числитель и знаменатель \n первой дроби:', background='PaleVioletRed', font=('Arial', 11)).place(height=40, width=290, x=0, y=20)
Label(text='Введите числитель и знаменатель \n второй дроби:', background='PaleVioletRed', font=('Arial', 11)).place(height=40, width=290, x=0, y=125)

#   разделители для дробей
Label(text='/', background='PaleVioletRed', font=('Arial', 40)).place(height=50, width=15, x=140, y=70)
Label(text='/', background='PaleVioletRed', font=('Arial', 40)).place(height=50, width=15, x=140, y=175)

#   окна ввода для дробей
entry_numer_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_1.place(height=40, width=100, x=35, y=65)
entry_denomin_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_1.place(height=40, width=100, x=160, y=85)

entry_numer_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_2.place(height=40, width=100, x=35, y=170)
entry_denomin_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_2.place(height=40, width=100, x=160, y=190)

#   лейблы для второй половины экрана
Label(text='Дробь на число', background='PaleVioletRed', font=('Arial', 11)).place(height=20, width=290, x=310, y=0)
Label(text='Введите числитель и знаменатель \n дроби:', background='PaleVioletRed', font=('Arial', 11)).place(height=40, width=290, x=310, y=20)
Label(text='Введите число:', background='PaleVioletRed', font=('Arial', 11)).place(height=40, width=290, x=310, y=120)

#   разделитель для дроби
Label(text='/', background='PaleVioletRed', font=('Arial', 40)).place(height=50, width=15, x=440, y=70)

#    окна ввода для дроби и числа
entry_numer_1_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_1_2.place(height=40, width=100, x=335, y=65)
entry_denomin_1_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_1_2.place(height=40, width=100, x=460, y=85)
entry_num_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_num_1.place(height=40, width=100, x=400, y=170)

#   кнопки действий для 1 части окна
btn_add_1 = Button(text='+', font=('Arial', 13), background='#f5b1c3', command=partial(add_1, '<Button-1>'))
btn_add_1.place(width=100, height=40, x=30, y=260)
btn_sub_1 = Button(text='-', font=('Arial', 13), background='#f5b1c3', command=partial(sub_1, '<Button-1>'))
btn_sub_1.place(width=100, height=40, x=160, y=260)
btn_mul_1 = Button(text='x', font=('Arial', 10), background='#f5b1c3', command=partial(mul_1, '<Button-1>'))
btn_mul_1.place(width=100, height=40, x=30, y=330)
btn_div_1 = Button(text='/', font=('Arial', 13), background='#f5b1c3', command=partial(div_1, '<Button-1>'))
btn_div_1.place(width=100, height=40, x=160, y=330)

#   кнопки действий для 2 части окна
btn_add_2 = Button(text='+', font=('Arial', 13), background='#f5b1c3', command=partial(add_2, '<Button-1>'))
btn_add_2.place(width=100, height=40, x=340, y=260)
btn_sub_2 = Button(text='-', font=('Arial', 13), background='#f5b1c3', command=partial(sub_2, '<Button-1>'))
btn_sub_2.place(width=100, height=40, x=470, y=260)
btn_mul_2 = Button(text='x', font=('Arial', 10), background='#f5b1c3', command=partial(mul_2, '<Button-1>'))
btn_mul_2.place(width=100, height=40, x=340, y=330)
btn_div_2 = Button(text='/', font=('Arial', 13), background='#f5b1c3', command=partial(div_2, '<Button-1>'))
btn_div_2.place(width=100, height=40, x=470, y=330)
btn_pow = Button(text='x^y', font=('Arial', 13), background='#f5b1c3', command=partial(pow, '<Button-1>'))
btn_pow.place(width=100, height=40, x=405, y=390)


root.mainloop()