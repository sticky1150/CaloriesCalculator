#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont


def ok():
    food_dic = {"ข้าวผัดหมู":350, "แกงเขียวหวาน":400}
    dessert_dic = {}
    bevarage_dic = {}
    food_name = food_var.get()
    dessert_name = dessert_var.get()
    beverage_name = beverage_var.get()
    print food_name , food_dic[food_name.encode('utf8')]#show values of dic by thai language
    rooto = Tk()
    Label(rooto, text= food_dic[food_name.encode('utf8')] ).grid(row=0, sticky=W)#show label in callories
    rooto.mainloop()

def food():#select food page
    global food_var, dessert_var, beverage_var
    root.destroy()
    rootf = Tk()
    rootf.geometry("400x350+200+200")
    rootf.title("Food Selecter")
    label = Label(rootf, text="Food Selecter",font=("Britannic Bold", 30),bg="white",fg="black")
    label.grid(row=0,column=1)
    Label(rootf, text=" ",font=("Britannic Bold", 20)).grid(row=1, sticky=W)
    Label(rootf, text="อาหารคาว",font=("Britannic Bold", 20)).grid(row=2, sticky=W)
    Label(rootf, text="ของหวาน",font=("Britannic Bold", 20)).grid(row=3, sticky=W)
    Label(rootf, text="เครื่องดื่ม",font=("Britannic Bold", 20)).grid(row=4, sticky=W)
    #------------Food Section------------------#
    food = ('ข้าวผัดหมู','แกงเขียวหวาน','กบทอด','ข้าวไข่ดาว','ข้าวขาหมู','ข้าวไกย่าง')
    food_var = StringVar(rootf)
    food_var.set(food[0])
    food_lis = OptionMenu(rootf, food_var, *food)
    food_lis.configure(font=("Britannic Bold", 20))
    food_lis.grid(row=2, column=1)
    food_var.get()
    
    #----------Dessert Section---------------#
    dessert = ('บัวลอย','ขนมโก๋','อิอิ','ครุคริ')
    dessert_var = StringVar(rootf)
    dessert_var.set(dessert[0])
    dessert_lis = OptionMenu(rootf, dessert_var, *dessert)
    dessert_lis.grid(row=3, column=1)
    dessert_var.get()

    #------Beverage Section---------#
    beverage = ('เป็บซี่','โคล่า','ชา','ครุคริ')
    beverage_var = StringVar(rootf)
    beverage_var.set(beverage[0])
    beverage_lis = OptionMenu(rootf, beverage_var, *beverage)
    beverage_lis.grid(row=4, column=1)
    beverage_var.get()
    
    button = Button(rootf, text="OK", command=ok)
    button.grid(row=5, column=1)
    rootf.mainloop()



root = Tk()
root.geometry("400x350+200+200")
font = tkFont.Font(size="25")
root.title("Calories Calculator")
label = Label(root, text="Calories Calculator",font=("Britannic Bold", 30),bg="white",fg="black")
label.pack(fill=X)
frame1 = Frame(root).pack(side = "top")
button2 = Button(frame1, padx=30, pady=35, bd=15, 
                     text="คำนวณเฉพาะพลังงานของอาหาร",font=("AngsanaNew", 20), fg="black", bg="yellow", command=food)
button2.pack()
root.mainloop()

 
