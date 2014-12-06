#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont


#-------calculate calories page------#
def calculate():
    rooto = Tk()
    rooto.geometry("450x400+200+200")
    rooto.title("Calculator")
    food_dic = {'ไม่เลือก':0, 'ข้าวผัดหมู':350, 'แกงเขียวหวาน':400}
    dessert_dic = {'ไม่เลือก':0, 'กล้วยบวชชี':230, 'ขนมปลากริมไข่เต่า':250,
                   'ข้าวเหนียวกะทิทุเรียน':225, 'ข้าวเหนียวดำเปียก 1 ถ้วย':205, 'ข้าวโพดคั่ว (เคลือบน้ำตาล)':60,
                   'ครองแครงกะทิ':250, 'ครีมโรล 1 ชิ้น':360, 'ชิฟฟอนกาแฟ':275, 'ชิฟฟอนคัสตาร์ดเค้ก':340,
                   'ช็อคโกแลตำ':170, 'ซ่าหริ่ม 1 ถ้วย':275,'ถั่วเขียวต้มน้ำตาล':160, 'ทับทิมกรอบ':250,
                   'บราวนี่':340, 'บะจ่าง':300, 'บัวลอย':223, 'บัวลอยน้ำขิง':160, 'บัวลอยเผือก':300,
                   'บูลเบอร์รี่ชีสเค้ก':285, 'พายกรอบ (โรยน้ำตาล)':235, 'พายชีสบูลเบอร์รี่':350, 'ฟรุตสลัด':180,
                   'ฟรุตเค้ก':400, 'ฟรุ้ตบาร์':305, 'มันเทศเชื่อม':230, 'มันแกงบวด':184,'รวมมิตร':230,
                   'ลอดช่องน้ำกะทิ':210, 'ลอดช่องสิงคโปร์':215, 'ลำใยในน้ำเชื่อม':180, 'ลิ้นจี่ในน้ำเชื่อม':110,
                   'ลูกตาลลอยแก้ว':180, 'ลูกเดือยต้มน้ำตาล':140, 'วุ้นกะทิ':215, 'สังขยา':204, 'สังขยาฟักทอง':288,
                   'สังขยาเผือก':222, 'สาลี่':116, 'สาเกเชื่อมราดกะทิ':235, 'อาลัว':145, 'เค้กกล้วยหอม':370,
                   'เค้กช็อคโกแลต':275, 'เค้กเนย':255, 'เค้กเนยแต่งหน้า':405, 'เค้กใบเตย':250, 'เฉาก๊วย':90,
                   'เดนิสแฮม':385, 'เต้าหู้นมสด':150, 'เต้าฮวยน้ำขิง':130, 'เต้าฮวยฟรุตสลัด':150, 'เผือกน้ำกะทิ':250,
                   'เผือกเชื่อม':220, 'แบล็กฟลอเรสต์เค้ก':470, 'แมงลักน้ำกะทิ':112, 'แยมโรล':310, 'โรตี (ใส่นมข้น+น้ำตาล+ใส่ไข่)':590,
                   'ไอศกรีมกะทิ':215, 'ไอศกรีมกาแฟ':142, 'ไอศกรีมชอกโกแล็ต':110, 'ไอศกรีมวนิลลา':140, 'ไอศกรีมสตรอเบอรี่':110,
                   'ไอศกรีมเรซิน':264}
    beverage_dic = {'ไม่เลือก':0, 'กาแฟร้อน':55, 'กาแฟเย็น':115, 'ชาดำเย็น':110, 'ชามะนาว':100, 'ชาร้อน':55, 'ชาเขียว (รสหวาน)':120,
                    'ชาเย็น':100, 'ช็อคโกแลตร้อน':120, 'ช็อคโกแลตเย็น':120, 'นมจืด (ไขมันต่ำ)':125, 'นมจืด (ไม่มีไขมัน)':80,
                    'นมถั่วเหลือง (หวานน้อย)':140, 'นมปรุงแต่ง (รสหวาน)':200, 'นมเย็น':150, 'น้ำกระเจี๊ยบ':120, 'น้ำนมข้าวโพด':80,
                    'น้ำผลไม้รวม':100, 'น้ำผักรวม':90, 'น้ำมะนาว':100, 'น้ำมะพร้าว':120, 'น้ำมะพร้าวผสมเนื้อ':150, 'น้ำมะเขือเทศ':48,
                    'น้ำลำใย':100, 'น้ำส้มคั้น':90, 'น้ำองุ่น':112, 'น้ำอัดลม (หวาน)':75, 'น้ำอัดลมประเภทโคล่า(325 cc)':130,
                    'น้ำเต้าหู้(จืด)':75, 'น้ำใบบัวบก':120, 'น้ำใบเตย':120, 'มิลค์เชค':150,'โกโก้':210, 'โยเกิร์ต (รสธรรมชาติ)':95,
                    'โยเกิร์ต (รสผลไม้)':175, 'โยเกิร์ต (ไขมันต่ำรสผลไม้)':160, 'โอวัลติน':210, 'โอเลี้ยง':165}
    food_name = food_var.get()
    dessert_name = dessert_var.get()
    beverage_name = beverage_var.get()
    #find sum calories
    calories = food_dic[food_name.encode('utf8')]+dessert_dic[dessert_name.encode('utf8')]+beverage_dic[beverage_name.encode('utf8')]
    Label(rooto, text="จำนวนแคลอรี่ทั้งหมด", font=("Britannic Bold", 25)).grid(row=0, column=3)
    Label(rooto, text=calories, font=("Britannic Bold", 25)).grid(row=1, column=3)#show callories in label
    Label(rooto, text="การออกกำลังกายที่แนะนำ", font=("Britannic Bold", 18)).grid(row=3, column=3)
    Label(rooto, text="วิ่งเร็ว", font=("Britannic Bold", 15)).grid(row=4, column=2)
    Label(rooto, text=str((calories/15)/60)+" ชั่วโมง "+str((calories/15)%60)+" นาที").grid(row=4, column=3)
    Label(rooto, text="ว่ายน้ำ", font=("Britannic Bold", 15)).grid(row=5, column=2)
    Label(rooto, text=str((calories/8)/60)+" ชั่วโมง "+str((calories/8)%60)+" นาที").grid(row=5, column=3)
    Label(rooto, text="ปั่นจักรยาน", font=("Britannic Bold", 15)).grid(row=6, column=2)
    Label(rooto, text=str((calories/7)/60)+" ชั่วโมง "+str((calories/7)%60)+" นาที").grid(row=6, column=3)
    Label(rooto, text="กรุณาปิดหน้านี้เพื่อคำนวณอีกใหม่").grid(row=7, column=3)
    rooto.mainloop()

#------choose food page---------#
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
    food = ('ไม่เลือก','ข้าวผัดหมู','แกงเขียวหวาน','กบทอด','ข้าวไข่ดาว','ข้าวขาหมู','ข้าวไกย่าง')
    food_var = StringVar(rootf)
    food_var.set(food[0])
    food_lis = OptionMenu(rootf, food_var, *food)
    food_lis.configure(font=("Britannic Bold", 20))
    food_lis.grid(row=2, column=1)
    food_var.get()
    
    #----------Dessert Section---------------#
    dessert = ('ไม่เลือก', 'กล้วยบวชชี', 'ขนมปลากริมไข่เต่า', 'ข้าวเหนียวกะทิทุเรียน', 'ข้าวเหนียวดำเปียก', 'ข้าวโพดคั่ว (เคลือบน้ำตาล)',
               'ครองแครงกะทิ', 'ครีมโรล', 'ชิฟฟอนกาแฟ', 'ชิฟฟอนคัสตาร์ดเค้ก'
               'ช็อคโกแลตำ', 'ซ่าหริ่ม', 'ถั่วเขียวต้มน้ำตาล', 'ทับทิมกรอบ', 'บราวนี่', 'บะจ่าง',
               'บัวลอย', 'บัวลอยน้ำขิง', 'บัวลอยเผือก', 'บูลเบอร์รี่ชีสเค้ก', 'พายกรอบ (โรยน้ำตาล)',
               'พายชีสบูลเบอร์รี่', 'ฟรุตสลัด', 'ฟรุตเค้ก', 'ฟรุ้ตบาร์', 'มันเทศเชื่อม',
               'มันแกงบวด', 'รวมมิตร', 'ลอดช่องน้ำกะทิ', 'ลอดช่องสิงคโปร์', 'ลำใยในน้ำเชื่อม', 'ลิ้นจี่ในน้ำเชื่อม',
               'ลูกตาลลอยแก้ว', 'ลูกเดือยต้มน้ำตาล', 'วุ้นกะทิ', 'สังขยา', 'สังขยาฟักทอง', 'สังขยาเผือก',
               'สาลี่', 'สาเกเชื่อมราดกะทิ', 'อาลัว', 'เค้กกล้วยหอม', 'เค้กช็อคโกแลต', 'เค้กเนย',
               'เค้กเนยแต่งหน้า', 'เค้กใบเตย', 'เฉาก๊วย', 'เดนิสแฮม', 'เต้าหู้นมสด', 'เต้าฮวยน้ำขิง',
               'เต้าฮวยฟรุตสลัด', 'เผือกน้ำกะทิ', 'เผือกเชื่อม', 'แบล็กฟลอเรสต์เค้ก', 'แมงลักน้ำกะทิ',
               'แยมโรล', 'โรตี (ใส่นมข้น+น้ำตาล+ใส่ไข่)', 'ไอศกรีมกะทิ', 'ไอศกรีมกาแฟ', 'ไอศกรีมชอกโกแล็ต',
               'ไอศกรีมวนิลลา', 'ไอศกรีมสตรอเบอรี่', 'ไอศกรีมเรซิน')
    dessert_var = StringVar(rootf)
    dessert_var.set(dessert[0])
    dessert_lis = OptionMenu(rootf, dessert_var, *dessert)
    dessert_lis.configure(font=("Britannic Bold", 20))
    dessert_lis.grid(row=3, column=1)
    dessert_var.get()

    #------Beverage Section---------#

    beverage = ('ไม่เลือก', 'กาแฟร้อน', 'กาแฟเย็น', 'ชาดำเย็น', 'ชามะนาว', 'ชาร้อน', 'ชาเขียว (รสหวาน)', 'ชาเย็น',
                'ช็อคโกแลตร้อน', 'ช็อคโกแลตเย็น', 'นมจืด (ไขมันต่ำ)', 'นมจืด (ไม่มีไขมัน)', 'นมถั่วเหลือง (หวานน้อย)',
                'นมปรุงแต่ง (รสหวาน)', 'นมเย็น', 'น้ำกระเจี๊ยบ', 'น้ำนมข้าวโพด', 'น้ำผลไม้รวม', 'น้ำผักรวม', 'น้ำมะนาว',
                'น้ำมะพร้าว', 'น้ำมะพร้าวผสมเนื้อ', 'น้ำมะเขือเทศ', 'น้ำลำใย', 'น้ำส้มคั้น', 'น้ำองุ่น', 'น้ำอัดลม (หวาน)', 
                'น้ำอัดลมประเภทโคล่า(325 cc)', 'น้ำเต้าหู้(จืด)', 'น้ำใบบัวบก', 'น้ำใบเตย', 'มิลค์เชค', 'โกโก้',
                'โยเกิร์ต (รสธรรมชาติ)', 'โยเกิร์ต (รสผลไม้)', 'โยเกิร์ต (ไขมันต่ำรสผลไม้)', 'โอวัลติน', 'โอเลี้ยง')
    beverage_var = StringVar(rootf)
    beverage_var.set(beverage[0])
    beverage_lis = OptionMenu(rootf, beverage_var, *beverage)
    beverage_lis.grid(row=4, column=1)
    beverage_lis.configure(font=("Britannic Bold", 20))
    beverage_var.get()
    
    button = Button(rootf, text="OK", command=calculate)
    button.grid(row=5, column=1)
    rootf.mainloop()


#-------First Page------#
root = Tk()
root.geometry("400x350+200+200")
font = tkFont.Font(size="25")
root.title("Calories Calculator")
label = Label(root, text="Calories Calculator",font=("Britannic Bold", 30),bg="white",fg="black")
label.pack(fill=X)
label1 = Label(root, text="",font=("Britannic Bold", 30))
label1.pack(fill=X)
frame1 = Frame(root).pack(side = "top")
button2 = Button(frame1, padx=30, pady=35, bd=15, 
                     text="คำนวณเฉพาะพลังงานของอาหาร",font=("AngsanaNew", 20), fg="black", bg="yellow", command=food)
button2.pack()
root.mainloop()

 
