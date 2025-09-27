from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from database import queries


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Student Management System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stu_ID = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_age = StringVar()
        self.var_gen = StringVar()
        self.var_pno = StringVar()
        self.var_email = StringVar()
        self.var_bus = StringVar()
        self.var_com_search = StringVar()
        self.var_search = StringVar()

        # ================== Top Images ==================
        img = Image.open("assets/srm1.png")
        img = img.resize((540, 160), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        Button(self.root, image=self.photo, cursor="hand2").place(x=0, y=0, width=520, height=160)

        img_2 = Image.open("assets/images_(1).jpeg")
        img_2 = img_2.resize((540, 160), Image.LANCZOS)
        self.photo_2 = ImageTk.PhotoImage(img_2)
        Button(self.root, image=self.photo_2, cursor="hand2").place(x=521, y=0, width=520, height=160)

        img_3 = Image.open("assets/images_(1).jpeg")
        img_3 = img_3.resize((540, 160), Image.LANCZOS)
        self.photo_3 = ImageTk.PhotoImage(img_3)
        Button(self.root, image=self.photo_3, cursor="hand2").place(x=1041, y=0, width=500, height=160)

        # Background
        img_bg = Image.open("assets/images.png")
        img_bg = img_bg.resize((1550, 1000), Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root, image=self.photo_bg, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=160, width=1550, height=1000)

        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 24, "bold"), fg="white", bg="red")
        lbl_title.place(x=0, y=0, width=1520, height=60)

        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=13, y=60, width=1500, height=550)

        # ================== Left Frame ==================
        dataleftframe = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2,
                                   text="Student Information",
                                   font=("times new roman", 20, "bold"),
                                   fg="green", bg="white")
        dataleftframe.place(x=10, y=10, width=550, height=525)

        # Current Course Frame
        std_lbl_info_frame = LabelFrame(dataleftframe, bd=4, relief=RIDGE, padx=2,
                                        text="Current Course Information",
                                        font=("times new roman", 14, "bold"),
                                        fg="blue", bg="white")
        std_lbl_info_frame.place(x=0, y=0, width=540, height=120)

        # Department
        Label(std_lbl_info_frame, text="Department:",
              font=("times new roman", 14, "bold"), bg="white").grid(row=0, column=0, padx=1, sticky=W)
        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep,
                                 font=("times new roman", 14, "bold"), width=15, state="readonly")
        combo_dep["value"] = ("Select Department", "Engineering", "Law", "Humanities",
                              "Hotel Management", "Finance", "Bioscience", "Computer Application")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=1, pady=4, sticky=W)

        # Course
        Label(std_lbl_info_frame, text="Courses:",
              font=("times new roman", 14, "bold"), bg="white").grid(row=0, column=2, padx=1, sticky=W)
        combo_course = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course,
                                    font=("times new roman", 14, "bold"), width=13, state="readonly")
        combo_course["value"] = ("Select Course", "Btech", "LLB", "BA", "MA",
                                 "Bcom", "Bioengineering", "BCA", "MCA", "BHM", "BBA")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=1, pady=3, sticky=W)

        # Year
        Label(std_lbl_info_frame, text="Year:",
              font=("times new roman", 14, "bold"), bg="white").grid(row=1, column=0, padx=1, sticky=W)
        combo_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year,
                                  font=("times new roman", 14, "bold"), width=15, state="readonly")
        combo_year["value"] = ("Select Year", "1st", "2nd", "3rd", "4th", "5th", "6th")
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=1, pady=4, sticky=W)

        # Semester
        Label(std_lbl_info_frame, text="Semester:",
              font=("times new roman", 14, "bold"), bg="white").grid(row=1, column=2, padx=1, sticky=W)
        combo_sem = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_sem,
                                 font=("times new roman", 14, "bold"), width=13, state="readonly")
        combo_sem["value"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th",
                              "6th", "7th", "8th", "9th", "10th", "11th", "12th")
        combo_sem.current(0)
        combo_sem.grid(row=1, column=3, padx=1, pady=3, sticky=W)

        # ================== Student Info Frame ==================
        stu_info = LabelFrame(dataleftframe, bd=4, relief=RIDGE, padx=2,
                              text="Student Details",
                              font=("times new roman", 14, "bold"),
                              fg="blue", bg="white")
        stu_info.place(x=0, y=121, width=540, height=200)

        # ID
        Label(stu_info, text="StudentID:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=0, column=0, padx=1, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_stu_ID,
                  font=("times new roman", 14, "bold"), width=17).grid(row=0, column=1, padx=1, sticky=W)

        # Name
        Label(stu_info, text="Name:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=0, column=2, padx=1, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_name,
                  font=("times new roman", 14, "bold"), width=14).grid(row=0, column=3, padx=1, sticky=W)

        # Section
        Label(stu_info, text="Section:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=1, column=0, padx=1, pady=10, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_sec,
                  font=("times new roman", 14, "bold"), width=17).grid(row=1, column=1, padx=1, pady=10, sticky=W)

        # Age
        Label(stu_info, text="Age:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=1, column=2, padx=1, pady=10, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_age,
                  font=("times new roman", 14, "bold"), width=14).grid(row=1, column=3, padx=1, pady=10, sticky=W)

        # Gender
        Label(stu_info, text="Gender:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=2, column=0, padx=1, pady=10, sticky=W)
        combo_gen = ttk.Combobox(stu_info, textvariable=self.var_gen,
                                 font=("times new roman", 14, "bold"), width=15, state="readonly")
        combo_gen["value"] = ("Select Gender", "Male", "Female")
        combo_gen.current(0)
        combo_gen.grid(row=2, column=1, padx=1, pady=10, sticky=W)

        # Phone
        Label(stu_info, text="Phone NO.:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=2, column=2, padx=1, pady=10, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_pno,
                  font=("times new roman", 14, "bold"), width=14).grid(row=2, column=3, padx=1, pady=10, sticky=W)

        # Email
        Label(stu_info, text="Email:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=3, column=0, padx=1, pady=10, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_email,
                  font=("times new roman", 14, "bold"), width=17).grid(row=3, column=1, padx=1, pady=10, sticky=W)

        # Bus
        Label(stu_info, text="Bus NO.:", font=("times new roman", 14, "bold"),
              bg="white").grid(row=3, column=2, padx=1, pady=10, sticky=W)
        ttk.Entry(stu_info, textvariable=self.var_bus,
                  font=("times new roman", 14, "bold"), width=14).grid(row=3, column=3, padx=1, pady=10, sticky=W)

        # ================== Button Frame ==================
        btn_frame = Frame(dataleftframe, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=321, width=538, height=163)
        heading = LabelFrame(btn_frame, bd=4, relief=RIDGE, padx=2,
                             text="Operations", font=("times new roman", 14, "bold"),
                             fg="blue", bg="white")
        heading.place(x=0, y=0, width=538, height=163)

        Button(btn_frame, text="Save", command=self.add_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=22, height=2, cursor="hand2").grid(row=0, column=0, padx=5, pady=20)

        Button(btn_frame, text="Update", command=self.update_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=22, height=2, cursor="hand2").grid(row=0, column=1, padx=5, pady=20)

        Button(btn_frame, text="Delete", command=self.delete_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=22, height=2, cursor="hand2").grid(row=1, column=0, padx=8, pady=5)

        Button(btn_frame, text="Reset", command=self.reset_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=22, height=2, cursor="hand2").grid(row=1, column=1, padx=8, pady=5)

        # ================== Right Frame ==================
        datarightframe = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2,
                                    text="Student Details",
                                    font=("times new roman", 20, "bold"),
                                    fg="green", bg="white")
        datarightframe.place(x=570, y=10, width=915, height=525)

        # Image
        img_1 = Image.open("assets/images.jpeg")
        img_1 = img_1.resize((900, 150), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        Label(datarightframe, image=self.photoimg_1, bd=2, relief=RIDGE).place(x=0, y=0, width=900, height=150)

        # Search Frame
        searchframe = LabelFrame(datarightframe, bd=4, relief=RIDGE, padx=2,
                                 text="Search Student Information",
                                 font=("times new roman", 20, "bold"),
                                 fg="green", bg="white")
        searchframe.place(x=0, y=150, width=900, height=75)

        Label(searchframe, text="Search by:",
              font=("times new roman", 14, "bold"), fg="red", bg="white").grid(row=0, column=0, padx=1, sticky=W)

        combo_search = ttk.Combobox(searchframe, textvariable=self.var_com_search,
                                    font=("times new roman", 14, "bold"), width=15, state="readonly")
        combo_search["value"] = ("Select Attribute", "Student_ID", "Phone", "Email")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=1, sticky=W)

        ttk.Entry(searchframe, textvariable=self.var_search,
                  font=("times new roman", 14, "bold"), width=14).grid(row=0, column=2, padx=10, sticky=W)

        Button(searchframe, text="Search", command=self.search_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=18, cursor="hand2").grid(row=0, column=3, padx=10, sticky=W)

        Button(searchframe, text="Show All", command=self.fetch_data,
               font=("times new roman", 14, "bold"), fg="white", bg="blue",
               width=18, cursor="hand2").grid(row=0, column=4, padx=8, sticky=W)

        # ================== Student Table ==================
        table_frame = Frame(datarightframe, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=225, width=900, height=260)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          column=("v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headings
        headings = ["Department", "Course", "Year", "Semester", "StudentID",
                    "Name", "Section", "Age", "Gender", "Phone", "Email", "Bus"]
        for i, head in enumerate(headings):
            self.student_table.heading(chr(118+i), text=head)
            self.student_table.column(chr(118+i), width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # ================== Functions ==================
    def add_data(self):
        if (self.var_dep.get() == "" or self.var_course.get() == "" or
            self.var_year.get() == "" or self.var_sem.get() == "" or
            self.var_stu_ID.get() == "" or self.var_name.get() == ""):
            messagebox.showerror("ERROR", "All fields are required!", parent=self.root)
            return
        data = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(),
                self.var_stu_ID.get(), self.var_name.get(), self.var_sec.get(), self.var_age.get(),
                self.var_gen.get(), self.var_pno.get(), self.var_email.get(), self.var_bus.get())
        queries.insert_student(data)
        self.fetch_data()
        messagebox.showinfo("Success", "Student added successfully!", parent=self.root)

    def fetch_data(self):
        rows = queries.fetch_students()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_sem.set(data[3])
            self.var_stu_ID.set(data[4])
            self.var_name.set(data[5])
            self.var_sec.set(data[6])
            self.var_age.set(data[7])
            self.var_gen.set(data[8])
            self.var_pno.set(data[9])
            self.var_email.set(data[10])
            self.var_bus.set(data[11])

    def update_data(self):
        if self.var_stu_ID.get() == "":
            messagebox.showerror("ERROR", "Select a record to update!", parent=self.root)
            return
        data = (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(),
                self.var_name.get(), self.var_sec.get(), self.var_age.get(), self.var_gen.get(),
                self.var_pno.get(), self.var_email.get(), self.var_bus.get(), self.var_stu_ID.get())
        queries.update_student(data)
        self.fetch_data()
        messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)

    def delete_data(self):
        if self.var_stu_ID.get() == "":
            messagebox.showerror("ERROR", "Select a record to delete!", parent=self.root)
            return
        queries.delete_student(self.var_stu_ID.get())
        self.fetch_data()
        messagebox.showinfo("Success", "Record deleted successfully!", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_ID.set("")
        self.var_name.set("")
        self.var_sec.set("")
        self.var_age.set("")
        self.var_gen.set("Select Gender")
        self.var_pno.set("")
        self.var_email.set("")
        self.var_bus.set("")

    def search_data(self):
        if self.var_com_search.get() == "Select Attribute" or self.var_search.get() == "":
            messagebox.showerror("ERROR", "Please select an option and enter a value", parent=self.root)
            return
        rows = queries.search_students(self.var_com_search.get(), self.var_search.get())
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
