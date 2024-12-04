from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk

from Demos.win32ts_logoff_disconnected import username
from PIL import Image, ImageTk # we need to install pillow to import PIL - pip install pillow  ## for setting images inside the gui
import mysql.connector
import random
from tkinter import messagebox


class RoomWindow:
    def __init__(self, root):
        # doubt: what is the use of root?
        self.root = root
        self.root.title("ROOM BOOKING")
        self.root.geometry("1295x550+230+225")

        # storing the folder path for the image folder
        image_folder_path = 'D:/Python/Projects/Hotel Management System/images'

        # ============================================ variables for database============================================
        self.mobile_no_var = StringVar()
        self.check_in_date_var = StringVar()
        self.check_out_date_var = StringVar()
        self.room_type_var = StringVar()
        self.room_available_var = StringVar()
        self.meal_var = StringVar()
        self.no_of_days_var = StringVar()
        self.tax_var = StringVar()
        self.sub_total_var = StringVar()
        self.total_var = StringVar()


        # ============================================ heading ============================================
        lbltitle = Label(self.root, text="ROOM BOOKING", font=('times new roman', 15, 'bold'), bg='black',
                         fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)

        # ============================================ label frame left side ============================================
        lbl_frame1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details",
                                font=('times new roman', 12, 'bold'), padx=2)
        lbl_frame1.place(x=0, y=50, width=425, height=490)

        # ============================================ labels and entries ============================================
        # customer contact entry
        lbl_cust_contact = Label(lbl_frame1, text="Mobile Number:", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_cust_contact = ttk.Entry(lbl_frame1, textvariable=self.mobile_no_var, width=18, font=('arial', 13, 'bold'))
        entry_cust_contact.grid(row=0, column=1, sticky=W)

        # fetch data button
        btn_fetch = Button(lbl_frame1, text="Fetch", command=self.fetch_room_date, font=('arial', 10, 'bold'), bg="black",
                         fg="gold", width=8)
        btn_fetch.place(x=324, y=4)

        # check in date entry
        lbl_check_in_date = Label(lbl_frame1, text="Check-in Date:", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_check_in_date.grid(row=1, column=0, sticky=W)
        entry_check_in_date = DateEntry(lbl_frame1, textvariable=self.check_in_date_var, width=36, background='black',
                               foreground='white', borderwidth=2)
        entry_check_in_date.grid(row=1, column=1)
        # entry_check_in_date = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        # entry_check_in_date.grid(row=1, column=1)

        # check out date entry
        lbl_check_out_date = Label(lbl_frame1, text="Check-out Date", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_check_out_date.grid(row=2, column=0, sticky=W)
        entry_check_out_date = DateEntry(lbl_frame1, textvariable=self.check_out_date_var, width=36, background='black',
                                        foreground='white', borderwidth=2)
        entry_check_out_date.grid(row=2, column=1)
        # entry_check_out_date = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        # entry_check_out_date.grid(row=2, column=1)

        # room type combobox
        lbl_room_type = Label(lbl_frame1, text="Room Type", font=('arial', 12, 'bold'), padx=2,
                                pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)
        combo_room_type = ttk.Combobox(lbl_frame1, textvariable=self.room_type_var, font=('arial', 12, 'bold'), width=24, state="readonly")
        combo_room_type["value"] = ("Single", "Double", "Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        # Available room entry
        lbl_avail_rooms = Label(lbl_frame1, text="Available Rooms", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_avail_rooms.grid(row=4, column=0, sticky=W)
        entry_avail_rooms = ttk.Entry(lbl_frame1, width=26, textvariable=self.room_available_var, font=('arial', 13, 'bold'))
        entry_avail_rooms.grid(row=4, column=1)

        # Meal entry
        lbl_meal = Label(lbl_frame1, text="Meal", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        entry_meal = ttk.Entry(lbl_frame1, textvariable=self.meal_var, width=26, font=('arial', 13, 'bold'))
        entry_meal.grid(row=5, column=1)

        # no. of days entry
        lbl_no_of_days = Label(lbl_frame1, text="Number of Days", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        entry_no_of_days = ttk.Entry(lbl_frame1, textvariable=self.no_of_days_var, width=26, font=('arial', 13, 'bold'))
        entry_no_of_days.grid(row=6, column=1)

        # Tax entry
        lbl_tax = Label(lbl_frame1, text="Tax", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_tax.grid(row=7, column=0, sticky=W)
        entry_tax = ttk.Entry(lbl_frame1, textvariable=self.tax_var, width=26, font=('arial', 13, 'bold'))
        entry_tax.grid(row=7, column=1)

        # Sub Total entry
        lbl_sub_total = Label(lbl_frame1, text="Sub Total", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_sub_total.grid(row=8, column=0, sticky=W)
        entry_sub_total = ttk.Entry(lbl_frame1, textvariable=self.sub_total_var, width=26, font=('arial', 13, 'bold'))
        entry_sub_total.grid(row=8, column=1)

        # Total cost entry
        lbl_total = Label(lbl_frame1, text="Total", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_total.grid(row=9, column=0, sticky=W)
        entry_total = ttk.Entry(lbl_frame1, textvariable=self.total_var, width=26, font=('arial', 13, 'bold'))
        entry_total.grid(row=9, column=1)

        # create bill button
        btn_bill = Button(lbl_frame1, text="Bill", font=('arial', 12, 'bold'), bg="black",
                           fg="gold", width=9)
        btn_bill.grid(row=10, column=0, sticky=W)

        # ============================================ button frame ============================================
        btn_frame = Frame(lbl_frame1, bd=2, relief=RIDGE)
        # btn_frame.grid(row=10, column=0)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # buttons
        # Add Button
        btn_add = Button(btn_frame, text="Add", command=self.add_data, font=('arial', 12, 'bold'), bg="black",
                         fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        # Update Button
        btn_update = Button(btn_frame, text="Update", font=('arial', 12, 'bold'), bg="black",
                            fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        # Delete Button
        btn_del = Button(btn_frame, text="Delete", font=('arial', 12, 'bold'), bg="black",
                         fg="gold", width=9)
        btn_del.grid(row=0, column=2, padx=1)

        # Reset Button
        btn_clear = Button(btn_frame, text="Clear All", font=('arial', 12, 'bold'),
                           bg="black", fg="gold", width=9)
        btn_clear.grid(row=0, column=3, padx=1)


        # ============================================ section for output top right side ============================================

        # room

        # image
        image1 = Image.open(f'{image_folder_path}/bed.jpg')
        # resizing the image using Resampling.LANCZOS form Image lib
        image1 = image1.resize((488, 350), Image.Resampling.LANCZOS)
        # converting to image toolkit using ImageTk PhotoImage and passing the resized image
        self.img1 = ImageTk.PhotoImage(image1)
        # now using tkinter label we will show it in the window
        lblimg1 = Label(self.root, image=self.img1, bd=4, relief=RIDGE)
        # lblimg1.grid(row=0, column=1)
        lblimg1.place(x=800, y=55, width=488, height=350)




        # ============================================ label search frame right bottom side ============================================
        lbl_frame_search = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search",
                                font=('times new roman', 12, 'bold'), padx=2)
        lbl_frame_search.place(x=435, y=280, width=859, height=260)

        # ============================================ Search section ============================================
        # Search By label
        lbl_search_by = Label(lbl_frame_search, text="Search By:", font=('arial', 12, 'bold'), bg="red", fg="white", padx=1)
        lbl_search_by.grid(row=0, column=0, sticky=W)

        # Search by combobox
        self.search_option_var = StringVar()
        search_combo = ttk.Combobox(lbl_frame_search, textvariable=self.search_option_var, width=15,
                                    font=('arial', 12, 'bold'), state="readonly")
        search_combo["value"] = ("Mobile No.", "Check-in Date", "Check-out Date", "Room Type")
        search_combo.current(3)
        search_combo.grid(row=0, column=1, padx=3)

        self.search_dict = {"Mobile No.": 'mobile', "Check-in Date": 'checkindate', "Check-out Date": 'checkoutdate', "Room Type": 'roomtype'}

        # Search by Entry
        self.search_data_var = StringVar()
        search_entry = ttk.Entry(lbl_frame_search, textvariable=self.search_data_var, width=27, font=('arial', 13, 'bold'))
        search_entry.grid(row=0, column=2, padx=3)

        # Search Button
        btn_search = Button(lbl_frame_search, text="Search", font=('arial', 12, 'bold'),
                            bg="black", fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=2)

        # Show All Button
        btn_show_all = Button(lbl_frame_search, text="Show All", command=self.fetch_data, font=('arial', 12, 'bold'),
                              bg="black", fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=2)



        # ============================================ Table frame ============================================
        tbl_frame = Frame(lbl_frame_search, bd=2, relief=RIDGE)
        tbl_frame.place(x=0, y=32, width=860, height=206)

        # Scroll bars for x-axis and y-axis
        scroll_x = ttk.Scrollbar(tbl_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tbl_frame, orient=VERTICAL)

        # Tabel
        self.room_details_tbl = ttk.Treeview(tbl_frame, columns=(
        "mobile", "checkindate", "checkoutdate", "roomtype", "roomavailable", "meal", "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # packing scroll bars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # configuring scroll bars
        scroll_x.config(command=self.room_details_tbl.xview)
        scroll_y.config(command=self.room_details_tbl.yview)

        self.room_details_tbl.heading("mobile", text="Mobile No.")
        self.room_details_tbl.heading("checkindate", text="Check-in Date")
        self.room_details_tbl.heading("checkoutdate", text="Check-out Date")
        self.room_details_tbl.heading("roomtype", text="Room Type")
        self.room_details_tbl.heading("roomavailable", text="Room Available")
        self.room_details_tbl.heading("meal", text="Meal")
        self.room_details_tbl.heading("noOfdays", text="Number Of Days")

        self.room_details_tbl["show"] = "headings"

        self.room_details_tbl.column("mobile", width=100)
        self.room_details_tbl.column("checkindate", width=100)
        self.room_details_tbl.column("checkoutdate", width=100)
        self.room_details_tbl.column("roomtype", width=100)
        self.room_details_tbl.column("roomavailable", width=100)
        self.room_details_tbl.column("meal", width=100)
        self.room_details_tbl.column("noOfdays", width=100)

        self.room_details_tbl.pack(fill=BOTH, expand=1)
        self.fetch_data()



    # method to fetch all the customer data using the mobile no. if its already present in the DB
    def fetch_room_date(self):
        if self.mobile_no_var.get()  == "":
            messagebox.showerror("Error",
                                 "Please enter Mobile number.",
                                 parent = self.root)
        else:
            try:
                # database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n", database="hotel_management")
                # creating a cursor that will be used to run queries
                my_cursor = conn.cursor()

                query = "SELECT Name, Gender, Email, Nationality, Address FROM customer WHERE Mobile = %s"
                value = (self.mobile_no_var.get(),)
                # executing the query
                my_cursor.execute(query, value)
                # fetching the data returned by the query
                row = my_cursor.fetchone()

                if row == None:
                    messagebox.showerror("Error",
                                         "This mobile number doesn't exists.",
                                         parent = self.root)
                else:
                    # commiting and closing the connection
                    conn.commit()
                    conn.close()

                    # ============================================ Fetch output frame on the top right part ============================================
                    showDataFrame = Frame(self.root, bd=3, relief=RIDGE, padx=2)
                    showDataFrame.place(x=436, y=58, width=350, height=223)

                    lblName = Label(showDataFrame, text="Name:", font=('arial', 12, 'bold'))
                    lblName.place(x=0, y=0)
                    lblNameOutput = Label(showDataFrame, text=row[0], font=('arial', 12, 'bold'))
                    lblNameOutput.place(x=100, y=0)

                    lblGender = Label(showDataFrame, text="Gender:", font=('arial', 12, 'bold'))
                    lblGender.place(x=0, y=30)
                    lblGenderOutput = Label(showDataFrame, text=row[1], font=('arial', 12, 'bold'))
                    lblGenderOutput.place(x=100, y=30)

                    lblEmail = Label(showDataFrame, text="Email:", font=('arial', 12, 'bold'))
                    lblEmail.place(x=0, y=60)
                    lblEmailOutput = Label(showDataFrame, text=row[2], font=('arial', 12, 'bold'))
                    lblEmailOutput.place(x=100, y=60)

                    lblNationality = Label(showDataFrame, text="Nationality:", font=('arial', 12, 'bold'))
                    lblNationality.place(x=0, y=90)
                    lblNationalityOutput = Label(showDataFrame, text=row[3], font=('arial', 12, 'bold'))
                    lblNationalityOutput.place(x=100, y=90)

                    lblAddress = Label(showDataFrame, text="Address:", font=('arial', 12, 'bold'))
                    lblAddress.place(x=0, y=120)
                    lblAddressOutput = Label(showDataFrame, text=row[4], font=('arial', 12, 'bold'))
                    lblAddressOutput.place(x=100, y=120)
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Something went wrong: {str(e)}",
                                       parent = self.root)



    # method to add room details to the room table in the DB
    def add_data(self):
        # validation
        if self.mobile_no_var.get() == "" or self.check_in_date_var.get() == "" or self.check_out_date_var.get() == "" or self.room_available_var.get() == "":
            messagebox.showerror("Error",
                                 "Require Fields: Mobile Number, Check-in Date, Check-out Date, Room Available",
                                 parent=self.root)  # here the parent decided on which window the error message box will be shown
        else:
            try:
                # database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                               database="hotel_management")
                # creating a cursor that will be used to run queries
                my_cursor = conn.cursor()
                # executing the query using cursor
                my_cursor.execute('INSERT INTO room VALUES(%s,%s,%s,%s,%s,%s,%s)', (
                    self.mobile_no_var.get(),
                    self.check_in_date_var.get(),
                    self.check_out_date_var.get(),
                    self.room_type_var.get(),
                    self.room_available_var.get(),
                    self.meal_var.get(),
                    self.no_of_days_var.get()))
                # commiting and closing the connection
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",
                                    "Room Details Added",
                                    parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Something went wrong: {str(e)}",
                                       parent=self.root)



    # method to fetch customer details and to show in the details part
    def fetch_data(self):
        try:
            # database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                           database="hotel_management")

            # creating a cursor that will be used to run queries
            my_cursor = conn.cursor()
            # executing the query using cursor
            my_cursor.execute('SELECT * FROM room')
            # storing all the data that is fetched in the cursor
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.room_details_tbl.delete(
                    *self.room_details_tbl.get_children())  # clearing out the table variable
                for row in rows:
                    self.room_details_tbl.insert("", END, values=row)
            else:
                pass

            # commiting and closing the connection
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("Warning",
                                   f"Something went wrong: {str(e)}",
                                   parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = RoomWindow(root)
    root.mainloop()
