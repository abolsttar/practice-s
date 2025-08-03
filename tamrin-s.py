"""tamrin1"""
import unittest

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
# print(f1, 'fahrenheit')

######################################
"""tamrin2"""

###################################################################Programming practice
# a = float(input('nm float 1: '))
# b = float(input('nm float 2: '))
# print((a + b) * 2)

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
#         nmb.append(int(inus))  # convert to number and add
#     except ValueError:
#         print('Please enter a valid number')
# print(max(nmb))
# print(nmb)
###################################################
# count = int(input("How many numbers do you want to enter?"))
# i = 1
# max_number = int(input(f"Enter number {i}: "))

# while i < count:
#     i += 1
#     num = int(input(f"Enter number {i}: "))
#     if num > max_number:
#         max_number = num

# print("Largest number:", max_number)
##################################################
# info = {
#     "Boualfazl":"Name" ,
#    "Tatar": "Family Name",
#     "18": "Age",
#     "Programmer": "Job"
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
# screen.title('My Accountant')
# screen.iconbitmap('e:tamrin/icon.ico')


# def seyHello(event):
#     os.system(f"python E:tamrin/msg/msgHello.py")
    



# but1= Button(screen,text="Register")
# but1.configure(bg='red', fg='white', pady=8,padx=8, font=('Simplified Arabic', 15, 'bold'))
# but1.place(x=0,y=50)
# but1.bind("<Button-1>", seyHello)


# screen.mainloop()
###################################################
"""تمرین 4"""
# from tkinter import *


# root = Tk()
# root.title('Simple Calculator')
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
#         entry.insert(END, 'Error')
#         expr = ''

# # buttons
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
#         cmd = lambda x=b: press(x)  # مشکل: lambda closure
#     Button(root, text=b, width=5, height=2, font=('Arial', 16), command=cmd).grid(row=row, column=col, padx=5, pady=5)
#     col += 1
#     if col > 3:
#         col = 0
#         row += 1

# root.mainloop()
# #############################################
# from tkinter import *
# root = Tk()

# root.title('BMI Calculator')
# root.geometry('390x350')

# label_height = Label(root, text="Height (cm):", font=('Arial', 18))
# label_height.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# ent_height = Entry(root, width=15, font=('Arial', 18), justify=RIGHT)
# ent_height.grid(row=0, column=1, padx=10, pady=10)

# label_weight = Label(root, text="Weight (kg):", font=('Arial', 18))
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
#             label_result.config(text="Height must be greater than zero!")
#             return
#         bmi_value = weight / (height ** 2)
#         label_result.config(text=f"Your BMI: {bmi_value:.2f}")
#     except ValueError:
#         label_result.config(text="Please enter a valid number!")

# Button(root, text="Calculate BMI", command=bmi, font=('Arial', 18), bd=5, relief=RIDGE).grid(row=2, column=0, columnspan=2, pady=10)

# root.mainloop()
############################################################
# sentence = input("Enter a sentence: ")

# words = sentence.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# max_count = max(word_count.values())

# most_common_words = [word for word, count in word_count.items() if count == max_count]

# print(f"Words with the most repetition ({max_count} times):")
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
# name = input('Name: ')
# family = input('Family Name: ')
# age = input('Age: ')
# use = {
#     'name': name,
#     'family': family,
#     'age': age
# }
# register(use)

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('Registration Form')
# root.geometry('500x800')
# root.resizable(False, False)

# # user list
# users = []

# # variables
# Name = StringVar()
# Family = StringVar()
# Age = StringVar()

# # variable to hold the index of user being edited
# editing_index = None

# # labels 
# Label(root, text=':Name', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=0, column=1, padx=10, pady=10, sticky='e')
# Label(root, text=':Family', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=1, column=1, padx=10, pady=10, sticky='e')
# Label(root, text=':Age', anchor='e', justify=RIGHT, font=('Tahoma', 12)).grid(row=2, column=1, padx=10, pady=10, sticky='e')

# # inputs
# entName = Entry(root, textvariable=Name, justify=RIGHT, font=('Tahoma', 12))
# entName.grid(row=0, column=0, padx=0, pady=10)
# entFamily = Entry(root, textvariable=Family, justify=RIGHT, font=('Tahoma', 12))
# entFamily.grid(row=1, column=0, padx=10, pady=10)
# entAge = Entry(root, textvariable=Age, justify=RIGHT, font=('Tahoma', 12))
# entAge.grid(row=2, column=0, padx=10, pady=10)


# error_label = Label(root, text='', fg='red', font=('Tahoma', 11), anchor='e', justify=RIGHT)
# error_label.grid(row=3, column=0, columnspan=2, sticky='w', padx=10)


# tbl = ttk.Treeview(root, columns=('Name', 'Family Name', 'Age'), show='headings', height=10)


# tbl.heading('Name', text='Name')
# tbl.heading('Family Name', text='Family Name') 
# tbl.heading('Age', text='Age')


# tbl.column('Name', width=150, anchor='center')
# tbl.column('Family Name', width=150, anchor='center')
# tbl.column('Age', width=100, anchor='center')


# tbl.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


# search_var = StringVar()


# def open_search_frame():
#     if hasattr(root, 'search_frame_widget') and root.search_frame_widget.winfo_exists():
#         return

#     search_frame = Frame(root, bd=2, relief=RIDGE)
#     search_frame.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='ew')
#     root.search_frame_widget = search_frame  

#     search_entry = Entry(search_frame, textvariable=search_var, font=('Tahoma', 12), width=20, justify=RIGHT)
#     search_entry.pack(side=RIGHT, padx=5)

#     search_button = Button(search_frame, text='جستجو', command=search_users, font=('Tahoma', 12))
#     search_button.pack(side=RIGHT, padx=5)

#     btn_close = Button(search_frame, text="بستن", command=search_frame.destroy, font=('Tahoma', 12), fg='red')
#     btn_close.pack(side=LEFT, padx=5)

# Button(root, text='Show Search Frame', command=open_search_frame, font=('Tahoma', 12)).grid(row=9, column=0, columnspan=2, pady=5)

# def search_users():
#     query = search_var.get().strip()

#     for item in tbl.get_children():
#         tbl.delete(item)
#     shown = set()  
#     if not query:
#         for user in users:
#             if user not in shown:
#                 parts = user.split(' - ')
#                 name_family = parts[0].split()
#                 name = name_family[0]
#                 family = name_family[1] if len(name_family) > 1 else ''
#                 age = parts[1].replace('Age: ', '') if len(parts) > 1 else ''
#                 tbl.insert('', 'end', values=(name, family, age))
#                 shown.add(user)
#     else:

#         for user in users:
#             if query in user and user not in shown:
#                 parts = user.split(' - ')
#                 name_family = parts[0].split()
#                 name = name_family[0]
#                 family = name_family[1] if len(name_family) > 1 else ''
#                 age = parts[1].replace('Age: ', '') if len(parts) > 1 else ''
#                 tbl.insert('', 'end', values=(name, family, age))
#                 shown.add(user)



# def is_duplicate_user(name, family, age):
#     user = f"{name} {family} - Age: {age}"
#     return user in users



# def register_user():
#     global editing_index
#     name = Name.get().strip()
#     family = Family.get().strip()
#     age = Age.get().strip()
#     error_label.config(text='')
#     if not name or not family or not age:
#         error_label.config(text='Please fill all fields.')
#         return
#     try:
#         age_int = int(age)
#     except ValueError:
#         error_label.config(text='Age must be a number.')
#         return
#     if age_int < 16:
#         error_label.config(text='Age must be at least 16 years.')
#         return

#     user = f"{name} {family} - Age: {age}"

#     if editing_index is not None:
#         if user != users[editing_index] and is_duplicate_user(name, family, age):
#             error_label.config(text='This user is already registered.')
#             return
#         users[editing_index] = user
#         editing_index = None
#     else:
#         if is_duplicate_user(name, family, age):
#             error_label.config(text='This user is already registered.')
#             return
#         users.append(user)
#     update_treeview()
#     Name.set("")
#     Family.set("")
#     Age.set("")
#     entName.focus_set()

# Button(root, text='Register', command=register_user, font=('Tahoma', 12)).grid(row=4, column=0, columnspan=2, pady=10)


# def update_treeview():
#     # clear all existing items
#     for item in tbl.get_children():
#         tbl.delete(item)
#     # add users from list
#     for user in users:
#         parts = user.split(' - ')
#         name_family = parts[0].split()
#         name = name_family[0]
#         family = name_family[1] if len(name_family) > 1 else ''
#         age = parts[1].replace('Age: ', '') if len(parts) > 1 else ''
#         tbl.insert('', 'end', values=(name, family, age))


# def delete_selected():
#     selected_item = tbl.selection()
#     if selected_item:

#         values = tbl.item(selected_item[0], 'values')
#         user_str = f"{values[0]} {values[1]} - Age: {values[2]}"

#         if user_str in users:
#             idx = users.index(user_str)
#             users.pop(idx)
#         tbl.delete(selected_item[0])
#     else:
#         error_label.config(text='Please select a user!')


# def edit_user():
#     global editing_index
#     selected_item = tbl.selection()
#     if selected_item:

#         values = tbl.item(selected_item[0], 'values')
#         name = values[0]
#         family = values[1]
#         age = values[2]

#         user_str = f"{name} {family} - Age: {age}"
#         try:
#             editing_index = users.index(user_str)
#         except ValueError:
#             editing_index = None
#         Name.set(name)
#         Family.set(family)
#         Age.set(age)
#         entName.focus_set()
#     else:
#         error_label.config(text='Please select a user!')

# Button(root, text='Delete Selected User', command=delete_selected, font=('Tahoma', 12)).grid(row=7, column=0, columnspan=2, pady=5)
# Button(root, text='Edit User', bg='#04ff00', fg='white', command=edit_user, font=('Tahoma', 12)).grid(row=8, column=0, columnspan=2, pady=5)

# root.mainloop()



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title} - {self.author} ({self.year})"

class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def info(self):
        return f"{super().info()} [Printed, Pages: {self.pages}]"

class EBook(Book):
    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self.file_format = file_format

    def info(self):
        return f"{super().info()} [Electronic, Format: {self.file_format}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

    def search(self, keyword):
        found = [book for book in self.books if keyword in book.title or keyword in book.author]
        if found:
            for book in found:
                print(book.info())
        else:
            print("No books found.")

    def show_all(self):
        if not self.books:
            print("No books in library.")
        for book in self.books:
            print(book.info())

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = PrintedBook("The Little Prince", "Antoine de Saint-Exupery", 1943, 120)
        self.book2 = EBook("Python for Everyone", "Charles Sever", 2016, "PDF")
        self.book3 = Book("Harry Potter", "J.K. Rowling", 1997)
    
    def test_library_initialization(self):
        self.assertEqual(len(self.library.books), 0)
        self.assertIsInstance(self.library.books, list)
    
    def test_add_book(self):
        initial_count = len(self.library.books)
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library.books), initial_count + 1)
        self.assertIn(self.book1, self.library.books)
    
    def test_add_multiple_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.assertEqual(len(self.library.books), 3)
    
    def test_remove_book_existing(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        initial_count = len(self.library.books)
        self.library.remove_book("The Little Prince")
        self.assertEqual(len(self.library.books), initial_count - 1)
        self.assertNotIn(self.book1, self.library.books)
    
    def test_remove_book_nonexistent(self):
        self.library.add_book(self.book1)
        initial_count = len(self.library.books)
        self.library.remove_book("Non-existent Book")
        self.assertEqual(len(self.library.books), initial_count)
    
    def test_search_by_title(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        try:
            self.library.search("Little")
        except Exception as e:
            self.fail(f"Search method failed: {e}")
    
    def test_search_by_author(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        try:
            self.library.search("Antoine")
        except Exception as e:
            self.fail(f"Search method failed: {e}")
    
    def test_search_nonexistent(self):
        self.library.add_book(self.book1)
        try:
            self.library.search("Word that doesn't exist")
        except Exception as e:
            self.fail(f"Search method failed: {e}")
    
    def test_show_all_empty(self):
        try:
            self.library.show_all()
        except Exception as e:
            self.fail(f"Show all method failed: {e}")
    
    def test_show_all_with_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        try:
            self.library.show_all()
        except Exception as e:
            self.fail(f"Show all method failed: {e}")

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Book Title", "Author", 2023)
        self.assertEqual(book.title, "Book Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2023)
    
    def test_book_info(self):
        book = Book("Book Title", "Author", 2023)
        expected_info = "Book Title - Author (2023)"
        self.assertEqual(book.info(), expected_info)

class TestPrintedBook(unittest.TestCase):
    def test_printed_book_creation(self):
        book = PrintedBook("Title", "Author", 2023, 200)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.pages, 200)
    
    def test_printed_book_info(self):
        book = PrintedBook("Title", "Author", 2023, 200)
        expected_info = "Title - Author (2023) [Printed, Pages: 200]"
        self.assertEqual(book.info(), expected_info)

class TestEBook(unittest.TestCase):
    def test_ebook_creation(self):
        book = EBook("Title", "Author", 2023, "PDF")
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.file_format, "PDF")
    
    def test_ebook_info(self):
        book = EBook("Title", "Author", 2023, "PDF")
        expected_info = "Title - Author (2023) [Electronic, Format: PDF]"
        self.assertEqual(book.info(), expected_info)

if __name__ == "__main__":
    unittest.main()

