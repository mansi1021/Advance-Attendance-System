from tkinter import *
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
from register import Register
import os 
from train import Train
from Face_Recognition import Face_Recognition
from Attendence import Attendence
from developer import Developer
from help import Help

class Face_Recognition_System:

    # ************************Functions Buttons************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are You sure exit this project",parent = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return 
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")  #title of page

        img = Image.open(r"college_images\img1.jpeg")
        img = img.resize((480,250),Image.ANTIALIAS) # resize(width,height)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=440,height=200)

        # second image
        img1 = Image.open(r"college_images\img3.jpeg")
        img1 = img1.resize((480,250),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=440,y=0,width=460,height=200)

        # third image
        img2 = Image.open(r"college_images\img4.jpeg")
        img2 = img2.resize((480,250),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=900,y=0,width=460,height=200)


        # fourth image
        img3 = Image.open(r"college_images\img5.jpeg")
        img3 = img3.resize((480,250),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x=1440,y=0,width=480,height=250)

        #bg - image
        img4 = Image.open(r"college_images\img15.jpeg")
        img4 = img4.resize((1920,800),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0,y=200,width=1920,height=800)

        #Title 
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20,"bold"),bg="white",fg="red")
        title_lbl.place(x=5 ,y=0,width=1340,height=35)

        # student button
        img5 = Image.open(r"college_images\img11.jpeg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=50,y=60,width=220,height=220)

        b2=Button(bg_img,text="Register Here",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=50,y=240,width=220,height=40)


        # detect face button
        img6 = Image.open(r"college_images\img10.jpeg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=380,y=60,width=220,height=220)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=380,y=240,width=220,height=40)

         # attendance button
        img7 = Image.open(r"college_images\img12.jpeg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=60,width=220,height=220)

        b2=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=240,width=220,height=40)

        # help desk
        img8 = Image.open(r"college_images\img13.jpeg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1040,y=60,width=220,height=220)

        b2=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1040,y=240,width=220,height=40)

        # Train face button
        img9 = Image.open(r"college_images\img6.jpeg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=50,y=300,width=220,height=180)

        b2=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=50,y=450,width=220,height=40)

         # Images Data button
        img10 = Image.open(r"college_images\img17.jpeg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2", command=self.open_img)
        b1.place(x=380,y=300,width=220,height=180)

        b2=Button(bg_img,text="Photos data",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=380,y=450,width=220,height=40)

        # Developer button
        img11 = Image.open(r"college_images\img18.jpeg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=220,height=180)

        b2=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",25,"bold"),bg="darkblue",fg="white")
        b2.place(x=700,y=450,width=220,height=40)

        # exit button
        img12 = Image.open(r"college_images\img16.jpeg")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2", command=self.iExit)
        b1.place(x=1040,y=300,width=220,height=220)

        b2=Button(bg_img,text="Exit",cursor="hand2", command=self.iExit,font=("times new roman",25,"bold"),bg="darkblue",fg="white")
        b2.place(x=1040,y=450,width=220,height=40)

    # **********
    def open_img(self):
        os.startfile("data")
        

if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
