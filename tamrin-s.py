"""tamrin1"""
# a = (int(input('n1')))
# aq = (int(input('n2')))
# if a > aq:
#     print( a)
# elif aq > a:
#     print( aq)

# tol = (int(input('tol: ')))
# arz = (int(input('arz: ')))
# print(tol * arz)

# cg = (int(input('dma_cg: ')))
# f1 = (cg*9/5)+32
# print(f1, f'farenhait') 

######################################
"""tamrin2"""

###################################################################Programming practice
# a = float(input('nm float 1: '))
# b = float(input('nm float 2: '))
# print((a +b )* 2)

# a = int(input('nm: '))
# if a % 2 ==0:
#     print('zoj')
# else:
#     print('favd')

# _1 =int(input('nm1: '))
# _2 =int(input('nm2: '))
# _3 =int(input('nm3: '))

# print((_1 + _2 + _3)//3)

################################################
"""تمرین 3"""

# nmb=[]

# while True:
#     inus =input('nmb: (for end :"don")')
#     if inus == "don":
#         break
#     try :
#         int(inus)
#         nmb.append(inus)
#     except:
#         print('?')
# print(max(nmb))
# print(nmb)
###################################################
# count = int(input("کنید؟ وارد میخواهید عدد چند"))
# i = 1
# max_number = int(input(f" :کنید وارد را{i}عدد"))

# while i < count:
#     i += 1
#     num = int(input(f" :کنید وارد را{i}عدد"))
#     if num > max_number:
#         max_number = num

# print("بزرگترین عدد:", max_number)
##################################################
# info = {
#     "بوالفضل":"نام" ,
#    "تتار": " خانوادگی نام",
#     "18": "سن",
#     "برنامه‌نویس": "شغل"
# }

# for key in info:
#     print(f"{key}: {info[key]}")
#################################################
# import os
# import tkinter
# from tkinter import *
# from tkinter import messagebox
# screen = Tk()

# screen.geometry('%dx%d+%d+%d' % (1000, 400, 140, 200))
# screen.title('حسابدار من')
# screen.iconbitmap('e:tamrin/icon.ico')


# def seyHello(event):
#     os.system(f"python E:tamrin/msg/msgHello.py")
    



# but1= Button(screen,text="ثبت نام")
# but1.configure(bg='red', fg='white', pady=8,padx=8, font=('Simplified Arabic', 15, 'bold'))
# but1.place(x=0,y=50)
# but1.bind("<Button-1>", seyHello)


# screen.mainloop()
###################################################
"""تمرین 4"""
# from tkinter import *


# root = Tk()
# root.title('ماشین حساب ساده')
# root.geometry('325x365')


# entry = Entry(root, width=20, font=('Arial', 20), bd=5, relief=RIDGE, justify=RIGHT)
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# expr = ''

# def press(key):
#     global expr
#     expr += str(key)
#     entry.delete(0, END)
#     entry.insert(END, expr)

# def clear():
#     global expr
#     expr = ''
#     entry.delete(0, END)

# def equal():
#     global expr
#     try:
#         result = str(eval(expr))
#         entry.delete(0, END)
#         entry.insert(END, result)
#         expr = ''
#     except:
#         entry.delete(0, END)
#         entry.insert(END, 'خطا')
#         expr = ''

# # دکمه‌ها
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', 'C', '=', '+'
# ]

# row = 1
# col = 0
# for b in buttons:
#     if b == 'C':
#         cmd = clear
#     elif b == '=':
#         cmd = equal
#     else:
#         cmd = lambda x=b: press(x)
#     Button(root, text=b, width=5, height=2, font=('Arial', 16), command=cmd).grid(row=row, column=col, padx=5, pady=5)
#     col += 1
#     if col > 3:
#         col = 0
#         row += 1

# root.mainloop()
# #############################################
# from tkinter import *
# root = Tk()

# root.title('BMI محاسبه')
# root.geometry('390x350')

# label_height = Label(root, text="قد (سانتی متر):", font=('Arial', 18))
# label_height.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# ent_height = Entry(root, width=15, font=('Arial', 18), justify=RIGHT)
# ent_height.grid(row=0, column=1, padx=10, pady=10)

# label_weight = Label(root, text="وزن (کیلوگرم):", font=('Arial', 18))
# label_weight.grid(row=1, column=0, padx=10, pady=10, sticky='e')
# ent_weight = Entry(root, width=15, font=('Arial', 18), justify=RIGHT)
# ent_weight.grid(row=1, column=1, padx=10, pady=10)

# label_result = Label(root, text="", font=('Arial', 18), fg='blue')
# label_result.grid(row=3, column=0, columnspan=2, pady=20)

# def bmi():
#     try:
#         height_cm = float(ent_height.get())
#         weight = float(ent_weight.get())
#         height = height_cm / 100 
#         if height <= 0:
#             label_result.config(text="قد باید بیشتر از صفر باشد!")
#             return
#         bmi_value = weight / (height ** 2)
#         label_result.config(text=f"BMI شما: {bmi_value:.2f}")
#     except ValueError:
#         label_result.config(text="لطفاً عدد معتبر وارد کنید!")

# Button(root, text="محاسبه BMI", command=bmi, font=('Arial', 18), bd=5, relief=RIDGE).grid(row=2, column=0, columnspan=2, pady=10)

# root.mainloop()
############################################################
# sentence = input("یک جمله وارد کنید: ")

# words = sentence.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# max_count = max(word_count.values())

# most_common_words = [word for word, count in word_count.items() if count == max_count]

# print(f"کلمه(ها)یی که بیشترین تکرار را دارند ({max_count} بار):")
# for word in most_common_words:
#     print(f"'{word}'")
##########################################################################
# userAll=[]
# def register(user):
#     human={'name':user['name'],'family':user['family'], 'age':user['age']}
#     if int(user['age'])>=18:
#         userAll.append(human)
#         print('ok')
#     else:
#         print('nmtonim')
# name = input('نام: ')
# family = input('نام خانوادگی: ')
# age = input('سن: ')
# use = {
#     'name': name,
#     'family': family,
#     'age': age
# }
# register(use)

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('فرم ثبت نام')
# root.geometry('500x800')
# root.resizable(False, False)

# # لیست کاربران
# users = []

# # متغیرها
# Name = StringVar()
# Family = StringVar()
# Age = StringVar()

# # متغیر برای نگهداری اندیس کاربر در حال ویرایش
# editing_index = None

# # لیبل‌ها 
# Label(root, text=':نام', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=0, column=1, padx=10, pady=10, sticky='e')
# Label(root, text=':فامیل', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=1, column=1, padx=10, pady=10, sticky='e')
# Label(root, text=':"سن', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=2, column=1, padx=10, pady=10, sticky='e')

# # ورودی‌ها
# entName = Entry(root, textvariable=Name, justify=RIGHT, font=('Tahoma', 12))
# entName.grid(row=0, column=0, padx=0, pady=10)
# entFamily = Entry(root, textvariable=Family, justify=RIGHT, font=('Tahoma', 12))
# entFamily.grid(row=1, column=0, padx=10, pady=10)
# entAge = Entry(root, textvariable=Age, justify=RIGHT, font=('Tahoma', 12))
# entAge.grid(row=2, column=0, padx=10, pady=10)

# # لیبل خطا
# error_label = Label(root, text='', fg='red', font=('Tahoma', 11), anchor='e', justify=RIGHT)
# error_label.grid(row=3, column=0, columnspan=2, sticky='w', padx=10)

# # ایجاد Treeview برای نمایش اطلاعات کاربران
# tbl = ttk.Treeview(root, columns=('نام', 'نام خانوادگی', 'سن'), show='headings', height=10)

# # تنظیم عناوین ستون‌ها
# tbl.heading('نام', text='نام')
# tbl.heading('نام خانوادگی', text='نام خانوادگی') 
# tbl.heading('سن', text='سن')

# # تنظیم عرض ستون‌ها
# tbl.column('نام', width=150, anchor='center')
# tbl.column('نام خانوادگی', width=150, anchor='center')
# tbl.column('سن', width=100, anchor='center')

# # قرار دادن Treeview در پنجره
# tbl.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# # --- افزودن تکست‌باکس و دکمه جستجو ---
# search_var = StringVar()

# # تابع ساخت و نمایش فریم جستجو با قابلیت بسته شدن
# def open_search_frame():
#     # اگر قبلاً ساخته شده، دوباره نسازد
#     if hasattr(root, 'search_frame_widget') and root.search_frame_widget.winfo_exists():
#         return

#     search_frame = Frame(root, bd=2, relief=RIDGE)
#     search_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='ew')
#     root.search_frame_widget = search_frame  # برای دسترسی بعدی

#     search_entry = Entry(search_frame, textvariable=search_var, font=('Tahoma', 12), width=20, justify=RIGHT)
#     search_entry.pack(side=RIGHT, padx=5)

#     search_button = Button(search_frame, text='جستجو', command=search_users, font=('Tahoma', 12))
#     search_button.pack(side=RIGHT, padx=5)

#     btn_close = Button(search_frame, text="بستن", command=search_frame.destroy, font=('Tahoma', 12), fg='red')
#     btn_close.pack(side=LEFT, padx=5)

# # دکمه برای نمایش فریم جستجو
# Button(root, text='نمایش فریم جستجو', command=open_search_frame, font=('Tahoma', 12)).grid(row=9, column=0, columnspan=2, pady=5)

# def search_users():
#     query = search_var.get().strip()
#     # پاک کردن Treeview
#     for item in tbl.get_children():
#         tbl.delete(item)
#     shown = set()  # برای جلوگیری از تکرار
#     if not query:
#         # اگر جستجو خالی بود، همه را نمایش بده
#         for user in users:
#             if user not in shown:
#                 parts = user.split(' - ')
#                 name_family = parts[0].split()
#                 name = name_family[0]
#                 family = name_family[1] if len(name_family) > 1 else ''
#                 age = parts[1].replace('سن: ', '') if len(parts) > 1 else ''
#                 tbl.insert('', 'end', values=(name, family, age))
#                 shown.add(user)
#     else:
#         # فقط کاربران مطابق را نمایش بده
#         for user in users:
#             if query in user and user not in shown:
#                 parts = user.split(' - ')
#                 name_family = parts[0].split()
#                 name = name_family[0]
#                 family = name_family[1] if len(name_family) > 1 else ''
#                 age = parts[1].replace('سن: ', '') if len(parts) > 1 else ''
#                 tbl.insert('', 'end', values=(name, family, age))
#                 shown.add(user)

# # تابع بررسی تکراری بودن کاربر

# def is_duplicate_user(name, family, age):
#     user = f"{name} {family} - سن: {age}"
#     return user in users

# # تابع ثبت نام
# # فقط یک بار تعریف شود و Treeview و Listbox را همزمان بروزرسانی کند

# def register_user():
#     global editing_index
#     name = Name.get().strip()
#     family = Family.get().strip()
#     age = Age.get().strip()
#     error_label.config(text='')
#     if not name or not family or not age:
#         error_label.config(text='لطفاً همه فیلدها را پر کنید.')
#         return
#     try:
#         age_int = int(age)
#     except ValueError:
#         error_label.config(text='سن باید عدد باشد.')
#         return
#     if age_int < 16:
#         error_label.config(text='سن باید حداقل 16 سال باشد.')
#         return

#     user = f"{name} {family} - سن: {age}"
#     # اگر در حالت ویرایش هستیم
#     if editing_index is not None:
#         # بررسی تکراری بودن فقط اگر اطلاعات تغییر کرده باشد
#         if user != users[editing_index] and is_duplicate_user(name, family, age):
#             error_label.config(text='این کاربر قبلاً ثبت شده است.')
#             return
#         users[editing_index] = user
#         editing_index = None
#     else:
#         if is_duplicate_user(name, family, age):
#             error_label.config(text='این کاربر قبلاً ثبت شده است.')
#             return
#         users.append(user)
#     update_treeview()
#     Name.set("")
#     Family.set("")
#     Age.set("")
#     entName.focus_set()

# Button(root, text='ثبت نام', command=register_user, font=('Tahoma', 12)).grid(row=4, column=0, columnspan=2, pady=10)

# # تابع بروزرسانی Treeview
# def update_treeview():
#     # پاک کردن تمام آیتم‌های موجود
#     for item in tbl.get_children():
#         tbl.delete(item)
#     # اضافه کردن کاربران از لیست
#     for user in users:
#         parts = user.split(' - ')
#         name_family = parts[0].split()
#         name = name_family[0]
#         family = name_family[1] if len(name_family) > 1 else ''
#         age = parts[1].replace('سن: ', '') if len(parts) > 1 else ''
#         tbl.insert('', 'end', values=(name, family, age))

# # دکمه حذف کاربر انتخاب شده
# def delete_selected():
#     selected_item = tbl.selection()
#     if selected_item:
#         # گرفتن اطلاعات کاربر انتخاب شده
#         values = tbl.item(selected_item[0], 'values')
#         user_str = f"{values[0]} {values[1]} - سن: {values[2]}"
#         # حذف از Treeview

#         tbl.delete(selected_item[0])
#         # حذف از لیست users و Listbox
#         if user_str in users:
#             idx = users.index(user_str)
#             users.pop(idx)


# def edit_user():
#     global editing_index
#     selected_item = tbl.selection()
#     if selected_item:
#         # گرفتن اطلاعات کاربر انتخاب شده
#         values = tbl.item(selected_item[0], 'values')
#         name = values[0]
#         family = values[1]
#         age = values[2]
#         # پیدا کردن اندیس کاربر در users
#         user_str = f"{name} {family} - سن: {age}"
#         try:
#             editing_index = users.index(user_str)
#         except ValueError:
#             editing_index = None
#         # قرار دادن اطلاعات در فیلدهای ورودی
#         Name.set(name)
#         Family.set(family)
#         Age.set(age)
#         # فوکوس روی فیلد نام
#         entName.focus_set()
#     else:
#         error_label.config(text='لطفاً یک کاربر را انتخاب کنید!')

# Button(root, text='حذف کاربر انتخاب شده', command=delete_selected, font=('Tahoma', 12)).grid(row=7, column=0, columnspan=2, pady=5)
# Button(root, text='ویراش کاربر', bg='#04ff00', fg='white', command=edit_user, font=('Tahoma', 12)).grid(row=8, column=0, columnspan=2, pady=5)

# root.mainloop()

# # #######################################################
# # کلاس پایه کتاب
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def info(self):
#         return f"{self.title} - {self.author} ({self.year})"

# # زیرکلاس کتاب چاپی
# class PrintedBook(Book):
#     def __init__(self, title, author, year, pages):
#         super().__init__(title, author, year)
#         self.pages = pages

#     def info(self):
#         return f"{super().info()} [چاپی، صفحات: {self.pages}]"

# # زیرکلاس کتاب الکترونیکی
# class EBook(Book):
#     def __init__(self, title, author, year, file_format):
#         super().__init__(title, author, year)
#         self.file_format = file_format

#     def info(self):
#         return f"{super().info()} [الکترونیکی، فرمت: {self.file_format}]"

# # کلاس مدیریت کتابخانه
# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)
#         print("کتاب با موفقیت اضافه شد.")

#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 print("کتاب حذف شد.")
#                 return
#         print("کتاب پیدا نشد.")

#     def search(self, keyword):
#         found = [book for book in self.books if keyword in book.title or keyword in book.author]
#         if found:
#             for book in found:
#                 print(book.info())
#         else:
#             print("کتابی پیدا نشد.")

#     def show_all(self):
#         if not self.books:
#             print("کتابی در کتابخانه وجود ندارد.")
#         for book in self.books:
#             print(book.info())

# # نمونه استفاده:
# lib = Library()
# lib.add_book(PrintedBook("شازده کوچولو", "آنتوان دو سنت اگزوپری", 1943, 120))
# lib.add_book(EBook("پایتون برای همه", "چارلز سیور", 2016, "PDF"))
# lib.show_all()
# lib.search("پایتون")
# lib.remove_book("شازده کوچولو")
# lib.show_all()
##################
# from abc import ABC, abstractmethod
# from multiprocessing import set_forkserver_preload
# class Person(ABC):
#     def fard (self, name, age ):
#         self.name = name
#         self.age = age


# @abstractmethod
# def info(self):
#     pass


