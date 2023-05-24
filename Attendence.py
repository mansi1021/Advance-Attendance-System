from tkinter import *
from tkinter import ttk, Frame
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.title("face Recognition System")


        # FIRST image
        img1 = Image.open(r"college_images\img19.jpeg")
        img1 = img1.resize((680,250),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0,y=0,width=680,height=250)

        # second image
        img2 = Image.open(r"college_images\img20.jpeg")
        img2 = img2.resize((680,250),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=680,y=0,width=680,height=250)

        #bg - image
        # third image
        img3 = Image.open(r"college_images\img15.jpeg")
        img3 = img3.resize((1920,500),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=180,width=1920,height=510)

        title_lbl = Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1420,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=0,y=45,width=1620,height=510)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence details",font=("times new roman",10,"bold"))
        Left_frame.place(x=15,y=5,width=650,height=450)

        left_inner_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white",)
        left_inner_frame.place(x=5,y=10,width=635,height=430)

        # attendence id
        attendenceId_label = Label(left_inner_frame,text="Attendence Id:",font=("times new roman",10,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceId_entry=ttk.Entry(left_inner_frame,width=20,font=("times new roman",10,"bold"))
        attendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Roll no
        roll_no_label = Label(left_inner_frame,text="Roll No.:",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(left_inner_frame,width=20,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        name_label = Label(left_inner_frame,text="Student Name:",font=("times new roman",10,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inner_frame,width=20,font=("times new roman",10,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        dep_label = Label(left_inner_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=5,sticky=W)

        dep_combo=ttk.Combobox(left_inner_frame,font=("times new roman",10,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Time
        time_label = Label(left_inner_frame,text="Time:",font=("times new roman",10,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inner_frame,width=20,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date
        date_label = Label(left_inner_frame,text="Date:",font=("times new roman",10,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inner_frame,width=20,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendence status
        attendenceStatus_label = Label(left_inner_frame,text="Attendence Status:",font=("times new roman",10,"bold"),bg="white")
        attendenceStatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendenceStatus_combo=ttk.Combobox(left_inner_frame,font=("times new roman",10,"bold"),state="readonly",width=18)
        attendenceStatus_combo["values"]=("Status","Present","Absent")
        attendenceStatus_combo.current(0)
        attendenceStatus_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # buttons frame
        btn_frame = Frame(left_inner_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=30,y=340,width=520,height=30)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv ,width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv , width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        # ********Right label frame*********
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence",font=("times new roman",10,"bold"))
        Right_frame.place(x=690,y=5,width=650,height=450)

        Table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=5,width=635,height=430)

        # Scroll bar table
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(Table_frame, columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll no")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence Status")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        # =========================== FETCH DATA =============================

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

        # =========================== Import CSV =============================

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root )
        # print(mydata)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            # print(csvread)
            for i in csvread:
                # print(i)
                mydata.append(i)
            # print(mydata)
            self.fetchData(mydata)
            # print(mydata)    

        # =========================== Export CSV =============================

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root )
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    # exp_write.append(i)
                messagebox.showinfo("Data Export","Your Data is Exported to "+ os.path.basename(fln)+" successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj = Attendence(root)
    root.mainloop()