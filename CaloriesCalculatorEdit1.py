#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont
import Tkinter as tk

#-------calculate calories page------#
def calculate():
    rooto = Tk()
    rooto.geometry("480x480+350+100")
    rooto.title("Calculator")
    food_dic = {'ไม่เลือก':0, 'กระเพาะปลา':150, 'กระเพาะปลาตุ๋นน้ำแดง':225, 'กุ้งผัดพริกอ่อน':235, 'ก๋วยจั๊บ':240, 'ก๋วยจั๊บญวณ':235,
                'ก๋วยเตี๋ยวคั่วไก่':435, 'ก๋วยเตี๋ยวต้มยำกุ้ง':320, 'ก๋วยเตี๋ยวผัดกระเพราไก่':440, 'ก๋วยเตี๋ยวผัดไทยกุ้งสดใส่ไข่':545, 'ก๋วยเตี๋ยวราดหน้าปลากระพง':435,
                'ก๋วยเตี๋ยวหลอด':225, 'ก๋วยเตี๋ยวเนื้อเรียง':370, 'ก๋วยเตี๋ยวเรือน้ำตกน้ำ':180, 'ก๋วยเตี๋ยวเรือน้ำตกแห้ง':225, 'ก๋วยเตี๋ยวเส้นปลา น้ำ':375,
                'ก๋วยเตี๋ยวเส้นปลา แห้ง':420, 'ก๋วยเตี๋ยวเส้นเล็กต้มยำหมู':335, 'ก๋วยเตี๋ยวเส้นเล็กหมูแห้ง':330, 'ก๋วยเตี๋ยวเส้นใหญ่ผัดซีอิ๊วใส่ไข่':520, 'ก๋วยเตี๋ยวเส้นใหญ่ราดหน้าหมู':405,
                'ก๋วยเตี๋ยวแขก':380, 'ขนมจีนน้ำยา':375, 'ขนมจีนน้ำเงี้ยว':305, 'ข้าว สตูว์ไก่':465, 'ข้าวกุ้งทอดกระเทียมพริกไทย':495,
                'ข้าวขาหมู':690, 'ข้าวคลุกกะปิ':410, 'ข้าวซอยไก่ / หมู':395, 'ข้าวต้ม(ข้าวกล้อง)':120, 'ข้าวต้ม(ข้าวขาว)':120,
                'ข้าวผัดกระเพรากุ้ง':540, 'ข้าวผัดกระเพราหมู':580, 'ข้าวผัดกระเพราไก่ไข่ดาว':630, 'ข้าวผัดกุนเชียง':590, 'ข้าวผัดกุ้งใส่ไข่':595,
                'ข้าวผัดคะน้าหมูกรอบ':670, 'ข้าวผัดต้มยำทะเลแห้ง':400, 'ข้าวผัดน้ำพริกกุ้งสด':460, 'ข้าวผัดน้ำพริกลงเรือ':605, 'ข้าวผัดปลาหมึกน้ำพริกเผา':535,
                'ข้าวผัดปลาเค็ม':405, 'ข้าวผัดปูใส่ไข่':610, 'ข้าวผัดมันกุ้งใส่ไข่':575, 'ข้าวผัดหนำเลียบ-หมู-ไข่':370, 'ข้าวผัดหมูน้ำพริกเผา':665,
                'ข้าวผัดหมูใส่ไข่':660, 'ข้าวผัดอเมริกัน':790, 'ข้าวผัดแกงเขียวหวานไก่':630, 'ข้าวผัดแหนม':610, 'ข้าวผัดไส้กรอก':520,
                'ข้าวมันส้มตำ เนื้อผัดหวาน':590, 'ข้าวมันไก่':585, 'ข้าวมันไก่ทอด':695, 'ข้าวราดหน้าไก่':400,
                'ข้าวหน้ากุ้งผัดพริกสด':540, 'ข้าวหน้าเป็ด':495, 'ข้าวหมกไก่':540, 'ข้าวหมูกระเทียม':525, 'ข้าวหมูแดง':560,
                'ข้าวเหนียวหมูทอด':440, 'ข้าวเหนียวหมูสวรรค์':480, 'ข้าวไก่อบ':490, 'ข้าวไข่เจียว':445, 'บะหมี่กรอบราดหน้า':515,
                'บะหมี่กรอบราดหน้า รวมมิตร':690, 'บะหมี่กรอบราดหน้า ไก่ หน่อไม้':660, 'บะหมี่กึ่งสำเร็จรูปผัดกระเพราหมู':540, 'บะหมี่กึ่งสำเร็จรูปผัดขี้เมา':530,
                'บะหมี่น่องไก่-น้ำ':375, 'บะหมี่น้ำต้มยำ หมู':300, 'บะหมี่เกี๊ยวหมูแดง-น้ำ':305, 'บะหมี่เกี๊ยวเป็ดย่าง':415, 'บะหมี่เป็ดน้ำ':370,
                'บะหมี่แห้ง หมูแดง':345, 'บาร์บีคิวซี่โครงหมู ข้าวคลุกเนย':340, 'ผัดวุ้นเส้นใส่ไข่':265, 'ผัดไชโป๊วใส่ไข่':125,
                'ผัดไทยไข่ห่อ':565, 'ผัดไทยไร้เส้น':350, 'พอร์คชอปทอด ผักผัดเนย':545, 'มักกะโรนีขี้เมาไก่':520, 'มักกะโรนีผัดกุ้ง':420, 'ยากิโซบะ':400,
                'วุ้นเส้นผัดไทย กุ้งสด':520, 'สปาเกตตี้กระเพรากุ้ง':485, 'สปาเก็ตตี้ไก่อบ':430, 'สลัดผัก':240, 'สลัดเนื้อสันในทอด':490,
                'สุกียากี้แห้งทะเล':280, 'สุกี้ยากี้ไก่-น้ำ':345, 'สเต็กปลาย่าง':260, 'สเต็กหมู ผักสดคลุก':505, 'สเต็กหมู สลัดผักสด':375,
                'สเต็กไก่ทอด มันบด':615, 'ส้มตำปู':35, 'ส้มตำไทย':55, 'หมี่กรอบราดหน้าหมู':690, 'หมี่ซั่วผัด':395, 'เกี๊ยวกรอบราดหน้ากุ้ง':635,
                'เกี๊ยวน้ำกุ้ง':275, 'เกี๊ยวปลาน้ำ':165, 'เฝอ':240, 'เย็นตาโฟน้ำ':290, 'เส้นจันท์ผัดปู':575, 'เส้นหมี่ลูกชิ้นน้ำใส':225,
                'เส้นหมี่ลูกชิ้นหมูแห้ง':430, 'เส้นใหญ่ผัดขี้เมา':550, 'โกยซีหมี่':550, 'โจ๊กหมู':160, 'โจ๊กหมู ตับ ไข่ลวก':230}
    dessert_dic = {'ไม่เลือก':0, 'กล้วยบวชชี':230, 'ขนมปลากริมไข่เต่า':250,
                   'ข้าวเหนียวกะทิทุเรียน':225, 'ข้าวเหนียวดำเปียก':205, 'ข้าวโพดคั่ว (เคลือบน้ำตาล)':60,
                   'ครองแครงกะทิ':250, 'ครีมโรล':360, 'ชิฟฟอนกาแฟ':275, 'ชิฟฟอนคัสตาร์ดเค้ก':340,
                   'ช็อคโกแลตำ':170, 'ซ่าหริ่ม':275,'ถั่วเขียวต้มน้ำตาล':160, 'ทับทิมกรอบ':250,
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
    rootf = tk.Tk()
    rootf.geometry("480x480+350+100")

    
    rootf.title("Food Selecter")
    image2 = tk.PhotoImage(file="Green_Lime_Blur.gif")
    w = image2.width()
    h = image2.height()

    panel1 = tk.Label(rootf, image=image2)
    panel1.pack(side='top', fill='both', expand='yes')

    
    

    
    label = tk.Label(panel1, text="Food Selecter",font=("Chelsea", 30),bg="chartreuse4",fg="snow")
    label.pack(fill=X)
    label2 = Frame(panel1, bg="chartreuse4")
    Label(label2, text="อาหารคาว",font=("Chelsea", 20),fg="snow",bg="chartreuse4").pack(side=TOP, anchor=W, fill=X, expand=YES)
    Label(label2, text="ของหวาน",font=("Chelsea", 20),fg="snow",bg="chartreuse4").pack(side=TOP, anchor=W, fill=X, expand=YES)
    Label(label2, text="เครื่องดื่ม",font=("Chelsea", 20),fg="snow",bg="chartreuse4").pack(side=TOP, anchor=W, fill=X, expand=YES)
    label2.pack(side=LEFT, fill=BOTH, pady=145)
    label3 = Frame(panel1, bg="chartreuse4")
    
    #------------Food Section------------------#
    food = ('ไม่เลือก', 'กระเพาะปลา', 'กระเพาะปลาตุ๋นน้ำแดง', 'กุ้งผัดพริกอ่อน', 'ก๋วยจั๊บ', 'ก๋วยจั๊บญวณ', 'ก๋วยเตี๋ยวคั่วไก่',
            'ก๋วยเตี๋ยวต้มยำกุ้ง', 'ก๋วยเตี๋ยวผัดกระเพราไก่', 'ก๋วยเตี๋ยวผัดไทยกุ้งสดใส่ไข่', 'ก๋วยเตี๋ยวราดหน้าปลากระพง', 'ก๋วยเตี๋ยวหลอด',
            'ก๋วยเตี๋ยวเนื้อเรียง', 'ก๋วยเตี๋ยวเรือน้ำตกน้ำ', 'ก๋วยเตี๋ยวเรือน้ำตกแห้ง', 'ก๋วยเตี๋ยวเส้นปลา น้ำ', 'ก๋วยเตี๋ยวเส้นปลา แห้ง',
            'ก๋วยเตี๋ยวเส้นเล็กต้มยำหมู', 'ก๋วยเตี๋ยวเส้นเล็กหมูแห้ง', 'ก๋วยเตี๋ยวเส้นใหญ่ผัดซีอิ๊วใส่ไข่', 'ก๋วยเตี๋ยวเส้นใหญ่ราดหน้าหมู', 'ก๋วยเตี๋ยวแขก',
            'ขนมจีนน้ำยา', 'ขนมจีนน้ำเงี้ยว', 'ข้าว สตูว์ไก่', 'ข้าวกุ้งทอดกระเทียมพริกไทย', 'ข้าวขาหมู', 'ข้าวคลุกกะปิ', 'ข้าวซอยไก่ / หมู',
            'ข้าวต้ม(ข้าวกล้อง)', 'ข้าวต้ม(ข้าวขาว)', 'ข้าวผัดกระเพรากุ้ง', 'ข้าวผัดกระเพราหมู', 'ข้าวผัดกระเพราไก่ไข่ดาว', 'ข้าวผัดกุนเชียง',
            'ข้าวผัดกุ้งใส่ไข่', 'ข้าวผัดคะน้าหมูกรอบ', 'ข้าวผัดต้มยำทะเลแห้ง', 'ข้าวผัดน้ำพริกกุ้งสด', 'ข้าวผัดน้ำพริกลงเรือ', 'ข้าวผัดปลาหมึกน้ำพริกเผา',
            'ข้าวผัดปลาเค็ม', 'ข้าวผัดปูใส่ไข่', 'ข้าวผัดมันกุ้งใส่ไข่', 'ข้าวผัดหนำเลียบ-หมู-ไข่', 'ข้าวผัดหมูน้ำพริกเผา', 'ข้าวผัดหมูใส่ไข่',
            'ข้าวผัดอเมริกัน', 'ข้าวผัดแกงเขียวหวานไก่', 'ข้าวผัดแหนม', 'ข้าวผัดไส้กรอก', 'ข้าวมันส้มตำ เนื้อผัดหวาน', 'ข้าวมันไก่',
            'ข้าวมันไก่ทอด', 'ข้าวราดหน้าไก่', 'ข้าวหน้ากุ้งผัดพริกสด', 'ข้าวหน้าเป็ด', 'ข้าวหมกไก่', 'ข้าวหมูกระเทียม',
            'ข้าวหมูแดง', 'ข้าวเหนียวหมูทอด', 'ข้าวเหนียวหมูสวรรค์', 'ข้าวไก่อบ', 'ข้าวไข่เจียว', 'บะหมี่กรอบราดหน้า',
            'บะหมี่กรอบราดหน้า รวมมิตร', 'บะหมี่กรอบราดหน้า ไก่ หน่อไม้', 'บะหมี่กึ่งสำเร็จรูปผัดกระเพราหมู', 'บะหมี่กึ่งสำเร็จรูปผัดขี้เมา',
            'บะหมี่น่องไก่-น้ำ', 'บะหมี่น้ำต้มยำ หมู', 'บะหมี่เกี๊ยวหมูแดง-น้ำ', 'บะหมี่เกี๊ยวเป็ดย่าง', 'บะหมี่เป็ดน้ำ', 'บะหมี่แห้ง หมูแดง',
            'บาร์บีคิวซี่โครงหมู ข้าวคลุกเนย', 'ผัดวุ้นเส้นใส่ไข่', 'ผัดไชโป๊วใส่ไข่','ผัดไทยไข่ห่อ', 'ผัดไทยไร้เส้น', 'พอร์คชอปทอด ผักผัดเนย',
            'มักกะโรนีขี้เมาไก่', 'มักกะโรนีผัดกุ้ง', 'ยากิโซบะ', 'วุ้นเส้นผัดไทย กุ้งสด', 'สปาเกตตี้กระเพรากุ้ง', 'สปาเก็ตตี้ไก่อบ', 'สลัดผัก',
            'สลัดเนื้อสันในทอด', 'สุกียากี้แห้งทะเล', 'สุกี้ยากี้ไก่-น้ำ', 'สเต็กปลาย่าง', 'สเต็กหมู ผักสดคลุก', 'สเต็กหมู สลัดผักสด',
            'สเต็กไก่ทอด มันบด', 'ส้มตำปู', 'ส้มตำไทย', 'หมี่กรอบราดหน้าหมู', 'หมี่ซั่วผัด', 'เกี๊ยวกรอบราดหน้ากุ้ง', 'เกี๊ยวน้ำกุ้ง',
            'เกี๊ยวปลาน้ำ', 'เฝอ', 'เย็นตาโฟน้ำ', 'เส้นจันท์ผัดปู', 'เส้นหมี่ลูกชิ้นน้ำใส', 'เส้นหมี่ลูกชิ้นหมูแห้ง', 'เส้นใหญ่ผัดขี้เมา',
            'โกยซีหมี่', 'โจ๊กหมู', 'โจ๊กหมู ตับ ไข่ลวก')
    food_var = StringVar(rootf)
    food_var.set(food[0])
    food_lis = tk.OptionMenu(label3, food_var, *food)
    food_lis.config(width = 13)
    food_lis.configure(font=("Chelsea", 20))
    food_lis.pack(side="top", anchor=N, fill=X, expand=YES)
    food_lis = food_lis.nametowidget(food_lis.menuname)
    food_lis.configure(font=("Chelsea", 16))
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
    dessert_lis = OptionMenu(label3, dessert_var, *dessert)
    dessert_lis.config(width = 13)
    dessert_lis.configure(font=("Chelsea", 20))
    dessert_lis.pack(side=TOP, anchor=W, fill=X, expand=YES)
    dessert_lis = dessert_lis.nametowidget(dessert_lis.menuname)
    dessert_lis.configure(font=("Chelsea", 16))
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
    beverage_lis = OptionMenu(label3, beverage_var, *beverage)
    beverage_lis.config(width = 13)
    beverage_lis.pack(side=TOP, anchor=W, fill=X, expand=YES)
    beverage_lis.configure(font=("Chelsea", 20), bg="snow")
    beverage_lis = beverage_lis.nametowidget(beverage_lis.menuname)
    beverage_lis.configure(font=("Chelsea", 16))
    beverage_var.get()
    label3.pack(side=LEFT, padx=10, pady=10)
    button = Button(panel1, text="OK", command=calculate, padx=40, pady=15, bd=5, fg="black", bg="snow")
    button.pack(side='right')
    rootf.mainloop()


#-------First Page------#
root = tk.Tk()
image1 = tk.PhotoImage(file="Green_Lime_Blur.gif")
w = image1.width()
h = image1.height()


root.geometry("480x480+350+100")

panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')


font = tkFont.Font(size="25")
root.title("Calories Calculator")



label = tk.Label(panel1, text=" Calories Calculator ",font=("Chelsea", 40),fg='snow',bg='chartreuse4',compound='center')
label.pack(side='top', fill='both')





frame1 = Frame(root).pack(side = "left")
button2 = tk.Button(panel1, padx=30, pady=35, bd=5, 
                     text="คำนวณพลังงานของอาหาร",font=("CSPraJad", 20), fg="black", bg="snow", command=food)
button2.pack(expand=YES)
root.mainloop()

 
