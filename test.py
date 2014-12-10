from Tkinter import *
root = Tk()                

win = Toplevel(root)       
win.title('Sing...')       
win.protocol('WM_DELETE_WINDOW', lambda:0)

msg = Button(win, text='Text', command=win.destroy)
msg.pack(expand=YES, fill=BOTH)
msg.config(padx=10, pady=10, bd=10, relief=RAISED)
msg.config(bg='black', fg='red', font=('times', 30, 'bold italic'))

root.title('Lumberjack demo')
Label(root, text='Main window', width=30).pack()
Button(root, text='Quit All', command=root.quit).pack()
root.mainloop()
