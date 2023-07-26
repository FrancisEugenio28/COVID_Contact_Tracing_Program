from tkinter import *
from tkinter import ttk

# create a class 
# create a GUI for seach
search_gui = Tk()
search_gui.title("Search Your Entry")
search_gui.geometry('550x250')

# Set the width of the head_frame to the width of the search_gui
head_frame = Frame(search_gui, bd=2, relief="groove", bg="#FF0000")  # Stylish red color
head_frame.place(x=5, y=5, width=540, height=60)  # Updated width to 390
head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
head_label.pack(pady=10)

padding_frame = Frame(search_gui, bd=2, relief="groove")
padding_frame.place(x=5, y=70, width=540, height=170)

referencenum_label = Label(search_gui, text="PLEASE ENTER YOUR REFERENCE NUMBER: ")
referencenum_label.place(x=15,y=100)
referencenum_entry = Entry(search_gui, width='35')
referencenum_entry.place(x=255,y=100)

# create a forget button for those who forget their reference number
forget_text = Label(search_gui, text='Note: in case you forgot your own reference number please click "Forgot Reference Number"\r for other ways of searching your inforamtion')
forget_text.place(x=25,y=130)
forget_btn = Button(search_gui, text='Forgot Reference Number')
forget_btn.place(x=190,y=175)

# create a button for search
search_btn = Button(search_gui, text='Search')
search_btn.place(x=480,y=97)
# add function for each entry
# read the csv for possible entry
# display the entry 
search_gui.mainloop()
