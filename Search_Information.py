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
        self.search_gui.geometry('550x250')

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

    # add function for each entry
    def create_new_tab(self):
        # Function to create another tab when the "Forgot Reference Number" button is pressed
        new_tab = Toplevel(self.search_gui)
        new_tab.title("Other way to see your information")

        # Add contents to the forgot the reference button choice

    def create_ref_tab(self):
        # create another tab for displaying all the inputs in the csv file
        ref_tab = Toplevel(self.search_gui)
        ref_tab.title("Your Information")
        self.show_data(ref_tab)

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

        tree_scroll = Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
        tree_scroll.grid(row=0, column=1, sticky="ns")

        tree.configure(yscrollcommand=tree_scroll.set)
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
        tree.column("Reference Number", anchor=CENTER, width=100)
        tree.column("Last Name", anchor=W, width=100)
        tree.column("Middle Name", anchor=W, width=100)
        tree.column("First Name", anchor=W, width=100)
        tree.column("Age", anchor=CENTER, width=60)
        tree.column("Address", anchor=W, width=200)
        tree.column("Contact Number", anchor=W, width=120)
        tree.column("Gender", anchor=CENTER, width=80)
        tree.column("Email", anchor=W, width=200)
        tree.column("Vaccination Status", anchor=W, width=150)
        tree.column("Symptoms", anchor=W, width=200)
        tree.column("Exposure[yes]", anchor=CENTER, width=100)
        tree.column("Exposure[no]", anchor=CENTER, width=100)
        tree.column("Guardian Last Name", anchor=W, width=100)
        tree.column("Guardian First Name", anchor=W, width=100)
        tree.column("Guardian Relationship", anchor=W, width=120)
        tree.column("Guardian Contact Number", anchor=W, width=120)
        tree.column("Guardian Email", anchor=W, width=200)
    # create headings
        for column in tree["columns"]:
            tree.heading(column, command=lambda c=column: self.sort_treeview(tree,c))
    # insert data rows
        for entry in self.data_list:
            tree.insert("", "end", values=entry)
    # configure the grids weight to resize the treeview properly
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
if __name__ == "__main__":
    search_app = search_information()