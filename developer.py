from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        img_top = Image.open(r"college_images\img14.jpeg")  # Insert Image inside ""
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # ********Frame**********************
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=620)

        img_top1 = Image.open(r"college_images\img14.jpeg")  # Insert Image inside ""
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=80, y=10, width=200, height=200)

        # Developer info
        dev_label = Label(main_frame, text="Mansi Kanwar", font=("times new roman", 20, "bold"))
        dev_label.place(x=85, y=215)

        dev_label = Label(main_frame, text="19ESKIT054", font=("times new roman", 20, "bold"))
        dev_label.place(x=90, y=255)

        img_top2 = Image.open(r"college_images\img14.jpeg")  # Insert Image inside ""
        img_top2 = img_top2.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=80, y=310, width=200, height=200)

        dev_labe2 = Label(main_frame, text="Manasvini Sharma", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=80, y=520)

        dev_labe2 = Label(main_frame, text="19ESKIT053", font=("times new roman", 20, "bold"))
        dev_labe2.place(x=90, y=560)

        img_top3 = Image.open(r"college_images\img14.jpeg")
        img_top3 = img_top3.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()