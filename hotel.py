from tkinter import * # for gui
from PIL import Image, ImageTk # we need to install pillow to import PIL - pip install pillow  ## for setting images inside the gui

from customer import Customer_window

class HotelManagementSystem:

    def __init__(self, root):
        # doubt: what is the use of root?
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")

        # storing the folder path for the image folder
        image_folder_path = 'D:/Python/Projects/Hotel Management System/images'

        # ============================================ 1st image ============================================
        # image_1 file path
        image1 = Image.open(f'{image_folder_path}/hotel1.png')
        # resizing the image using Resampling.LANCZOS form Image lib
        image1 = image1.resize((1320, 140),Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img1 = ImageTk.PhotoImage(image1)
        # now using tkinter label we will show it in the window
        lblimg1 = Label(self.root, image=self.img1, bd=4, relief=RIDGE)
        lblimg1.place(x=230, y=0, width=1320, height=140)

        # ============================================ logo ============================================
        # logo image file path
        image2 = Image.open(f'{image_folder_path}/logohotel.png')
        # resizing the image using Resampling.LANCZOS form Image lib
        image2 = image2.resize((230, 140), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img2 = ImageTk.PhotoImage(image2)
        # now using tkinter label we will show it in the window
        lblimg2 = Label(self.root, image=self.img2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        # ============================================ heading ============================================
        lbltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=('times new roman', 40, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0,y=140, width=1550, height=50)

        # ============================================ main frame ============================================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=610)

        # ============================================ menu frame ============================================
        lbl_menu = Label(main_frame,text="MENU", font=('times new roman', 20, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ============================================ button frame ============================================
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(button_frame, text="Customer", width=20, command=self.customer_details, font=('times new roman', 14, 'bold'), bg='black', fg='gold', bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(button_frame, text="Room", width=20, font=('times new roman', 14, 'bold'), bg='black',
                          fg='gold', bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(button_frame, text="Details", width=20, font=('times new roman', 14, 'bold'), bg='black',
                          fg='gold', bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(button_frame, text="Report", width=20, font=('times new roman', 14, 'bold'), bg='black',
                          fg='gold', bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(button_frame, text="Logout", width=20, font=('times new roman', 14, 'bold'), bg='black',
                            fg='gold', bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ============================================ right side image ============================================
        # right side image file path
        image3 = Image.open(f'{image_folder_path}/slide3.jpg')
        # resizing the image using Resampling.LANCZOS form Image lib
        image3 = image3.resize((1310, 590), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img3 = ImageTk.PhotoImage(image3)
        # now using tkinter label we will show it in the window
        lblimg3 = Label(main_frame, image=self.img3, bd=4, relief=RIDGE)
        lblimg3.place(x=226, y=0, width=1310, height=590)

        # ============================================ left-bottom image1 ============================================
        # right side image file path
        image4 = Image.open(f'{image_folder_path}/food.jpg')
        # resizing the image using Resampling.LANCZOS form Image lib
        image4 = image4.resize((230, 200), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img4 = ImageTk.PhotoImage(image4)
        # now using tkinter label we will show it in the window
        lblimg4 = Label(main_frame, image=self.img4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=200)

        # ============================================ left-bottom image2 ============================================
        # right side image file path
        image5 = Image.open(f'{image_folder_path}/myh.jpg')
        # resizing the image using Resampling.LANCZOS form Image lib
        image5 = image5.resize((230, 190), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img5 = ImageTk.PhotoImage(image5)
        # now using tkinter label we will show it in the window
        lblimg5 = Label(main_frame, image=self.img5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=410, width=230, height=200)

    # creating a method for customer button
    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_window(self.new_window)


# doubt: why is main function used ?
if __name__ == '__main__':
    # creating the window object of Tkinter inside main function
    root = Tk()

    # creating object
    obj = HotelManagementSystem(root)

    # closing the mainloop
    root.mainloop()
