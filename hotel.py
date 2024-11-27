from tkinter import * # for gui
from PIL import Image, ImageTk # we need to install pillow to import PIL - pip install pillow  ## for setting images inside the gui

class HotelManagementSystem:

    def __init__(self, root):
        # doubt: what is the use of root?
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")

        # storing the folder path for the image folder
        image_folder_path = 'D:/Python/Projects/Hotel Management System/images'

        # ================================ 1st image ================================
        # image_1 file path
        image1 = Image.open(f'{image_folder_path}/hotel1.png')
        # resizing the image using Resampling.LANCZOS form Image lib
        image1 = image1.resize((1320, 140),Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img1 = ImageTk.PhotoImage(image1)
        # now using tkinter label we will show it in the window
        lblimg1 = Label(self.root, image=self.img1, bd=4, relief=RIDGE)
        lblimg1.place(x=230, y=0, width=1320, height=140)

        # ================================ logo ================================
        # logo image file path
        image2 = Image.open(f'{image_folder_path}/logohotel.png')
        # resizing the image using Resampling.LANCZOS form Image lib
        image2 = image2.resize((230, 140), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img2 = ImageTk.PhotoImage(image2)
        # now using tkinter label we will show it in the window
        lblimg2 = Label(self.root, image=self.img2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        # ================================ heading ================================
        lbltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=('times new roman', 40, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0,y=140, width=1550, height=50)

        # ================================ main frame ================================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=610)

# doubt: why is main function used ?
if __name__ == '__main__':
    # creating the window object of Tkinter inside main function
    root = Tk()

    # creating object
    obj = HotelManagementSystem(root)

    # closing the mainloop
    root.mainloop()
