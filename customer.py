from tkinter import *

from Demos.win32ts_logoff_disconnected import username
from PIL import Image, ImageTk # we need to install pillow to import PIL - pip install pillow  ## for setting images inside the gui
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class CustomerWindow:

    def __init__(self, root):
        # doubt: what is the use of root?
        self.root = root
        self.root.title("CUSTOMER")
        self.root.geometry("1295x550+230+225")

        # storing the folder path for the image folder
        image_folder_path = 'D:/Python/Projects/Hotel Management System/images'

        # ============================================ variables for database ============================================
        self.ref_var = StringVar()
        x = random.randint(1000, 9999)
        # setting a random value to the reference no variable
        self.ref_var.set(str(x))

        self.name_var = StringVar()
        self.guardian_var = StringVar()
        self.gender_var = StringVar()
        self.postal_var = StringVar()
        self.mobile_var = StringVar()
        self.email_var = StringVar()
        self.nationality_var = StringVar()
        self.id_proof_var = StringVar()
        self.id_num_var = StringVar()
        self.address_var = StringVar()



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
        entry_cust_ref = ttk.Entry(lbl_frame1, textvariable=self.ref_var, width=26, font=('arial', 13, 'bold'), state="readonly")
        entry_cust_ref.grid(row=0, column=1)

        #customer name
        lbl_cust_name = Label(lbl_frame1, text="Name", font=('arial', 12, 'bold'), padx=2,
                             pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_cust_name = ttk.Entry(lbl_frame1, textvariable=self.name_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_name.grid(row=1, column=1)

        # customer guardian name
        lbl_cust_gname = Label(lbl_frame1, text="Guardian Name", font=('arial', 12, 'bold'), padx=2,
                              pady=6)
        lbl_cust_gname.grid(row=2, column=0, sticky=W)
        entry_cust_gname = ttk.Entry(lbl_frame1, textvariable=self.guardian_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_gname.grid(row=2, column=1)

        # customer gender combobox
        lbl_cust_gender = Label(lbl_frame1, text="Gender", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_gender.grid(row=3, column=0, sticky=W)
        gender_combo = ttk.Combobox(lbl_frame1, textvariable=self.gender_var, font=('arial', 12, 'bold'), width=24, state="readonly")
        gender_combo["value"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1)

        # customer postal code
        lbl_cust_postcode = Label(lbl_frame1, text="Postcode", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_postcode.grid(row=4, column=0, sticky=W)
        entry_cust_postcode = ttk.Entry(lbl_frame1, textvariable=self.postal_var, width=26, font=('arial', 13, 'bold'), validate='key', validatecommand=vcmd)
        entry_cust_postcode.grid(row=4, column=1)

        # customer mobile number
        lbl_cust_mobnum = Label(lbl_frame1, text="Mobile Number", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_mobnum.grid(row=5, column=0, sticky=W)
        entry_cust_mobnum = ttk.Entry(lbl_frame1, textvariable=self.mobile_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_mobnum.grid(row=5, column=1)

        # customer email
        lbl_cust_email = Label(lbl_frame1, text="Email", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_email.grid(row=6, column=0, sticky=W)
        entry_cust_email = ttk.Entry(lbl_frame1, textvariable=self.email_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_email.grid(row=6, column=1)

        # customer nationality combobox
        lbl_cust_nationality = Label(lbl_frame1, text="Nationality", font=('arial', 12, 'bold'), padx=2,
                                pady=6)
        lbl_cust_nationality.grid(row=7, column=0, sticky=W)
        nationality_combo = ttk.Combobox(lbl_frame1, textvariable=self.nationality_var, font=('arial', 12, 'bold'), width=24, state="readonly")
        nationality_combo["value"] = ('India', 'Bangladesh', 'United States', 'United Kingdom', 'Sri Lanka', 'Nepal', 'Bhutan', 'China', 'Pakistan', 'Africa', 'United Arab Emirates')
        nationality_combo.current(0)
        nationality_combo.grid(row=7, column=1)

        # customer id proof type combobox
        lbl_cust_idtype = Label(lbl_frame1, text="Id Proof Type", font=('arial', 12, 'bold'), padx=2,
                                pady=6)
        lbl_cust_idtype.grid(row=8, column=0, sticky=W)
        idtype_combo = ttk.Combobox(lbl_frame1, textvariable=self.id_proof_var, font=('arial', 12, 'bold'), width=24, state="readonly")
        idtype_combo["value"] = ("Aadhar Id", "Voter Id", "Passport", "Driver's Licence")
        idtype_combo.current(0)
        idtype_combo.grid(row=8, column=1)


        # customer id number
        lbl_cust_idnum = Label(lbl_frame1, text="Id Number", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_idnum.grid(row=9, column=0, sticky=W)
        entry_cust_idnum = ttk.Entry(lbl_frame1, textvariable=self.id_num_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_idnum.grid(row=9, column=1)

        # customer address
        lbl_cust_addr = Label(lbl_frame1, text="Address", font=('arial', 12, 'bold'), padx=2,
                               pady=6)
        lbl_cust_addr.grid(row=10, column=0, sticky=W)
        entry_cust_addr = ttk.Entry(lbl_frame1, textvariable=self.address_var, width=26, font=('arial', 13, 'bold'))
        entry_cust_addr.grid(row=10, column=1)

        # ============================================ button frame ============================================
        btn_frame = Frame(lbl_frame1, bd=2, relief=RIDGE)
        # btn_frame.grid(row=10, column=0)
        btn_frame.place(x=0,y=400, width=412, height=40)

        #buttons
        # Add Button
        btn_add = Button(btn_frame, text="Add", command=self.add_data,font=('arial',12, 'bold'), bg="black", fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        # Update Button
        btn_update = Button(btn_frame, text="Update", command=self.update_data, font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        # Delete Button
        btn_del = Button(btn_frame, text="Delete", command=self.delete_data, font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_del.grid(row=0, column=2, padx=1)

        # Reset Button
        btn_clear = Button(btn_frame, text="Clear All", command=self.clear_entry_fields, font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_clear.grid(row=0, column=3, padx=1)

        # ============================================ label frame right side ============================================
        lbl_frame2 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search",
                                font=('times new roman', 12, 'bold'), padx=2)
        lbl_frame2.place(x=435, y=50, width=860, height=490)

        # ============================================ Search section ============================================
        # Search By label
        lbl_search_by = Label(lbl_frame2, text="Search By:", font=('arial', 12, 'bold'), bg="red", fg="white", padx=1)
        lbl_search_by.grid(row=0, column=0, sticky=W)

        # Search by combobox
        self.search_option_var = StringVar()
        search_combo = ttk.Combobox(lbl_frame2, textvariable=self.search_option_var, width=15, font=('arial', 12, 'bold'), state="readonly")
        search_combo["value"] = ("Reference No.", "Name", "Guardian's Name", "Mobile", "Email", "Id Number", "Address")
        search_combo.current(3)
        search_combo.grid(row=0, column=1, padx=3)

        self.search_dict = {"Reference No.":'Ref', "Name": 'Name', "Guardian's Name": 'Guardian', "Mobile": 'Mobile', "Email": 'Email', "Id Number": 'Idnumber', "Address":'Address'}

        # Search by Entry
        self.search_data_var = StringVar()
        search_entry = ttk.Entry(lbl_frame2, textvariable=self.search_data_var, width=27, font=('arial', 13, 'bold'))
        search_entry.grid(row=0, column=2, padx=3)

        # Search Button
        btn_search = Button(lbl_frame2, text="Search", command= self.search_records, font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=2)

        # Show All Button
        btn_show_all = Button(lbl_frame2, text="Show All", command= self.fetch_data, font=('arial', 12, 'bold'), bg="black", fg="gold", width=9)
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
        self.cust_details_tbl.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    # method to add customer details in the database
    def add_data(self):
        # validation
        if self.mobile_var.get() == "" or self.name_var.get() == "" or self.id_num_var.get() == "":
            messagebox.showerror("Error",
                                 "Require Fields: Name, Mobile Number, Id Number",
                                 parent = self.root) # here the parent decided on which window the error message box will be shown
        else:
            try:
                # database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n", database="hotel_management")
                # creating a cursor that will be used to run queries
                my_cursor = conn.cursor()
                # executing the query using cursor
                my_cursor.execute('INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                    self.ref_var.get(),
                                                                                                    self.name_var.get(),
                                                                                                    self.guardian_var.get(),
                                                                                                    self.gender_var.get(),
                                                                                                    self.postal_var.get(),
                                                                                                    self.mobile_var.get(),
                                                                                                    self.email_var.get(),
                                                                                                    self.nationality_var.get(),
                                                                                                    self.id_proof_var.get(),
                                                                                                    self.id_num_var.get(),
                                                                                                    self.address_var.get()))
                # commiting and closing the connection
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",
                                    "Customer Details Added",
                                    parent = self.root)
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Something went wrong: {str(e)}",
                                       parent = self.root)



    # method to fetch customer details and to show in the details part
    def fetch_data(self):
        try:
            # database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                           database="hotel_management")

            # creating a cursor that will be used to run queries
            my_cursor = conn.cursor()
            # executing the query using cursor
            my_cursor.execute('SELECT * FROM customer')
            # storing all the data that is fetched in the cursor
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.cust_details_tbl.delete(*self.cust_details_tbl.get_children()) #clearing out the table variable
                for row in rows:
                    self.cust_details_tbl.insert("", END, values=row)
            else:
                pass

            # commiting and closing the connection
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("Warning",
                                   f"Something went wrong: {str(e)}",
                                   parent=self.root)



    # method to get the info from the treeview table to the entry field so that we can update it
    def get_cursor(self, event=""): # pass the second param event to pass a event which will help bind
        # creating a cursor variable
        cursor_row = self.cust_details_tbl.focus() # we have to first focus on the table

        # store the item of the table that has the focus on it in a variable
        content = self.cust_details_tbl.item(cursor_row)

        # storing the content value in a different variable
        row = content["values"]

        # now we can access all the row values from the row variable
        # setting all the variable names to the values that we have in the rows variable
        self.ref_var.set(row[0])
        self.name_var.set(row[1])
        self.guardian_var.set(row[2])
        self.gender_var.set(row[3])
        self.postal_var.set(row[4])
        self.mobile_var.set(row[5])
        self.email_var.set(row[6])
        self.nationality_var.set(row[7])
        self.id_proof_var.set(row[8])
        self.id_num_var.set(row[9])
        self.address_var.set(row[10])

        # now we have to bind this function within the table



    # method to update the data in the Database
    def update_data(self):
        # validation
        if self.mobile_var.get() == "" or self.name_var.get() == "" or self.id_num_var.get() == "":
            messagebox.showerror("Error",
                                 "Require Fields: Name, Mobile Number, Id Number",
                                 parent=self.root)
        else:
            try:
                # database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                               database="hotel_management")
                # creating a cursor that will be used to run queries
                my_cursor = conn.cursor()
                # executing the query using cursor
                my_cursor.execute('UPDATE customer SET Name=%s, Guardian=%s, Gender=%s, PostalCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE Ref=%s',
                                  (
                                            self.name_var.get(),
                                            self.guardian_var.get(),
                                            self.gender_var.get(),
                                            self.postal_var.get(),
                                            self.mobile_var.get(),
                                            self.email_var.get(),
                                            self.nationality_var.get(),
                                            self.id_proof_var.get(),
                                            self.id_num_var.get(),
                                            self.address_var.get(),
                                            self.ref_var.get()
                                            )
                                  )
                # commiting and closing the connection
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",
                                    "Customer Details Updated",
                                    parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Something went wrong: {str(e)}",
                                       parent=self.root)




    # method to delete data from the Database
    def delete_data(self):
        # getting a confirmation using messagebox before deleting a record from the Databasae
        do_del = messagebox.askyesno("Confirmation", "Do you want to delete the record?")
        if do_del:
            try:
                # database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                               database="hotel_management")
                # creating a cursor that will be used to run queries
                my_cursor = conn.cursor()

                # executing the query using cursor
                # we can assign the query and the value from the entry fields to variables and pass them to the execute method
                query = 'DELETE FROM customer WHERE Ref=%s'
                value = (self.ref_var.get(),)
                my_cursor.execute(query, value)

                # commiting and closing the connection
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",
                                    "Customer Details Deleted",
                                    parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning",
                                       f"Something went wrong: {str(e)}",
                                       parent=self.root)
        else:
            return



    # method to clear all the entry fields and reset them to original state
    def clear_entry_fields(self):
        # we have to just set all the text-variables to empty strings

        # we will put a new reference no. in the ref variable
        x = random.randint(1000, 9999)
        self.ref_var.set(str(x))

        self.name_var.set("")
        self.guardian_var.set("")
        # self.gender_var.set("")
        self.postal_var.set("")
        self.mobile_var.set("")
        self.email_var.set("")
        # self.nationality_var.set("")
        # self.id_proof_var.set("")
        self.id_num_var.set("")
        self.address_var.set(r"")




    # method to search records based on a filter
    def search_records(self):
        try:
            # database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="123456@Rp@n",
                                           database="hotel_management")
            # creating a cursor that will be used to run queries
            my_cursor = conn.cursor()

            # executing the query using cursor
            # we can assign the query and the value from the entry fields to variables and pass them to the execute method
            query = f"SELECT * FROM customer WHERE {str(self.search_dict[self.search_option_var.get()])} LIKE '%{str(self.search_data_var.get())}%'"
            my_cursor.execute(query)
            # now we will fetch the result into a variable
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                # first we will delete the data into the existing table
                self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
                # enter the fetched data into the table
                for row in rows:
                    self.cust_details_tbl.insert("", END, values=row)
                self.search_data_var.set("")
            else:
                self.cust_details_tbl.delete(*self.cust_details_tbl.get_children())
                messagebox.showinfo("Search",
                                    "No matching data found.",
                                    parent = self.root)

            # commiting and closing the connection
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("Warning",
                                   f"Something went wrong: {str(e)}",
                                   parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()