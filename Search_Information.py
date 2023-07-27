from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv


# create a class 
class search_information:
    def __init__(self):
# create a GUI for seach
        self.search_gui = Tk()
        self.search_gui.title("Search Your Entry")
        self.search_gui.geometry('550x245')

        # Set the width of the head_frame to the width of the search_gui
        self.head_frame = Frame(self.search_gui, bd=2, relief="groove", bg="#FF0000")  # Stylish red color
        self.head_frame.place(x=5, y=5, width=540, height=60)  # Updated width to 390
        self.head_label = Label(self.head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
        self.head_label.pack(pady=10)

        padding_frame = Frame(self.search_gui, bd=2, relief="groove")
        padding_frame.place(x=5, y=70, width=540, height=170)

        self.referencenum_label = Label(self.search_gui, text="PLEASE ENTER YOUR REFERENCE NUMBER: ")
        self.referencenum_label.place(x=15,y=100)
        self.referencenum_entry = Entry(self.search_gui, width='35')
        self.referencenum_entry.place(x=255,y=100)

        # create a forget button for those who forget their reference number
        self.forget_text = Label(self.search_gui, text='Note: in case you forgot your own reference number please click "Forgot Reference Number"\r for other ways of searching your inforamtion')
        self.forget_text.place(x=25,y=130)
        self.forget_btn = Button(self.search_gui, text='Forgot Reference Number', command=self.create_new_tab)
        self.forget_btn.place(x=190,y=175)

        # create a button for search
        self.search_btn = Button(self.search_gui, text='Search', command=self.search_entry)
        self.search_btn.place(x=480,y=97)

        self.data_list = self.read_csv()

        self.search_gui.mainloop()

    # add function for forgot button
    def create_new_tab(self):
        # Function to create another tab when the "Forgot Reference Number" button is pressed
        new_tab = Toplevel(self.search_gui)
        new_tab.title("Other way to see your information")
        new_tab.geometry('820x325')
        # heading
        head_frame = Frame(new_tab, bd=2, relief="groove", bg="#FF0000")  # Stylish red color
        head_frame.place(x=5, y=5, width=810, height=60)
        head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
        head_label.pack(pady=10)
        # padding
        padding_frame = Frame(new_tab, bd=2, relief="groove")
        padding_frame.place(x=5, y=70, width=810, height=250)
        # instruction
        instruction_label = Label(new_tab, text="This pannel will be the other way for you to confirm that you've entered your information in the application. May you please fill all the needed \rinformation")
        instruction_label.place(x=25,y=80)
        # input last name
        lastname_label = Label(new_tab,text = "LAST NAME : ")
        lastname_label.place(x=10, y=120)
        lastname_entry = Entry(new_tab,width="28") 
        lastname_entry.place(x=90,y=120)
        # input middle name
        middlename_label = Label(new_tab,text = "MIDDLE NAME : ")
        middlename_label.place(x=270, y=120)
        middlename_entry = Entry(new_tab,width="28") 
        middlename_entry.place(x=365,y=120)
        # input first name
        firstname_label = Label(new_tab,text = "FIRST NAME : ")
        firstname_label.place(x=545, y=120)
        firstname_entry = Entry(new_tab,width="28") 
        firstname_entry.place(x=625,y=120)
        # age
        age_label = Label(new_tab, text= "AGE : ")
        age_label.place(x=10, y=160)
        age_entry = Scale(new_tab, from_=1, to=100, length="730",orient="horizontal")
        age_entry.place(x=65,y=140)
        # address
        address_label = Label(new_tab, text="ADDRESS : ")
        address_label.place(x=10,y=190)
        address_entry = Entry(new_tab, width=120)
        address_entry.place(x=75,y=190)
        # contact number
        contactnum_label = Label(new_tab, text="CONTACT NUMBER : ")
        contactnum_label.place(x=10,y=220)
        contactnum_entry = Entry(new_tab, width='45')
        contactnum_entry.place(x=130,y=220)
        # gender
        gender_label = Label(new_tab, text="GENDER : ")
        gender_label.place(x=410,y=220)
        gender_entry = ttk.Combobox(new_tab, width="50",values=["Prefer Not to Say", "Male", "Female", "LGBTQ+", "Other"])
        gender_entry.place(x=475,y=220)
        # email
        email_label = Label(new_tab, text="EMAIL : ")
        email_label.place(x=10,y=250)
        email_entry = Entry(new_tab, width=122)
        email_entry.place(x=60,y=250)
        # create a search button
        search_btn = Button(new_tab, text="Search")
        search_btn.place(x=375,y=280)
        # gather all the inputs 
        def search_info(self):
            last_name = lastname_entry.get().upper()
            middle_name = middlename_entry.get().upper()
            first_name = firstname_entry.get().upper()
            age = age_entry.get().upper()
            address = address_entry.get().upper()
            contact_number = contactnum_entry.get().upper()
            gender = gender_entry.get().upper()
            email = email_entry.get().upper()
        # read csv is there is a same input
            with open("contact_tracing_data.csv", "r") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    if (
                        row["LAST_NAME"] == last_name
                        and row["MIDDLE_NAME"] == middle_name
                        and row["FIRST_NAME"] == first_name
                        and row["AGE"] == age
                        and row["ADDRESS"] == address
                        and row["CONTACT_NUMBER"] == contact_number
                        and row["GENDER"] == gender
                        and row["EMAIL"] == email
                    ):
                        # print your info
                        print("Your information:")
                        print("Last Name:", row["LAST_NAME"])
                        print("Middle Name:", row["MIDDLE_NAME"])
                        print("First Name:", row["FIRST_NAME"])
                        print("Age:", row["AGE"])
                        print("Address:", row["ADDRESS"])
                        print("Contact Number:", row["CONTACT_NUMBER"])
                        print("Gender:", row["GENDER"])
                        print("Email:", row["EMAIL"])
                        break
                else:
                    # if no match is found, inform the user
                    print("No matching information found.")
        # print your info

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
if __name__ == "__main__":
    search_app = search_information()