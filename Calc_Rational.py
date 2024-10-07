import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Rational Calculator')
root.geometry('600x450')
root['bg'] = 'PaleVioletRed'
root.resizable(False, False)

separator = Frame(root, bg="black", width=2)
separator.place(relx=0.5, rely=0, relheight=1)

lable_1 = Label(text='Дробь на дробь', background='PaleVioletRed', font=('Arial', 11))
lable_1.place(height=20, width=290, x=0, y=0)
label_message = Label(text='Введите числитель и знаменатель \n первой дроби:', background='PaleVioletRed', font=('Arial', 11))
label_message.place(height=40, width=290, x=0, y=20)
label_message_2 = Label(text='Введите числитель и знаменатель \n второй дроби:', background='PaleVioletRed', font=('Arial', 11))
label_message_2.place(height=40, width=290, x=0, y=125)

label_1 = Label(text='/', background='PaleVioletRed', font=('Arial', 40))
label_1.place(height=50, width=15, x=140, y=70)
label_2 = Label(text='/', background='PaleVioletRed', font=('Arial', 40))
label_2.place(height=50, width=15, x=140, y=175)

entry_numer_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_1.place(height=40, width=100, x=35, y=65)
entry_denomin_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_1.place(height=40, width=100, x=160, y=85)

entry_numer_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_2.place(height=40, width=100, x=35, y=170)
entry_denomin_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_2.place(height=40, width=100, x=160, y=190)


lable_2 = Label(text='Дробь на число', background='PaleVioletRed', font=('Arial', 11))
lable_2.place(height=20, width=290, x=310, y=0)
label_message = Label(text='Введите числитель и знаменатель \n дроби:', background='PaleVioletRed', font=('Arial', 11))
label_message.place(height=40, width=290, x=310, y=20)
label_message_2 = Label(text='Введите число:', background='PaleVioletRed', font=('Arial', 11))
label_message_2.place(height=40, width=290, x=310, y=120)
label_1_2 = Label(text='/', background='PaleVioletRed', font=('Arial', 40))
label_1_2.place(height=50, width=15, x=440, y=70)

entry_numer_1_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_numer_1_2.place(height=40, width=100, x=335, y=65)
entry_denomin_1_2 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=LEFT)
entry_denomin_1_2.place(height=40, width=100, x=460, y=85)
entry_num_1 = Entry(background='PaleVioletRed', font=('Arial', 20), justify=RIGHT)
entry_num_1.place(height=40, width=100, x=400, y=170)


root.mainloop()