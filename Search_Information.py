from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv


# create a class 
class search_information:
    def __init__(self):
        # create a GUI for search
        self.search_gui = Tk()
        self.search_gui.title("Search Your Entry")
        self.search_gui.geometry('550x245')

        self.head_frame = Frame(self.search_gui, bd=2, relief="groove", bg="#FF0000")
        self.head_frame.place(x=5, y=5, width=540, height=60)
        self.head_label = Label(self.head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
        self.head_label.pack(pady=10)

        padding_frame = Frame(self.search_gui, bd=2, relief="groove")
        padding_frame.place(x=5, y=70, width=540, height=170)

        self.referencenum_label = Label(self.search_gui, text="PLEASE ENTER YOUR REFERENCE NUMBER: ")
        self.referencenum_label.place(x=15, y=100)
        self.referencenum_entry = Entry(self.search_gui, width='35')
        self.referencenum_entry.place(x=255, y=100)

        # create an instance of ForgotRefNum
        self.forgot_ref_num = ForgotRefNum(self.search_gui)

        # create a forget button for those who forget their reference number
        self.forget_text = Label(self.search_gui, text='Note: in case you forgot your own reference number please click "Forgot Reference Number"\r for other ways of searching your information')
        self.forget_text.place(x=25, y=130)
        self.forget_btn = Button(self.search_gui, text='Forgot Reference Number', command=self.forgot_ref_num.create_new_tab)
        self.forget_btn.place(x=190, y=175)

        # create a button for search
        self.search_btn = Button(self.search_gui, text='Search', command=self.search_entry)
        self.search_btn.place(x=480, y=97)

        self.data_list = self.read_csv()

        self.search_gui.mainloop()

    # Add contents to the forgot the reference button choice
    def create_info_tab(self):
        # create another tab for displaying all the inputs in the csv file
        info_tab = Toplevel(self.search_gui)
        info_tab.title("Your Information")
        self.show_data(info_tab)

    # read the csv for possible entry
    def read_csv(self):
        data_list = []
        try:
            with open("contact_tracing_data.csv", newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data_list.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found!")
        return data_list
    
    def search_entry(self):
        reference_number = self.referencenum_entry.get()

        if reference_number:
            for entry in self.data_list:
                if reference_number in entry:
                    messagebox.showinfo("Entry Found", "Your reference number is listed in the data file.")
                    self.create_ref_tab()
                    return
            messagebox.showinfo("Entry Not Found", "Your reference number is not listed in the data file.")
        else:
            messagebox.showwarning("Warning", "Please enter your reference number!")
        
    def show_data(self, tab):
    # function to display data in a new tab using a treeview widget
        tree_frame = Frame(tab)
        tree_frame.pack(fill="both", expand=True)

        tree = ttk.Treeview(tree_frame)
        tree.grid(row=0, column=0, sticky="nsew")

        tree_scroll_y = Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
        tree_scroll_y.grid(row=0, column=1, sticky="ns")
        tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
        tree_scroll_x.grid(row=1, column=0, columnspan=2, sticky="ew")

        tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    # define columns for the treeview
        tree["columns"] = [
            "Reference Number", "Last Name", "Middle Name", "First Name",
            "Age", "Address", "Contact Number", "Gender", "Email",
            "Vaccination Status", "Symptoms", "Exposure[yes]", "Exposure[no]",
            "Guardian Last Name", "Guardian First Name", "Guardian Relationship",
            "Guardian Contact Number", "Guardian Email"
        ]
    # format columns
        tree.column("#0", width=0, stretch=NO)
        for column in tree["columns"]:
            tree.column(column, anchor=W, width=150)
            tree.heading(column, text=column)

    # insert data rows
        for entry in self.data_list:
            tree.insert("", "end", values=entry)
    # configure the grids weight to resize the treeview properly
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)

    # add function for forgot button
class ForgotRefNum:
    def __init__(self, search_gui):
        # store the search_gui instance for later use
        self.search_gui = search_gui
    def create_new_tab(self):
        new_tab = Toplevel(self.search_gui)
        new_tab.title("Other way to see your information")
        new_tab.geometry('820x325')

        head_frame = Frame(new_tab, bd=2, relief="groove", bg="#FF0000")
        head_frame.place(x=5, y=5, width=810, height=60)
        head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
        head_label.pack(pady=10)

        padding_frame = Frame(new_tab, bd=2, relief="groove")
        padding_frame.place(x=5, y=70, width=810, height=250)

        instruction_label = Label(new_tab, text="This panel will be the other way for you to confirm that you've entered your information in the application. May you please fill all the needed information")
        instruction_label.place(x=25,y=80)

        lastname_label = Label(new_tab,text = "LAST NAME : ")
        lastname_label.place(x=10, y=120)
        self.lastname_entry = Entry(new_tab,width="28") 
        self.lastname_entry.place(x=90,y=120)

        middlename_label = Label(new_tab,text = "MIDDLE NAME : ")
        middlename_label.place(x=270, y=120)
        self.middlename_entry = Entry(new_tab,width="28") 
        self.middlename_entry.place(x=365,y=120)

        firstname_label = Label(new_tab,text = "FIRST NAME : ")
        firstname_label.place(x=545, y=120)
        self.firstname_entry = Entry(new_tab,width="28") 
        self.firstname_entry.place(x=625,y=120)

        age_label = Label(new_tab, text= "AGE : ")
        age_label.place(x=10, y=160)
        self.age_entry = Scale(new_tab, from_=1, to=100, length="730",orient="horizontal")
        self.age_entry.place(x=65,y=140)

        address_label = Label(new_tab, text="ADDRESS : ")
        address_label.place(x=10,y=190)
        self.address_entry = Entry(new_tab, width=120)
        self.address_entry.place(x=75,y=190)

        contactnum_label = Label(new_tab, text="CONTACT NUMBER : ")
        contactnum_label.place(x=10,y=220)
        self.contactnum_entry = Entry(new_tab, width='45')
        self.contactnum_entry.place(x=130,y=220)

        gender_label = Label(new_tab, text="GENDER : ")
        gender_label.place(x=410,y=220)
        self.gender_entry = ttk.Combobox(new_tab, width="50", values=["Prefer Not to Say", "Male", "Female", "LGBTQ+", "Other"])
        self.gender_entry.place(x=475,y=220)

        email_label = Label(new_tab, text="EMAIL : ")
        email_label.place(x=10,y=250)
        self.email_entry = Entry(new_tab, width=122)
        self.email_entry.place(x=60,y=250)

        search_btn = Button(new_tab, text="Search", command=self.search_info)
        search_btn.place(x=375,y=280)

    def search_info(self):
        last_name = self.lastname_entry.get().upper()
        middle_name = self.middlename_entry.get().upper()
        first_name = self.firstname_entry.get().upper()
        age = int(self.age_entry.get())
        address = self.address_entry.get().upper()
        contact_number = self.contactnum_entry.get()
        gender = self.gender_entry.get()
        email = self.email_entry.get().upper()

        with open("contact_tracing_data.csv", "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if (
                    row["Last Name"] == last_name
                    and row["Middle Name"] == middle_name
                    and row["First Name"] == first_name
                    and int(row["Age"]) == age
                    and row["Address"] == address
                    and row["Contact Number"] == contact_number
                    and row["Gender"] == gender
                    and row["Email"] == email
                ):
                    messagebox.showinfo("Information Found, You've been registered", "Your information:\n"
                                        f"Last Name: {row['Last Name']}\n"
                                        f"Middle Name: {row['Middle Name']}\n"
                                        f"First Name: {row['First Name']}\n"
                                        f"Age: {row['Age']}\n"
                                        f"Address: {row['Address']}\n"
                                        f"Contact Number: {row['Contact Number']}\n"
                                        f"Gender: {row['Gender']}\n"
                                        f"Email: {row['Email']}")
                    return

        messagebox.showerror("Wrong Credentials", "Wrong credentials. Please try again.")
    
if __name__ == "__main__":
    search_app = search_information()