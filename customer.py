from tkinter import *
from PIL import Image, ImageTk # we need to install pillow to import PIL - pip install pillow  ## for setting images inside the gui
from tkinter import ttk


class Customer_window:

    def __init__(self, root):
        # doubt: what is the use of root?
        self.root = root
        self.root.title("CUSTOMER")
        self.root.geometry("1295x550+230+225")

        # storing the folder path for the image folder
        image_folder_path = 'D:/Python/Projects/Hotel Management System/images'


        # validating input is number and 10 digits or not in the mobile number entry field
        def validate_input(P):
            if P.isdigit() and len(P) <= 10:
                return True
            elif P == "":
                return True
            else:
                return False

        vcmd = (root.register(validate_input), '%P')



        # ============================================ heading ============================================
        lbltitle = Label(self.root, text="ADD CUSTOMER DETAILS", font=('times new roman', 15, 'bold'), bg='black',
                         fg='gold', bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1295, height=50)

        # ============================================ label frame left side ============================================
        lbl_frame1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=('times new roman', 12, 'bold'), padx = 2)
        lbl_frame1.place(x=0, y=50, width=425, height=490)

        # ============================================ labels and entries ============================================
        #customer reference
        lbl_cust_ref = Label(lbl_frame1, text="Customer Reference", font=('arial', 12, 'bold'), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_cust_ref = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_ref.grid(row=0, column=1)

        #customer name
        lbl_cust_name = Label(lbl_frame1, text="Name", font=('arial', 12, 'bold'), padx=2,
                             pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_cust_name = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_name.grid(row=1, column=1)

        # customer guardian name
        lbl_cust_gname = Label(lbl_frame1, text="Guardian Name", font=('arial', 12, 'bold'), padx=2,
                              pady=6)
        lbl_cust_gname.grid(row=2, column=0, sticky=W)
        entry_cust_gname = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_gname.grid(row=2, column=1)

        # customer gender combobox
        lbl_cust_gender = Label(lbl_frame1, text="Gender", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_gender.grid(row=3, column=0, sticky=W)
        gender_combo = ttk.Combobox(lbl_frame1, font=('arial', 12, 'bold'), width=24, state="readonly")
        gender_combo["value"] = ("Male", "Femail", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1)

        # customer postcode
        lbl_cust_postcode = Label(lbl_frame1, text="Postcode", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_postcode.grid(row=4, column=0, sticky=W)
        entry_cust_postcode = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'), validate='key', validatecommand=vcmd)
        entry_cust_postcode.grid(row=4, column=1)

        # customer mobile number
        lbl_cust_mobnum = Label(lbl_frame1, text="Mobile Number", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_mobnum.grid(row=5, column=0, sticky=W)
        entry_cust_mobnum = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_mobnum.grid(row=5, column=1)

        # customer email
        lbl_cust_email = Label(lbl_frame1, text="Email", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_email.grid(row=6, column=0, sticky=W)
        entry_cust_email = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_email.grid(row=6, column=1)

        # customer nationality combobox
        lbl_cust_nationality = Label(lbl_frame1, text="Nationality", font=('arial', 12, 'bold'), padx=2,
                                pady=6)
        lbl_cust_nationality.grid(row=7, column=0, sticky=W)
        nationality_combo = ttk.Combobox(lbl_frame1, font=('arial', 12, 'bold'), width=24, state="readonly")
        nationality_combo["value"] = ('India', 'Bangladesh', 'United States', 'United Kingdom', 'Sri Lanka', 'Nepal', 'Bhutan', 'China', 'Pakistan', 'Africa', 'United Arab Emirates')
        nationality_combo.current(0)
        nationality_combo.grid(row=7, column=1)

        # customer id proof type combobox
        lbl_cust_idtype = Label(lbl_frame1, text="Id Proof Type", font=('arial', 12, 'bold'), padx=2,
                                pady=6)
        lbl_cust_idtype.grid(row=8, column=0, sticky=W)
        idtype_combo = ttk.Combobox(lbl_frame1, font=('arial', 12, 'bold'), width=24, state="readonly")
        idtype_combo["value"] = ("Aadhar Id", "Voter Id", "Passport", "Driver's Licence")
        idtype_combo.current(0)
        idtype_combo.grid(row=8, column=1)


        # customer id number
        lbl_cust_idnum = Label(lbl_frame1, text="Id Number", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_idnum.grid(row=9, column=0, sticky=W)
        entry_cust_idnum = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_idnum.grid(row=9, column=1)

        # customer address
        lbl_cust_addr = Label(lbl_frame1, text="Address", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_addr.grid(row=10, column=0, sticky=W)
        entry_cust_addr = ttk.Entry(lbl_frame1, width=26, font=('arial', 13, 'bold'))
        entry_cust_addr.grid(row=10, column=1)

        # ============================================ button frame ============================================
        btn_frame = Frame(lbl_frame1, bd=2, relief=RIDGE)
        # btn_frame.grid(row=10, column=0)
        btn_frame.place(x=0,y=400, width=412, height=40)

        #buttons
        # Add Button
        btn_add = Button(btn_frame, text="Add", font=('arial',12, 'bold'), bg="black", fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        # Update Button
        btn_update = Button(btn_frame, text="Update", font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        # Delete Button
        btn_del = Button(btn_frame, text="Delete", font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_del.grid(row=0, column=2, padx=1)

        # Reset Button
        btn_reset = Button(btn_frame, text="Reset", font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_reset.grid(row=0, column=3, padx=1)

        # ============================================ label frame right side ============================================
        lbl_frame2 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search",
                                font=('times new roman', 12, 'bold'), padx=2)
        lbl_frame2.place(x=435, y=50, width=860, height=490)

        # ============================================ Search section ============================================
        # Search By label
        lbl_search_by = Label(lbl_frame2, text="Search By:", font=('arial', 12, 'bold'), bg="red", fg="white", padx=1)
        lbl_search_by.grid(row=0, column=0, sticky=W)

        # Search by combobox
        search_combo = ttk.Combobox(lbl_frame2, width=15, font=('arial', 12, 'bold'), state="readonly")
        search_combo["value"] = ("Reference No.", "Name", "Guardian's Name", "Mobile", "Email", "Id Number", "Address")
        search_combo.current(3)
        search_combo.grid(row=0, column=1, padx=3)

        # Search by Entry
        search_entry = ttk.Entry(lbl_frame2, width=27, font=('arial', 13, 'bold'))
        search_entry.grid(row=0, column=2, padx=3)

        # Search Button
        btn_search = Button(lbl_frame2, text="Search", font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=2)

        # Show All Button
        btn_show_all = Button(lbl_frame2, text="Show All", font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=2)

        # ============================================ Table frame ============================================
        tbl_frame = Frame(lbl_frame2, bd=2, relief=RIDGE)
        tbl_frame.place(x=0, y=60, width=860, height=350)

        # Scroll bars for x-axis and y-axis
        scroll_x = ttk.Scrollbar(tbl_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tbl_frame, orient=VERTICAL)

        # Tabel
        self.cust_details_tbl = ttk.Treeview(tbl_frame, columns=("ref", "name", "guardian_name", "gender", "postal", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # packing scroll bars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # configuring scroll bars
        scroll_x.config(command=self.cust_details_tbl.xview)
        scroll_y.config(command=self.cust_details_tbl.yview)

        self.cust_details_tbl.heading("ref", text="Reference No.")
        self.cust_details_tbl.heading("name", text="Name")
        self.cust_details_tbl.heading("guardian_name", text="Guardian Name")
        self.cust_details_tbl.heading("gender", text="Gender")
        self.cust_details_tbl.heading("postal", text="Postal Code")
        self.cust_details_tbl.heading("mobile", text="Mobile No.")
        self.cust_details_tbl.heading("email", text="Email")
        self.cust_details_tbl.heading("nationality", text="Nationality")
        self.cust_details_tbl.heading("idproof", text="Id Proof")
        self.cust_details_tbl.heading("idnumber", text="Id Number")
        self.cust_details_tbl.heading("address", text="Address")

        self.cust_details_tbl["show"] = "headings"

        self.cust_details_tbl.column("ref", width=100)
        self.cust_details_tbl.column("name", width=100)
        self.cust_details_tbl.column("guardian_name", width=100)
        self.cust_details_tbl.column("gender", width=100)
        self.cust_details_tbl.column("postal", width=100)
        self.cust_details_tbl.column("mobile", width=100)
        self.cust_details_tbl.column("email", width=100)
        self.cust_details_tbl.column("nationality", width=100)
        self.cust_details_tbl.column("idproof", width=100)
        self.cust_details_tbl.column("idnumber", width=100)
        self.cust_details_tbl.column("address", width=100)

        self.cust_details_tbl.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()