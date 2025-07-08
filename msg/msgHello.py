from tkinter import *

screen = Tk()

screen.geometry('%dx%d+%d+%d' % (400, 95, 500, 400))
screen.title('پیام خوش آمد گویی')
screen.iconbitmap('e:tamrin/icon.ico')
def close():
    screen.destroy()

titel = Label(screen, text='خوش آمدید', bg='black', fg='white', font=('Simplified Arabic', 30, 'bold'), anchor='s').pack(fill=BOTH, side=TOP)
but1= Button(screen,text="بستن فرم", width=50, command=close).pack(fill=BOTH)


screen.mainloop()