from tkinter import *
# Create a simple GUI for COVID contract tracing
Contact_tracing = Tk()
Contact_tracing.title("COVID-19 Contact Tracing")
Contact_tracing.geometry("300x500")
# Make a simple program wherein the user will able to input all the information
# Input name
def Gui_display():
    name_label = Label(Contact_tracing,text = "NAME : ")
    name_label.place(x=10, y=70)
    name_entry = Entry(Contact_tracing,width="30") 
    name_entry.place(x=70,y=70)
    # Input age
    age_label = Label(Contact_tracing, text= "AGE : ")
    age_label.place(x=10, y=110)
    age_entry = Scale(Contact_tracing, from_=1, to=100, length="190",orient="horizontal")
    age_entry.place(x=65,y=90)
    # Input Address
    address_label = Label(Contact_tracing, text= "ADDRESS : ")
    address_label.place(x=10, y=140)
    # Input Phone number
    phone_num_label = Label(Contact_tracing, text= "PHONE NUMBER : ")
    phone_num_label.place(x=10, y=170)
    # Input Email
    email_label = Label(Contact_tracing, text= "E-MAIL : ")
    email_label.place(x=10, y=200)
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