# gui.py
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from database import Database  # Import the Database class
import os # Import os for path handling

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Student Management System")

        # Initialize the database connection
        self.db = Database()

        # ==================== Variable Declarations ====================
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

        # Call method to create GUI components
        self._create_widgets()
        # Initial data load
        self.fetch_data()

    def _create_widgets(self):
        """Creates and places all the GUI widgets."""

        # ==================== Tkinter Style ====================
        style = ttk.Style()
        style.theme_use('clam') # Changed from 'default' to 'clam' for better styling on macOS
        style.configure('Blue.TButton', background='blue', foreground='white', font=("times new roman", 12, "bold"))
        style.configure('Treeview.Heading', font=("times new roman", 13, "bold")) # Style for Treeview headers
        style.configure('Treeview', font=("times new roman", 12)) # Style for Treeview rows

        # ==================== Header Images ====================
        # Define base path for images
        image_base_path = "/Users/luckyjaglan/Documents/Projects/Student_Database_Management_System/Management_Images/"

        # 1st image (srm1.png)
        img1_path = os.path.join(image_base_path, "srm1.png")
        img1 = Image.open(img1_path)
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=540, height=160)

        # 2nd image (images_(1)-dszdYhTtd-transformed.jpeg)
        img2_path = os.path.join(image_base_path, "images_(1)-dszdYhTtd-transformed.jpeg")
        img2 = Image.open(img2_path)
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=540, y=0, width=540, height=160)

        # 3rd image (mainbuilding.jpeg)
        img3_path = os.path.join(image_base_path, "mainbuilding.jpeg")
        img3 = Image.open(img3_path)
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=1080, y=0, width=540, height=160) # Adjusted x-coordinate for a 1920 width window

        # ==================== Background Image ====================
        bg_img_path = os.path.join(image_base_path, "bg.png")
        bg_img = Image.open(bg_img_path)
        bg_img = bg_img.resize((1530, 710), Image.LANCZOS) # Ensure this matches your root geometry
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        lbl_bg = Label(self.root, image=self.photobg_img)
        lbl_bg.place(x=0, y=160, width=1530, height=710) # Adjusted y-coordinate to be below header

        # ==================== Title Label ====================
        lbl_title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="red", fg="white")
        lbl_title.place(x=0, y=160, width=1530, height=50) # Placed over background image

        # ==================== Main Frame ====================
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=10, y=215, width=1500, height=650) # Adjusted size and position

        # ==================== Left Frame (Student Information) ====================
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"), bg="white", fg="red")
        left_frame.place(x=10, y=10, width=650, height=630)

        # Current Course Information
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"), bg="white", fg="red")
        current_course_frame.place(x=5, y=5, width=630, height=150)

        # Department
        lbl_dep = Label(current_course_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        combo_dep = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12), width=18, state="readonly")
        combo_dep["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Course
        lbl_course = Label(current_course_frame, text="Course:", font=("times new roman", 12, "bold"), bg="white")
        lbl_course.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        combo_course = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12), width=18, state="readonly")
        combo_course["values"] = ("Select Course", "BCA", "B.Tech", "MCA", "M.Tech")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Year
        lbl_year = Label(current_course_frame, text="Year:", font=("times new roman", 12, "bold"), bg="white")
        lbl_year.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        combo_year = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12), width=18, state="readonly")
        combo_year["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        combo_year.current(0)
        combo_year.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Semester
        lbl_sem = Label(current_course_frame, text="Semester:", font=("times new roman", 12, "bold"), bg="white")
        lbl_sem.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        combo_sem = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12), width=18, state="readonly")
        combo_sem["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        combo_sem.current(0)
        combo_sem.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Student Class Information
        student_class_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Student Class Information", font=("times new roman", 12, "bold"), bg="white", fg="red")
        student_class_frame.place(x=5, y=160, width=630, height=300)

        # Student ID
        lbl_stu_id = Label(student_class_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        lbl_stu_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        txt_stu_id = ttk.Entry(student_class_frame, textvariable=self.var_stu_ID, font=("times new roman", 12), width=20)
        txt_stu_id.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        # Name
        lbl_name = Label(student_class_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        txt_name = ttk.Entry(student_class_frame, textvariable=self.var_name, font=("times new roman", 12), width=20)
        txt_name.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        # Section
        lbl_sec = Label(student_class_frame, text="Section:", font=("times new roman", 12, "bold"), bg="white")
        lbl_sec.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        txt_sec = ttk.Entry(student_class_frame, textvariable=self.var_sec, font=("times new roman", 12), width=20)
        txt_sec.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Age
        lbl_age = Label(student_class_frame, text="Age:", font=("times new roman", 12, "bold"), bg="white")
        lbl_age.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        txt_age = ttk.Entry(student_class_frame, textvariable=self.var_age, font=("times new roman", 12), width=20)
        txt_age.grid(row=1, column=3, padx=2, pady=5, sticky=W)

        # Gender
        lbl_gen = Label(student_class_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        lbl_gen.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        combo_gen = ttk.Combobox(student_class_frame, textvariable=self.var_gen, font=("times new roman", 12), width=18, state="readonly")
        combo_gen["values"] = ("Select Gender", "Male", "Female", "Other")
        combo_gen.current(0)
        combo_gen.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # Phone No.
        lbl_pno = Label(student_class_frame, text="Phone NO.:", font=("times new roman", 12, "bold"), bg="white")
        lbl_pno.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        txt_pno = ttk.Entry(student_class_frame, textvariable=self.var_pno, font=("times new roman", 12), width=20)
        txt_pno.grid(row=2, column=3, padx=2, pady=5, sticky=W)

        # Email
        lbl_email = Label(student_class_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        txt_email = ttk.Entry(student_class_frame, textvariable=self.var_email, font=("times new roman", 12), width=20)
        txt_email.grid(row=3, column=1, padx=2, pady=5, sticky=W)

        # Bus No.
        lbl_bus = Label(student_class_frame, text="Bus NO.:", font=("times new roman", 12, "bold"), bg="white")
        lbl_bus.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        txt_bus = ttk.Entry(student_class_frame, textvariable=self.var_bus, font=("times new roman", 12), width=20)
        txt_bus.grid(row=3, column=3, padx=2, pady=5, sticky=W)

        # ==================== Button Frame (Operations) ====================
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=470, width=630, height=100)

        btn_add = ttk.Button(btn_frame, text="Save", command=self.add_data, width=22, style='Blue.TButton', cursor="hand2")
        btn_add.grid(row=0, column=0, padx=5, pady=10)

        btn_update = ttk.Button(btn_frame, text="Update", command=self.update_data, width=22, style='Blue.TButton', cursor="hand2")
        btn_update.grid(row=0, column=1, padx=5, pady=10)

        btn_delete = ttk.Button(btn_frame, text="Delete", command=self.delete_data, width=22, style='Blue.TButton', cursor="hand2")
        btn_delete.grid(row=1, column=0, padx=5, pady=10)

        btn_reset = ttk.Button(btn_frame, text="Reset", command=self.reset_data, width=22, style='Blue.TButton', cursor="hand2")
        btn_reset.grid(row=1, column=1, padx=5, pady=10)

        # ==================== Right Frame (Student Details) ====================
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"), bg="white", fg="red")
        right_frame.place(x=670, y=10, width=810, height=630)

        # Image for the right frame (assuming this is the "5th image")
        # Ensure 'images.jpeg' exists in your Management Images folder
        right_panel_img_path = os.path.join(image_base_path, "images.jpeg")
        try:
            img_right_panel = Image.open(right_panel_img_path)
            img_right_panel = img_right_panel.resize((790, 200), Image.LANCZOS) # Adjust size to fit frame
            self.photo_right_panel = ImageTk.PhotoImage(img_right_panel)
            lbl_right_panel_img = Label(right_frame, image=self.photo_right_panel, bg="white")
            lbl_right_panel_img.place(x=5, y=5, width=790, height=200) # Placed at the top of the right frame
        except FileNotFoundError:
            messagebox.showwarning("Image Warning", f"Could not find {right_panel_img_path}. Please ensure it exists.", parent=self.root)
        except Exception as e:
            messagebox.showwarning("Image Error", f"Error loading image {right_panel_img_path}: {e}", parent=self.root)


        # Search System Frame
        searchframe = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search Student Information", font=("times new roman", 12, "bold"), bg="white", fg="red")
        searchframe.place(x=5, y=210, width=790, height=70) # Adjusted y-coordinate to be below the new image

        lbl_search_by = Label(searchframe, text="Search by:", font=("times new roman", 12, "bold"), bg="white")
        lbl_search_by.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        combo_search = ttk.Combobox(searchframe, textvariable=self.var_com_search, font=("times new roman", 12), width=18, state="readonly")
        combo_search["values"] = ("Select Attribute", "Student_ID", "Name", "Department", "Course")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        txt_search = ttk.Entry(searchframe, textvariable=self.var_search, font=("times new roman", 12), width=20)
        txt_search.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        btn_search = ttk.Button(searchframe, text="Search", command=self.search_data, width=18, style='Blue.TButton', cursor="hand2")
        btn_search.grid(row=0, column=3, padx=5, pady=5)

        btn_showall = ttk.Button(searchframe, text="Show all", command=self.fetch_data, width=18, style='Blue.TButton', cursor="hand2")
        btn_showall.grid(row=0, column=4, padx=5, pady=5)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=285, width=790, height=330) # Adjusted y-coordinate

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "sec", "age", "gen", "pno", "email", "bus"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("pno", text="Phone No.")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("bus", text="Bus No.")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("age", width=100)
        self.student_table.column("gen", width=100)
        self.student_table.column("pno", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("bus", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)


    # ==================== Data Operations Methods ====================

    def add_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or
            self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or
            self.var_stu_ID.get() == "" or self.var_name.get() == "" or
            self.var_sec.get() == "" or self.var_age.get() == "" or
            self.var_gen.get() == "Select Gender" or self.var_pno.get() == "" or
            self.var_email.get() == "" or self.var_bus.get() == ""):
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return

        try:
            data_tuple = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_stu_ID.get(),
                self.var_name.get(),
                self.var_sec.get(),
                self.var_age.get(),
                self.var_gen.get(),
                self.var_pno.get(),
                self.var_email.get(),
                self.var_bus.get()
            )
            self.db.add_student(data_tuple)
            messagebox.showinfo("Success", "Student data added successfully.", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to add data: {str(ex)}", parent=self.root)

    def fetch_data(self):
        try:
            records = self.db.fetch_all_students()
            self.student_table.delete(*self.student_table.get_children())
            for row in records:
                self.student_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to fetch data: {str(ex)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]

        if row: # Ensure a row is selected
            self.var_dep.set(row[0])
            self.var_course.set(row[1])
            self.var_year.set(row[2])
            self.var_sem.set(row[3])
            self.var_stu_ID.set(row[4])
            self.var_name.set(row[5])
            self.var_sec.set(row[6])
            self.var_age.set(row[7])
            self.var_gen.set(row[8])
            self.var_pno.set(row[9])
            self.var_email.set(row[10])
            self.var_bus.set(row[11])

    def update_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or
            self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or
            self.var_stu_ID.get() == "" or self.var_name.get() == "" or
            self.var_sec.get() == "" or self.var_age.get() == "" or
            self.var_gen.get() == "Select Gender" or self.var_pno.get() == "" or
            self.var_email.get() == "" or self.var_bus.get() == ""):
            messagebox.showerror("Error", "All fields are required for update.", parent=self.root)
            return

        try:
            data_tuple = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_name.get(),
                self.var_sec.get(),
                self.var_age.get(),
                self.var_gen.get(),
                self.var_pno.get(),
                self.var_email.get(),
                self.var_bus.get(),
                self.var_stu_ID.get() # Student ID for WHERE clause
            )
            self.db.update_student(data_tuple)
            messagebox.showinfo("Success", "Student data updated successfully.", parent=self.root)
            self.fetch_data()
            self.reset_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to update: {str(ex)}", parent=self.root)

    def delete_data(self):
        if self.var_stu_ID.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete a record.", parent=self.root)
            return
        
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student record?", parent=self.root)
        if confirm:
            try:
                self.db.delete_student(self.var_stu_ID.get())
                messagebox.showinfo("Success", "Student data deleted successfully.", parent=self.root)
                self.reset_data()
                self.fetch_data()
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to delete: {str(ex)}", parent=self.root)

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
        search_by = self.var_com_search.get()
        search_term = self.var_search.get()

        if search_by == "Select Attribute" or search_term == "":
            messagebox.showerror("Error", "Please select a search attribute and enter a search term.", parent=self.root)
            return
        
        try:
            records = self.db.search_student(search_by, search_term)
            self.student_table.delete(*self.student_table.get_children())
            if records:
                for row in records:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Not Found", "No records match your search.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to search data: {str(ex)}", parent=self.root)