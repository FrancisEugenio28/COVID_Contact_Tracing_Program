from tkinter import *
# Create a simple GUI for COVID contract tracing
Contact_tracing = Tk()
Contact_tracing.title("COVID-19 Contact Tracing")
Contact_tracing.geometry("500x500")
# Make a simple program wherein the user will able to input all the information
# Input name
def Gui_display():
    name_input = Label(Contact_tracing,text = "Name : ")
    name_input.place(x=10, y=70)
    # Input age
    age_input = Label(Contact_tracing, text= "Age : ")
    age_input.place(x=10, y=100)
    # Input Address
    # Input Phone number
    # Input Email
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