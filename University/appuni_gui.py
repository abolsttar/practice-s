import tkinter as tk
from tkinter import ttk, messagebox
import appuni

def is_persian_text(text):
    """Check if text contains Persian characters"""
    if not text:
        return False
    persian_chars = set('ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی')
    return any(char in persian_chars for char in text)

def create_smart_label(parent, text, **kwargs):
    """Create label with appropriate font based on text content"""
    if is_persian_text(text):
        font = ('Tahoma', 14, 'bold')
    else:
        font = ('Tahoma', 12)
    
    return tk.Label(parent, text=text, font=font, **kwargs)

def create_smart_entry(parent, **kwargs):
    """Create entry with appropriate font for Persian text"""
    font = ('Tahoma', 12)
    return tk.Entry(parent, font=font, **kwargs)

BG_DARK = '#0A0A0A'
BG_DARKER = '#050505'
FG_GOLD = '#FFD700'
FG_GOLD_LIGHT = '#FFE55C'
FG_WHITE = '#F5F5F5'
FG_GRAY = '#CCCCCC'
BTN_BG = '#1A1A1A'
BTN_BG_HOVER = '#2A2A2A'
BTN_FG = FG_GOLD
ENTRY_BG = '#1A1A1A'
ENTRY_FG = FG_WHITE
HIGHLIGHT_BG = '#2A2A2A'
CARD_BG = '#151515'
BORDER_COLOR = '#333333'
SHADOW_COLOR = '#000000'

class AppUniGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('سیستم مدیریت دانشگاه - University Management System')
        self.geometry('1200x800')
        self.configure(bg=BG_DARK)
        self.resizable(True, True)
        self.load_data()
        self._setup_style()
        self._show_login()
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        
        style.configure('Main.TFrame', background=BG_DARK)
        style.configure('Card.TFrame', background=CARD_BG, relief='flat', borderwidth=0)
        style.configure('Glass.TFrame', background=BG_DARKER, relief='flat', borderwidth=0)
        
        style.configure('Title.TLabel', background=BG_DARK, foreground=FG_GOLD, 
                       font=('Tahoma', 24, 'bold'))
        style.configure('Subtitle.TLabel', background=BG_DARK, foreground=FG_GOLD_LIGHT, 
                       font=('Tahoma', 16, 'bold'))
        style.configure('Header.TLabel', background=BG_DARK, foreground=FG_GOLD, 
                       font=('Tahoma', 14, 'bold'))
        style.configure('Normal.TLabel', background=BG_DARK, foreground=FG_WHITE, 
                       font=('Tahoma', 12))
        style.configure('Small.TLabel', background=BG_DARK, foreground=FG_GRAY, 
                       font=('Tahoma', 10))
        
        style.configure('Primary.TButton', 
                       background=BTN_BG, foreground=BTN_FG, 
                       font=('Tahoma', 12, 'bold'), padding=(20, 8),
                       relief='flat', borderwidth=0)
        style.map('Primary.TButton', 
                 background=[('active', FG_GOLD), ('pressed', FG_GOLD_LIGHT)], 
                 foreground=[('active', BG_DARK), ('pressed', BG_DARK)])
        
        style.configure('Secondary.TButton', 
                       background=HIGHLIGHT_BG, foreground=FG_WHITE, 
                       font=('Tahoma', 11), padding=(15, 6),
                       relief='flat', borderwidth=0)
        style.map('Secondary.TButton',
                 background=[('active', BTN_BG_HOVER), ('pressed', BTN_BG)],
                 foreground=[('active', FG_GOLD), ('pressed', FG_GOLD)])
        
        style.configure('Treeview', 
                       background=CARD_BG, foreground=FG_WHITE, 
                       fieldbackground=CARD_BG, font=('Tahoma', 11),
                       relief='flat', borderwidth=0)
        style.configure('Treeview.Heading', 
                       background=BTN_BG, foreground=FG_GOLD, 
                       font=('Tahoma', 12, 'bold'),
                       relief='flat', borderwidth=0)
        style.map('Treeview', 
                 background=[('selected', FG_GOLD)], 
                 foreground=[('selected', BG_DARK)])
        
        style.configure('Modern.TEntry', 
                       fieldbackground=ENTRY_BG, foreground=ENTRY_FG,
                       relief='flat', borderwidth=0)

    def load_data(self):
        try:
            appuni.load_all()
        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        try:
            appuni.save_all()
        except Exception as e:
            print(f"Error saving data: {e}")

    def _on_closing(self):
        self.save_data()
        self.quit()

    def _clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _show_login(self):
        self._clear()
        
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True)
        
        self._create_background_decoration(main_frame)
        
        login_container = ttk.Frame(main_frame, style='Main.TFrame')
        login_container.place(relx=0.5, rely=0.5, anchor='center')
        
        login_card = tk.Frame(login_container, bg=CARD_BG, relief='flat', bd=0)
        login_card.pack(padx=20, pady=20)
        
        shadow_frame = tk.Frame(login_container, bg=SHADOW_COLOR, relief='flat', bd=0)
        shadow_frame.place(relx=0.5, rely=0.5, anchor='center', x=3, y=3)
        shadow_frame.lower()
        
        card_content = ttk.Frame(login_card, style='Card.TFrame')
        card_content.pack(padx=40, pady=40)
        
        logo_frame = ttk.Frame(card_content, style='Card.TFrame')
        logo_frame.pack(pady=(0, 20))
        
        logo_label = tk.Label(logo_frame, text='🎓', font=('Tahoma', 48), 
                            bg=CARD_BG, fg=FG_GOLD)
        logo_label.pack()
        
        title_frame = ttk.Frame(card_content, style='Card.TFrame')
        title_frame.pack(pady=(0, 30))
        
        create_smart_label(title_frame, 'سیستم مدیریت دانشگاه', 
                 bg=CARD_BG, fg=FG_GOLD).pack()
        ttk.Label(title_frame, text='University Management System', 
                 style='Subtitle.TLabel').pack(pady=(5, 0))
        
        form_frame = ttk.Frame(card_content, style='Card.TFrame')
        form_frame.pack(fill='x', pady=20)
        
        username_frame = ttk.Frame(form_frame, style='Card.TFrame')
        username_frame.pack(fill='x', pady=10)
        
        create_smart_label(username_frame, '👤 نام کاربری', bg=CARD_BG, fg=FG_WHITE).pack(anchor='e', pady=(0, 8))
        
        username_entry = create_smart_entry(username_frame, 
                                bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                                relief='flat', bd=15, highlightthickness=1,
                                highlightbackground=BORDER_COLOR, highlightcolor=FG_GOLD)
        username_entry.pack(fill='x', pady=(0, 5))
        
        password_frame = ttk.Frame(form_frame, style='Card.TFrame')
        password_frame.pack(fill='x', pady=10)
        
        create_smart_label(password_frame, '🔒 رمز عبور', bg=CARD_BG, fg=FG_WHITE).pack(anchor='e', pady=(0, 8))
        
        password_entry = create_smart_entry(password_frame, 
                                bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                                relief='flat', bd=15, highlightthickness=1,
                                highlightbackground=BORDER_COLOR, highlightcolor=FG_GOLD,
                                show='●')
        password_entry.pack(fill='x', pady=(0, 5))
        
        button_frame = ttk.Frame(card_content, style='Card.TFrame')
        button_frame.pack(pady=30)
        
        def do_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            
            if appuni.login(username, password):
                self._show_dashboard()
            else:
                messagebox.showerror('خطا', 'نام کاربری یا رمز عبور اشتباه است!')
        
        login_btn = tk.Button(button_frame, text='🚀 ورود به سیستم', 
                             font=('Tahoma', 14, 'bold'), bg=BTN_BG, fg=BTN_FG,
                             relief='flat', bd=0, padx=25, pady=10,
                             command=do_login)
        login_btn.pack(fill='x')
        
        hint_frame = ttk.Frame(card_content, style='Card.TFrame')
        hint_frame.pack(pady=(20, 0))
        
        hint_text = '💡 نام کاربری: admin | رمز عبور: admin'
        ttk.Label(hint_frame, text=hint_text, style='Small.TLabel').pack()
        
        username_entry.bind('<Return>', lambda e: password_entry.focus())
        password_entry.bind('<Return>', lambda e: do_login())
        username_entry.focus()
        
        def on_entry_focus_in(event):
            event.widget.configure(highlightbackground=FG_GOLD, highlightthickness=2)
        
        def on_entry_focus_out(event):
            event.widget.configure(highlightbackground=BORDER_COLOR, highlightthickness=1)
        
        username_entry.bind('<FocusIn>', on_entry_focus_in)
        username_entry.bind('<FocusOut>', on_entry_focus_out)
        password_entry.bind('<FocusIn>', on_entry_focus_in)
        password_entry.bind('<FocusOut>', on_entry_focus_out)

    def _create_background_decoration(self, parent):
        for i in range(0, 1200, 100):
            for j in range(0, 800, 100):
                if (i + j) % 200 == 0:
                    dot = tk.Label(parent, text='•', font=('Tahoma', 10), 
                                 bg=BG_DARK, fg=SHADOW_COLOR)
                    dot.place(x=i, y=j)

    def _show_dashboard(self):
        self._clear()
        
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True)
        
        self._create_background_decoration(main_frame)
        
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', padx=30, pady=30)
        
        welcome_frame = ttk.Frame(header_frame, style='Main.TFrame')
        welcome_frame.pack(side='right')
        
        create_smart_label(welcome_frame, '🎓 سیستم مدیریت دانشگاه', 
                 bg=BG_DARK, fg=FG_GOLD).pack(side='right')
        ttk.Label(welcome_frame, text='University Management System', 
                 style='Subtitle.TLabel').pack(side='right', pady=(5, 0))
        
        logout_frame = ttk.Frame(header_frame, style='Main.TFrame')
        logout_frame.pack(side='left')
        tk.Button(logout_frame, text='🚪 خروج', 
                 font=('Tahoma', 12, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=15, pady=6,
                 command=self._show_login).pack()
        
        stats_frame = ttk.Frame(main_frame, style='Main.TFrame')
        stats_frame.pack(fill='x', padx=30, pady=20)
        
        student_card_container = ttk.Frame(stats_frame, style='Main.TFrame')
        student_card_container.pack(side='right', padx=15, expand=True, fill='both')
        
        student_card = tk.Frame(student_card_container, bg=CARD_BG, relief='flat', bd=0)
        student_card.pack(fill='both', expand=True, padx=5, pady=5)
        
        student_shadow = tk.Frame(student_card_container, bg=SHADOW_COLOR, relief='flat', bd=0)
        student_shadow.place(relx=0.5, rely=0.5, anchor='center', x=2, y=2)
        student_shadow.lower()
        
        student_content = ttk.Frame(student_card, style='Card.TFrame')
        student_content.pack(padx=20, pady=20)
        
        ttk.Label(student_content, text='👥', font=('Tahoma', 32), 
                 background=CARD_BG, foreground=FG_GOLD).pack()
        ttk.Label(student_content, text=f'{len(appuni.get_all_students())}', 
                 style='Title.TLabel').pack(pady=5)
        create_smart_label(student_content, 'دانشجو', 
                 bg=CARD_BG, fg=FG_GOLD).pack()
        
        teacher_card_container = ttk.Frame(stats_frame, style='Main.TFrame')
        teacher_card_container.pack(side='right', padx=15, expand=True, fill='both')
        
        teacher_card = tk.Frame(teacher_card_container, bg=CARD_BG, relief='flat', bd=0)
        teacher_card.pack(fill='both', expand=True, padx=5, pady=5)
        
        teacher_shadow = tk.Frame(teacher_card_container, bg=SHADOW_COLOR, relief='flat', bd=0)
        teacher_shadow.place(relx=0.5, rely=0.5, anchor='center', x=2, y=2)
        teacher_shadow.lower()
        
        teacher_content = ttk.Frame(teacher_card, style='Card.TFrame')
        teacher_content.pack(padx=20, pady=20)
        
        ttk.Label(teacher_content, text='👨‍🏫', font=('Tahoma', 32), 
                 background=CARD_BG, foreground=FG_GOLD).pack()
        ttk.Label(teacher_content, text=f'{len(appuni.get_all_teachers())}', 
                 style='Title.TLabel').pack(pady=5)
        create_smart_label(teacher_content, 'استاد', 
                 bg=CARD_BG, fg=FG_GOLD).pack()
        
        menu_frame = ttk.Frame(main_frame, style='Main.TFrame')
        menu_frame.pack(expand=True, padx=50, pady=40)
        
        create_smart_label(menu_frame, 'منوی اصلی', 
                 bg=BG_DARK, fg=FG_GOLD).pack(pady=(0, 30))
        
        menu_grid = ttk.Frame(menu_frame, style='Main.TFrame')
        menu_grid.pack()
        
        menu_buttons = [
            ('➕ ثبت دانشجو جدید', self._show_student_form, '🎓'),
            ('👨‍🏫 ثبت استاد جدید', self._show_teacher_form, '📚'),
            ('📚 مدیریت دانشجویان', self._show_students_management, '👥'),
            ('👨‍🏫 مدیریت اساتید', self._show_teachers_management, '👨‍🏫'),
            ('📊 ثبت نمرات', self._show_grades_management, '📝'),
            ('📈 گزارش‌گیری', self._show_reports, '📊')
        ]
        
        for i, (text, command, icon) in enumerate(menu_buttons):
            row = i // 2
            col = i % 2
            
            btn_container = ttk.Frame(menu_grid, style='Main.TFrame')
            btn_container.grid(row=row, column=col, padx=15, pady=15, sticky='ew')
            
            btn = tk.Button(btn_container, text=f'{icon} {text}', 
                           font=('Tahoma', 13, 'bold'), bg=BTN_BG, fg=BTN_FG,
                           relief='flat', bd=0, padx=20, pady=8,
                           command=command)
            btn.pack(fill='x', padx=5, pady=5)
            
            def on_enter(event, button=btn):
                button.configure(bg=BTN_BG_HOVER, fg=FG_WHITE)
            
            def on_leave(event, button=btn):
                button.configure(bg=BTN_BG, fg=BTN_FG)
            
            btn.bind('<Enter>', on_enter)
            btn.bind('<Leave>', on_leave)

    def _show_student_form(self, student_obj=None):
        self._clear()
        
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title = 'ویرایش دانشجو' if student_obj else 'ثبت دانشجو جدید'
        create_smart_label(header_frame, title, bg=BG_DARK, fg=FG_GOLD).pack(side='right')
        tk.Button(header_frame, text='بازگشت', 
                 font=('Tahoma', 12, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=15, pady=6,
                 command=self._show_dashboard).pack(side='left')
        
        form_card = ttk.Frame(main_frame, style='Card.TFrame')
        form_card.pack(expand=True, fill='both')
        
        fields_frame = ttk.Frame(form_card)
        fields_frame.pack(pady=30, padx=40)
        
        fields = [
            ('نام', 'name'),
            ('نام خانوادگی', 'family'),
            ('شماره تماس', 'phone'),
            ('کد دانشجویی', 'cod_student'),
            ('جنسیت', 'jensyt'),
            ('سن', 'age'),
            ('رشته', 'field')
        ]
        
        entries = {}
        
        for i, (label, key) in enumerate(fields):
            row = i // 2
            col = i % 2
            
            field_frame = ttk.Frame(fields_frame)
            field_frame.grid(row=row, column=col, padx=20, pady=10, sticky='ew')
            
            create_smart_label(field_frame, label+':', bg=CARD_BG, fg=FG_WHITE).pack(anchor='e')
            
            entry = create_smart_entry(field_frame, 
                           bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                           relief='flat', bd=5)
            entry.pack(fill='x', pady=5)
            
            if student_obj:
                if key == 'age':
                    entry.insert(0, str(getattr(student_obj, key)))
                else:
                    entry.insert(0, getattr(student_obj, key))
            
            entries[key] = entry
        
        def submit():
            try:
                values = {key: entry.get().strip() for key, entry in entries.items()}
                
                if not all(values.values()):
                    messagebox.showerror('خطا', 'همه فیلدها را پر کنید!')
                    return
                
                try:
                    age = int(values['age'])
                    if age <= 0:
                        raise ValueError()
                except ValueError:
                    messagebox.showerror('خطا', 'سن باید عدد مثبت باشد!')
                    return
                
                if student_obj:
                    student_obj._name = values['name']
                    student_obj._family = values['family']
                    student_obj._phone = values['phone']
                    student_obj.cod_student = values['cod_student']
                    student_obj._jensyt = values['jensyt']
                    student_obj._age = age
                    student_obj.field = values['field']
                    messagebox.showinfo('موفق', 'دانشجو با موفقیت ویرایش شد!')
                else:
                    appuni.add_student(
                        values['name'], values['family'], values['phone'],
                        values['cod_student'], values['jensyt'], age,
                        values['field']
                    )
                    messagebox.showinfo('موفق', 'دانشجو با موفقیت ثبت شد!')
                
                self._show_dashboard()
                
            except Exception as e:
                messagebox.showerror('خطا', f'خطا در ثبت دانشجو: {str(e)}')
        
        button_frame = ttk.Frame(form_card)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text='ثبت', 
                 font=('Tahoma', 18, 'bold'), bg=BTN_BG, fg=BTN_FG,
                 relief='flat', bd=0, padx=30, pady=12,
                 command=submit).pack(side='right', padx=10)
        tk.Button(button_frame, text='انصراف', 
                 font=('Tahoma', 16, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=20, pady=8,
                 command=self._show_dashboard).pack(side='right', padx=10)

    def _show_teacher_form(self, teacher_obj=None):
        self._clear()
        
        # Main container
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title = 'ویرایش استاد' if teacher_obj else 'ثبت استاد جدید'
        create_smart_label(header_frame, title, bg=BG_DARK, fg=FG_GOLD).pack(side='right')
        tk.Button(header_frame, text='بازگشت', 
                 font=('Tahoma', 16, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=20, pady=8,
                 command=self._show_dashboard).pack(side='left')
        
        # Form card
        form_card = ttk.Frame(main_frame, style='Card.TFrame')
        form_card.pack(expand=True, fill='both')
        
        # Form fields
        fields_frame = ttk.Frame(form_card)
        fields_frame.pack(pady=30, padx=40)
        
        # Field definitions
        fields = [
            ('نام', 'name'),
            ('نام خانوادگی', 'family'),
            ('شماره تماس', 'phone'),
            ('سن', 'age'),
            ('جنسیت', 'jensyt'),
            ('مدرک تحصیلی', 'edu'),
            ('سابقه کاری', 'history')
        ]
        
        entries = {}
        
        for i, (label, key) in enumerate(fields):
            row = i // 2
            col = i % 2
            
            field_frame = ttk.Frame(fields_frame)
            field_frame.grid(row=row, column=col, padx=20, pady=10, sticky='ew')
            
            create_smart_label(field_frame, label+':', bg=CARD_BG, fg=FG_WHITE).pack(anchor='e')
            
            entry = create_smart_entry(field_frame, 
                           bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                           relief='flat', bd=5)
            entry.pack(fill='x', pady=5)
            
            # Pre-fill if editing
            if teacher_obj:
                if key == 'age':
                    entry.insert(0, str(getattr(teacher_obj, key)))
                elif key == 'history':
                    entry.insert(0, ', '.join(getattr(teacher_obj, key)))
                else:
                    entry.insert(0, getattr(teacher_obj, key))
            
            entries[key] = entry
        
        # Submit button
        def submit():
            try:
                values = {key: entry.get().strip() for key, entry in entries.items()}
                
                # Validation
                if not all(values.values()):
                    messagebox.showerror('خطا', 'همه فیلدها را پر کنید!')
                    return
                
                try:
                    age = int(values['age'])
                    if age <= 0:
                        raise ValueError()
                except ValueError:
                    messagebox.showerror('خطا', 'سن باید عدد مثبت باشد!')
                    return
                
                history_list = [h.strip() for h in values['history'].split(',') if h.strip()]
                if teacher_obj:
                    # Update existing teacher
                    teacher_obj._name = values['name']
                    teacher_obj._family = values['family']
                    teacher_obj._phone = values['phone']
                    teacher_obj._age = age
                    teacher_obj._jensyt = values['jensyt']
                    teacher_obj._edu = values['edu']
                    teacher_obj._history = history_list
                    messagebox.showinfo('موفق', 'استاد با موفقیت ویرایش شد!')
                else:
                    # Create new teacher
                    appuni.add_teacher(
                        values['name'], values['family'], values['phone'],
                        values['jensyt'], age, values['edu'], ','.join(history_list)
                    )
                    messagebox.showinfo('موفق', 'استاد با موفقیت ثبت شد!')
                
                self._show_dashboard()
                
            except Exception as e:
                messagebox.showerror('خطا', f'خطا در ثبت استاد: {str(e)}')
        
        button_frame = ttk.Frame(form_card)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text='ثبت', 
                 font=('Tahoma', 18, 'bold'), bg=BTN_BG, fg=BTN_FG,
                 relief='flat', bd=0, padx=30, pady=12,
                 command=submit).pack(side='right', padx=10)
        tk.Button(button_frame, text='انصراف', 
                 font=('Tahoma', 16, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=20, pady=8,
                 command=self._show_dashboard).pack(side='right', padx=10)

    def _show_students_management(self):
        self._clear()
        
        # Main container
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        create_smart_label(header_frame, 'مدیریت دانشجویان', bg=BG_DARK, fg=FG_GOLD).pack(side='right')
        tk.Button(header_frame, text='بازگشت', 
                 font=('Tahoma', 16, 'bold'), bg=HIGHLIGHT_BG, fg=FG_WHITE,
                 relief='flat', bd=0, padx=20, pady=8,
                 command=self._show_dashboard).pack(side='left')
        
        # Search frame
        search_frame = ttk.Frame(main_frame, style='Card.TFrame')
        search_frame.pack(fill='x', pady=(0, 20))
        
        create_smart_label(search_frame, 'جستجو:', bg=CARD_BG, fg=FG_WHITE).pack(side='right', padx=10)
        search_entry = create_smart_entry(search_frame, 
                              bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                              relief='flat', bd=5)
        search_entry.pack(side='right', padx=10, fill='x', expand=True)
        
        # Students table
        table_frame = ttk.Frame(main_frame, style='Card.TFrame')
        table_frame.pack(fill='both', expand=True)
        
        columns = ('نام', 'نام خانوادگی', 'کد دانشجویی', 'رشته', 'سن', 'جنسیت', 'شماره تماس')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)
        
        # Populate data
        def refresh_table():
            tree.delete(*tree.get_children())
            for st in appuni.get_all_students():
                tree.insert('', 'end', values=(
                    st.name, st.family, st.cod_student, st.field, 
                    st.age, st.jensyt, st.phone
                ))
        
        refresh_table()
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons
        button_frame = ttk.Frame(main_frame, style='Main.TFrame')
        button_frame.pack(fill='x', pady=20)
        
        def edit_selected():
            try:
                selection = tree.selection()
                if not selection:
                    messagebox.showwarning('هشدار', 'لطفاً یک دانشجو انتخاب کنید!')
                    return
                item = tree.item(selection[0])
                student_code = str(item['values'][2]).strip()  # cod_student
                for st in appuni.get_all_students():
                    if str(st.cod_student).strip() == student_code:
                        self._show_student_form(st)
                        return
                messagebox.showerror('خطا', 'دانشجو یافت نشد!')
            except Exception as e:
                messagebox.showerror('خطا', f'خطای غیرمنتظره: {e}')
        
        def delete_selected():
            try:
                selection = tree.selection()
                if not selection:
                    messagebox.showwarning('هشدار', 'لطفاً یک دانشجو انتخاب کنید!')
                    return
                if messagebox.askyesno('تأیید', 'آیا از حذف این دانشجو اطمینان دارید؟'):
                    item = tree.item(selection[0])
                    student_code = str(item['values'][2]).strip()
                    for st in appuni.get_all_students():
                        if str(st.cod_student).strip() == student_code:
                            appuni.remove_student(st)
                            refresh_table()
                            messagebox.showinfo('موفق', 'دانشجو با موفقیت حذف شد!')
                            return
                    messagebox.showerror('خطا', 'دانشجو یافت نشد!')
            except Exception as e:
                messagebox.showerror('خطا', f'خطای غیرمنتظره: {e}')
        
        ttk.Button(button_frame, text='➕ دانشجو جدید', style='Primary.TButton',
                  command=self._show_student_form).pack(side='right', padx=5)
        ttk.Button(button_frame, text='✏️ ویرایش', style='Secondary.TButton',
                  command=edit_selected).pack(side='right', padx=5)
        ttk.Button(button_frame, text='🗑️ حذف', style='Secondary.TButton',
                  command=delete_selected).pack(side='right', padx=5)
        
        # Search functionality
        def search_students(*args):
            search_term = search_entry.get().lower()
            tree.delete(*tree.get_children())
            
            for st in appuni.get_all_students():
                if (search_term in st.name.lower() or 
                    search_term in st.family.lower() or 
                    search_term in st.cod_student.lower() or
                    search_term in st.field.lower()):
                    tree.insert('', 'end', values=(
                        st.name, st.family, st.cod_student, st.field, 
                        st.age, st.jensyt, st.phone
                    ))
        
        search_entry.bind('<KeyRelease>', search_students)

    def _show_teachers_management(self):
        self._clear()
        
        # Main container
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(header_frame, text='مدیریت اساتید', style='Title.TLabel').pack(side='right')
        ttk.Button(header_frame, text='بازگشت', style='Secondary.TButton',
                  command=self._show_dashboard).pack(side='left')
        
        # Search frame
        search_frame = ttk.Frame(main_frame, style='Card.TFrame')
        search_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(search_frame, text='جستجو:', style='Normal.TLabel').pack(side='right', padx=10)
        search_entry = tk.Entry(search_frame, font=('Arabic Typesetting', 12), 
                              bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                              relief='flat', bd=5)
        search_entry.pack(side='right', padx=10, fill='x', expand=True)
        
        # Teachers table
        table_frame = ttk.Frame(main_frame, style='Card.TFrame')
        table_frame.pack(fill='both', expand=True)
        
        columns = ('نام', 'نام خانوادگی', 'مدرک', 'سابقه', 'سن', 'جنسیت', 'شماره تماس')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)
        
        # Populate data
        def refresh_table():
            tree.delete(*tree.get_children())
            for t in appuni.get_all_teachers():
                tree.insert('', 'end', values=(
                    t.name, t.family, t.edu, ', '.join(t.history), 
                    t.age, t.jensyt, t.phone
                ))
        
        refresh_table()
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons
        button_frame = ttk.Frame(main_frame, style='Main.TFrame')
        button_frame.pack(fill='x', pady=20)
        
        def edit_selected():
            selection = tree.selection()
            if not selection:
                messagebox.showwarning('هشدار', 'لطفاً یک استاد انتخاب کنید!')
                return
            
            item = tree.item(selection[0])
            teacher_name = item['values'][0]  # name
            
            # Find teacher
            for t in appuni.get_all_teachers():
                if t.name == teacher_name:
                    self._show_teacher_form(t)
                    return
            
            messagebox.showerror('خطا', 'استاد یافت نشد!')
        
        def delete_selected():
            selection = tree.selection()
            if not selection:
                messagebox.showwarning('هشدار', 'لطفاً یک استاد انتخاب کنید!')
                return
            
            if messagebox.askyesno('تأیید', 'آیا از حذف این استاد اطمینان دارید؟'):
                item = tree.item(selection[0])
                teacher_name = item['values'][0]  # name
                
                # Find and remove teacher
                for t in appuni.get_all_teachers():
                    if t.name == teacher_name:
                        appuni.remove_teacher(t)
                        refresh_table()
                        messagebox.showinfo('موفق', 'استاد با موفقیت حذف شد!')
                        return
                
                messagebox.showerror('خطا', 'استاد یافت نشد!')
        
        ttk.Button(button_frame, text='➕ استاد جدید', style='Primary.TButton',
                  command=self._show_teacher_form).pack(side='right', padx=5)
        ttk.Button(button_frame, text='✏️ ویرایش', style='Secondary.TButton',
                  command=edit_selected).pack(side='right', padx=5)
        ttk.Button(button_frame, text='🗑️ حذف', style='Secondary.TButton',
                  command=delete_selected).pack(side='right', padx=5)
        
        # Search functionality
        def search_teachers(*args):
            search_term = search_entry.get().lower()
            tree.delete(*tree.get_children())
            
            for t in appuni.get_all_teachers():
                if (search_term in t.name.lower() or 
                    search_term in t.family.lower() or 
                    search_term in t.edu.lower()):
                    tree.insert('', 'end', values=(
                        t.name, t.family, t.edu, ', '.join(t.history), 
                        t.age, t.jensyt, t.phone
                    ))
        
        search_entry.bind('<KeyRelease>', search_teachers)

    def _show_grades_management(self):
        self._clear()
        
        # Main container
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(header_frame, text='مدیریت نمرات', style='Title.TLabel').pack(side='right')
        ttk.Button(header_frame, text='بازگشت', style='Secondary.TButton',
                  command=self._show_dashboard).pack(side='left')
        
        # Grade entry form
        form_card = ttk.Frame(main_frame, style='Card.TFrame')
        form_card.pack(fill='x', pady=(0, 20))
        
        form_frame = ttk.Frame(form_card)
        form_frame.pack(pady=20, padx=40)
        
        # Student selection
        ttk.Label(form_frame, text='کد دانشجویی:', style='Normal.TLabel').grid(row=0, column=1, sticky='e', padx=5, pady=5)
        student_entry = tk.Entry(form_frame, font=('Arabic Typesetting', 12), 
                               bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                               relief='flat', bd=5)
        student_entry.grid(row=0, column=0, padx=5, pady=5)
        
        # Grade entry
        ttk.Label(form_frame, text='نمره (0-20):', style='Normal.TLabel').grid(row=1, column=1, sticky='e', padx=5, pady=5)
        grade_entry = tk.Entry(form_frame, font=('Arabic Typesetting', 12), 
                             bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_GOLD,
                             relief='flat', bd=5)
        grade_entry.grid(row=1, column=0, padx=5, pady=5)
        
        # Submit button
        def submit_grade():
            try:
                student_code = student_entry.get().strip()
                grade_text = grade_entry.get().strip()
                
                if not student_code or not grade_text:
                    messagebox.showerror('خطا', 'همه فیلدها را پر کنید!')
                    return
                
                try:
                    grade = float(grade_text)
                    if not (0 <= grade <= 20):
                        raise ValueError()
                except ValueError:
                    messagebox.showerror('خطا', 'نمره باید بین 0 تا 20 باشد!')
                    return
                
                student_obj = None
                for st in appuni.get_all_students():
                    if st.cod_student == student_code:
                        student_obj = st
                        break
                
                if not student_obj:
                    messagebox.showerror('خطا', 'دانشجو یافت نشد!')
                    return
                
                # ثبت واقعی نمره (در اینجا فرض می‌کنیم هر دانشجو حداقل یک سکشن دارد)
                if hasattr(student_obj, 'sections') and student_obj.sections:
                    section = student_obj.sections[0]
                    appuni.set_grade(section, student_obj, grade)
                    messagebox.showinfo('موفق', f'نمره {grade} برای دانشجو {student_obj.name} {student_obj.family} ثبت شد!')
                else:
                    messagebox.showerror('خطا', 'سکشن برای این دانشجو یافت نشد!')
                
                # Clear form
                student_entry.delete(0, tk.END)
                grade_entry.delete(0, tk.END)
                
            except Exception as e:
                messagebox.showerror('خطا', f'خطا در ثبت نمره: {str(e)}')
        
        ttk.Button(form_frame, text='ثبت نمره', style='Primary.TButton',
                  command=submit_grade).grid(row=2, column=0, columnspan=2, pady=15)

    def _show_reports(self):
        self._clear()

        # Main container
        main_frame = ttk.Frame(self, style='Main.TFrame')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Header
        header_frame = ttk.Frame(main_frame, style='Main.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(header_frame, text='📊 گزارش‌گیری و آمار', style='Title.TLabel').pack(side='right')
        ttk.Button(header_frame, text='بازگشت', style='Secondary.TButton',
                  command=self._show_dashboard).pack(side='left')

        # Reports card (modern look)
        reports_card = ttk.Frame(main_frame, style='Card.TFrame')
        reports_card.pack(fill='both', expand=True, padx=10, pady=10)

        reports_frame = ttk.Frame(reports_card)
        reports_frame.pack(pady=30, padx=40, fill='x')

        # --- System Statistics ---
        ttk.Label(reports_frame, text='آمار کلی سیستم:', style='Header.TLabel').pack(anchor='e', pady=10)
        stats_text = f"""
        👥 تعداد کل دانشجویان: {len(appuni.get_all_students())}
        👨‍🏫 تعداد کل اساتید: {len(appuni.get_all_teachers())}
        🏫 تعداد کلاس‌ها: {len(appuni.get_all_classrooms()) if hasattr(appuni, 'get_all_classrooms') else 0}
        🏛️ نام دانشگاه: {appuni.university.name if hasattr(appuni, 'university') and hasattr(appuni.university, 'name') else 'نامشخص'}
        📍 مکان دانشگاه: {appuni.university.place if hasattr(appuni, 'university') and hasattr(appuni.university, 'place') else 'نامشخص'}
        """
        ttk.Label(reports_frame, text=stats_text, style='Normal.TLabel', 
                 justify='right').pack(anchor='e', pady=10)

        # --- Student Grades Table ---
        ttk.Label(reports_frame, text='جدول نمرات دانشجویان:', style='Header.TLabel').pack(anchor='e', pady=10)
        grades_table_frame = ttk.Frame(reports_frame, style='Card.TFrame')
        grades_table_frame.pack(fill='x', pady=10)

        columns = ('نام', 'نام خانوادگی', 'کد دانشجویی', 'رشته', 'میانگین نمرات', 'نمرات دروس')
        tree = ttk.Treeview(grades_table_frame, columns=columns, show='headings', height=8)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=140)

        # Populate table with student grades
        for st in appuni.get_all_students():
            grades_dict = st.get_grades() if hasattr(st, 'get_grades') else {}
            avg = st.average if hasattr(st, 'average') else 0.0
            grades_str = ', '.join([f"{d}: {g}" for d, g in grades_dict.items()]) if grades_dict else '---'
            tree.insert('', 'end', values=(
                st.name, st.family, st.cod_student, st.field, f"{avg:.2f}", grades_str
            ))

        # Scrollbar
        scrollbar = ttk.Scrollbar(grades_table_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side='left', fill='x', expand=True)
        scrollbar.pack(side='right', fill='y')

        # --- Recent Activities ---
        ttk.Label(reports_frame, text='فعالیت‌های اخیر:', style='Header.TLabel').pack(anchor='e', pady=10)
        if appuni.get_all_students():
            recent_students = appuni.get_all_students()[-3:] if len(appuni.get_all_students()) > 3 else appuni.get_all_students()
            recent_text = "دانشجویان اخیر:\n"
            for st in recent_students:
                recent_text += f"• {st.name} {st.family} ({st.field})\n"
        else:
            recent_text = "هیچ دانشجویی ثبت نشده است."
        ttk.Label(reports_frame, text=recent_text, style='Normal.TLabel',
                 justify='right').pack(anchor='e', pady=10)

if __name__ == '__main__':
    app = AppUniGUI()
    app.mainloop() 