from Tkinter import *
import tkFont

def ok():
    print "value is", text1.get()
    print "value is", variable.get()

def weight():
    root = Tk()
    root.geometry("400x350+200+200")
    root.title("Calories Calculator")
    Label(root, text="First").grid(row=0, sticky=W)
    Label(root, text="Second").grid(row=1, sticky=W)
    e1 = Entry(root)
    e2 = Entry(root)
    button1 = Button(root, text="คำนวณ", fg="black")
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    button1.grid(row=2, column=2)
    root.mainloop()
def food():
    global text1, variable
    root = Tk()
    root.geometry("400x350+200+200")
    root.title("Food Selecter")
    label = Label(root, text="Food Selecter",font=("Britannic Bold", 30),bg="white",fg="black")
    label.grid(row=0,column=1)
    Label(root, text=" ",font=("Britannic Bold", 20)).grid(row=1, sticky=W)
    Label(root, text="อาหารคาว",font=("Britannic Bold", 20)).grid(row=2, sticky=W)
    Label(root, text="ของหวาน",font=("Britannic Bold", 20)).grid(row=3, sticky=W)
    Label(root, text="เครื่องดื่ม",font=("Britannic Bold", 20)).grid(row=4, sticky=W)
    food1 = ['ข้าวผัดหมู','แกงเขียวหวาน','กบทอด','ข้าวไข่ดาว','ข้าวขาหมู','ข้าวไกย่าง','แกงเขียวหวาน']
    variable = StringVar(root)
    variable.set(food1[0])
    w = apply(OptionMenu, (root, variable) + tuple(food1))
    w.grid(row=2, column=1)
    text1 = StringVar(root)
    entry = Entry(root, textvariable=text1)
    text1.set(0)
    entry.grid(row=4, column=1)
    button = Button(root, text="OK", command=ok)
    button.grid(row=5, column=1)
    root.mainloop()



root = Tk()
root.geometry("400x350+200+200")
font = tkFont.Font(size="25")
root.title("Calories Calculator")
label = Label(root, text="Calories Calculator",font=("Britannic Bold", 30),bg="white",fg="black")
label.pack(fill=X)

frame1 = Frame(root).pack(side = "top")
button1 = Button(frame1, padx=15, pady=35, bd=15,
                     text="คำนวณพร้อมน้ำหนัก,เพศและส่วนสูง",font=("AngsanaNew", 20), fg="white", bg="red", command=weight)
button1.pack()
button2 = Button(frame1, padx=30, pady=35, bd=15, 
                     text="คำนวณเฉพาะพลังงานของอาหาร",font=("AngsanaNew", 20), fg="black", bg="yellow", command=food)
button2.pack()

root.mainloop()

 
