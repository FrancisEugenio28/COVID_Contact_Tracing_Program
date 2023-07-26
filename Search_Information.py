from tkinter import *
from tkinter import ttk

# create a class 
# create a GUI for seach
search_gui = Tk()
search_gui.title("Search Your Entry")
search_gui.geometry('500x250')

# Set the width of the head_frame to the width of the search_gui
head_frame = Frame(search_gui, bd=2, relief="groove", bg="#FF0000")  # Stylish red color
head_frame.place(x=5, y=5, width=490, height=60)  # Updated width to 390
head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
head_label.pack(pady=10)

padding_frame = Frame(search_gui, bd=2, relief="groove")
padding_frame.place(x=5, y=70, width=490, height=170)

referencenum_label = Label(search_gui, text="PLEASE ENTER YOUR REFERENCE NUMBER: ")
referencenum_label.place(x=15,y=100)
referencenum_entry = Entry(search_gui, width='35')
referencenum_entry.place(x=255,y=100)


# add function for each entry
# read the csv for possible entry
# display the entry 
search_gui.mainloop()
