from tkinter import *
from tkinter import ttk
# Create a simple GUI for COVID contract tracing
Contact_tracing = Tk()
Contact_tracing.title("COVID-19 Contact Tracing")
Contact_tracing.geometry("500x500")
# Make a simple program wherein the user will able to input all the information
def Gui_display():
    # create a padding for personal information
    personalinfo_frame = Frame(Contact_tracing, bd=2, relief="groove")
    personalinfo_frame.place(x=5, y=50, width=490, height=185)
    personalinfo_label = Label(Contact_tracing,text = "PERSONAL INFORMATION")
    personalinfo_label.place(x=15, y=40)
    # Input name
    name_label = Label(Contact_tracing,text = "NAME : ")
    name_label.place(x=10, y=70)
    name_entry = Entry(Contact_tracing,width="30") 
    name_entry.place(x=70,y=70)
    # Suffix
    suffix_label = Label(Contact_tracing, text= "SUFFIX : ")
    suffix_label.place(x=275,y=70)
    suffix_entry = Entry(Contact_tracing,width="18")
    suffix_entry.place(x=340,y=70)
    # Input age
    age_label = Label(Contact_tracing, text= "AGE : ")
    age_label.place(x=10, y=110)
    age_entry = Scale(Contact_tracing, from_=1, to=100, length="385",orient="horizontal")
    age_entry.place(x=65,y=90)
    # Input Address
    address_label = Label(Contact_tracing, text= "ADDRESS : ")
    address_label.place(x=10, y=140)
    address_entry = Entry(Contact_tracing,width="60") 
    address_entry.place(x=90,y=140)
    # Input Phone number
    phonenum_label = Label(Contact_tracing, text= "PHONE NUMBER : ")
    phonenum_label.place(x=10, y=170)
    phonenum_entry = Entry(Contact_tracing,width="55")
    phonenum_entry.place(x=120, y=170)
    # Input Email
    email_label = Label(Contact_tracing, text= "E-MAIL : ")
    email_label.place(x=10, y=200)
    email_entry = Entry(Contact_tracing,width="62")
    email_entry.place(x=80, y=200)
    # Ask the user if they are vaccinated
    # Ask the users if they experience any symptoms of the disease for the past weeks
    # Ask the users if they been with a person with possible symptoms
        #(PARENT OR GUARDIAN INFORMATION)
        # Input name
        # Input Relationship to the Guardian/Parent
    # create a submit button 
# collect all the data
    # create a data base 
    # print all the data into a txt file 
    # store it in the data base
# add a feature wherein the user may search for all the entries 
Gui_display()
Contact_tracing.mainloop()