import tkinter as tk
from tkinter import messagebox, ttk
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['registration_db']
collection = db['users']

def register():
    name = name_entry.get()
    family = family_entry.get()
    age = age_entry.get()
    
    if name and family and age:
        try:
            age = int(age)
            
            user_data = {
                "name": name,
                "family": family,
                "age": age
            }
            result = collection.insert_one(user_data)
            
            messagebox.showinfo("موفق", f"ثبت نام: {name} {family}\nسن: {age}\nID: {result.inserted_id}")
            
            name_entry.delete(0, tk.END)
            family_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            refresh_user_list()
            
        except ValueError:
            messagebox.showerror("خطا", "سن باید عدد باشد")
        except Exception as e:
            messagebox.showerror("خطا", f"مشکل در ذخیره: {e}")
    else:
        messagebox.showerror("خطا", "همه فیلدها را پر کنید")

def search_user():
    search_id = search_entry.get()
    if search_id:
        try:
            from bson import ObjectId
            user = collection.find_one({"_id": ObjectId(search_id)})
            if user:
                name_entry.delete(0, tk.END)
                family_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                
                name_entry.insert(0, user['name'])
                family_entry.insert(0, user['family'])
                age_entry.insert(0, str(user['age']))
                
                messagebox.showinfo("یافت شد", f"کاربر با ID: {search_id} یافت شد")
            else:
                messagebox.showerror("خطا", "کاربر یافت نشد")
        except Exception as e:
            messagebox.showerror("خطا", f"مشکل در جستجو: {e}")
    else:
        messagebox.showerror("خطا", "لطفاً ID را وارد کنید")

def update_user():
    search_id = search_entry.get()
    if search_id:
        try:
            from bson import ObjectId
            name = name_entry.get()
            family = family_entry.get()
            age = age_entry.get()
            
            if name and family and age:
                age = int(age)
                result = collection.update_one(
                    {"_id": ObjectId(search_id)},
                    {"$set": {"name": name, "family": family, "age": age}}
                )
                
                if result.modified_count > 0:
                    messagebox.showinfo("موفق", "اطلاعات کاربر بروزرسانی شد")
                    clear_fields()
                    refresh_user_list()
                else:
                    messagebox.showerror("خطا", "کاربر یافت نشد")
            else:
                messagebox.showerror("خطا", "همه فیلدها را پر کنید")
        except ValueError:
            messagebox.showerror("خطا", "سن باید عدد باشد")
        except Exception as e:
            messagebox.showerror("خطا", f"مشکل در بروزرسانی: {e}")
    else:
        messagebox.showerror("خطا", "لطفاً ID را وارد کنید")

def delete_user():
    search_id = search_entry.get()
    if search_id:
        try:
            from bson import ObjectId
            result = collection.delete_one({"_id": ObjectId(search_id)})
            
            if result.deleted_count > 0:
                messagebox.showinfo("موفق", "کاربر حذف شد")
                clear_fields()
                refresh_user_list()
            else:
                messagebox.showerror("خطا", "کاربر یافت نشد")
        except Exception as e:
            messagebox.showerror("خطا", f"مشکل در حذف: {e}")
    else:
        messagebox.showerror("خطا", "لطفاً ID را وارد کنید")

def clear_fields():
    name_entry.delete(0, tk.END)
    family_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

def refresh_user_list():
    user_list.delete(0, tk.END)
    for user in collection.find():
        user_list.insert(tk.END, f"ID: {user['_id']} - {user['name']} {user['family']}")

root = tk.Tk()
root.title("مدیریت کاربران")
root.geometry("600x500")

font_family = "Tahoma"
font_size = 12

search_frame = tk.Frame(root)
search_frame.pack(fill="x", padx=20, pady=10)

search_label = tk.Label(search_frame, text="جستجو با ID:", font=(font_family, font_size))
search_label.pack(side="right", padx=5)
search_entry = tk.Entry(search_frame, font=(font_family, font_size), width=20)
search_entry.pack(side="right", padx=5)

search_button = tk.Button(search_frame, text="جستجو", command=search_user, font=(font_family, font_size))
search_button.pack(side="right", padx=5)

input_frame = tk.Frame(root)
input_frame.pack(fill="x", padx=20, pady=10)

name_label = tk.Label(input_frame, text="نام:", font=(font_family, font_size), anchor="e")
name_label.pack(fill="x", pady=5)
name_entry = tk.Entry(input_frame, font=(font_family, font_size), justify="right")
name_entry.pack(fill="x", pady=5)

family_label = tk.Label(input_frame, text="فامیلی:", font=(font_family, font_size), anchor="e")
family_label.pack(fill="x", pady=5)
family_entry = tk.Entry(input_frame, font=(font_family, font_size), justify="right")
family_entry.pack(fill="x", pady=5)

age_label = tk.Label(input_frame, text="سن:", font=(font_family, font_size), anchor="e")
age_label.pack(fill="x", pady=5)
age_entry = tk.Entry(input_frame, font=(font_family, font_size), justify="right")
age_entry.pack(fill="x", pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

register_button = tk.Button(button_frame, text="ثبت نام", command=register, font=(font_family, font_size), 
                           bg="#4CAF50", fg="white", relief="flat", padx=20)
register_button.pack(side="left", padx=5)

update_button = tk.Button(button_frame, text="بروزرسانی", command=update_user, font=(font_family, font_size), 
                          bg="#2196F3", fg="white", relief="flat", padx=20)
update_button.pack(side="left", padx=5)

delete_button = tk.Button(button_frame, text="حذف", command=delete_user, font=(font_family, font_size), 
                         bg="#f44336", fg="white", relief="flat", padx=20)
delete_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="پاک کردن", command=clear_fields, font=(font_family, font_size), 
                        bg="#FF9800", fg="white", relief="flat", padx=20)
clear_button.pack(side="left", padx=5)

list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

list_label = tk.Label(list_frame, text="لیست کاربران:", font=(font_family, font_size))
list_label.pack(anchor="e")

user_list = tk.Listbox(list_frame, font=(font_family, font_size), height=10)
user_list.pack(fill="both", expand=True)

refresh_user_list()

root.mainloop() 