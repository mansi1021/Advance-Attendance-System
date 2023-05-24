from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white", fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\img13.jpeg") #Insert Image inside ""
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label = Label(f_lbl, text="Email 1 : mansisgh19@gmail.com", font=("times new roman", 20, "bold"))
        dev_label.place(x=80,y=530)

        
   

        dev_label2 = Label(f_lbl, text="Email 2 : smanasvini23@gmail.com", font=("times new roman", 20, "bold"))
        dev_label2.place(x=80,y=560)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
