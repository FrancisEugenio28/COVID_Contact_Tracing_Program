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
                    return
            messagebox.showinfo("Entry Not Found", "Your reference number is not listed in the data file.")
        else:
            messagebox.showwarning("Warning", "Please enter your reference number!")
        
    def show_data(self, tab):
    # function to display data in a new tab using a treeview widget
        tree_frame = Frame(tab)
        tree_frame.pack(fill="both", expand=True)

        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
        tree.pack(fill="both", expand=True)

        tree_scroll.config(command=tree.yview)
    # define columns for the treeview
    # format columns
    # create headings
    # insert data rows

if __name__ == "__main__":
    search_app = search_information()