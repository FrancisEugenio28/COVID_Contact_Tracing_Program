from tkinter import *
from tkinter import ttk


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
        self.forget_btn = Button(self.search_gui, text='Forgot Reference Number')
        self.forget_btn.place(x=190,y=175)

        # create a button for search
        self.search_btn = Button(self.search_gui, text='Search')
        self.search_btn.place(x=480,y=97)
# add function for each entry
# read the csv for possible entry
# display the entry 
        self.search_gui.mainloop()
