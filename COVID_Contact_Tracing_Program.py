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
    contnum_label = Label(Contact_tracing, text= "CONTACT NUMBER : ")
    contnum_label.place(x=10, y=170)
    contnum_entry = Entry(Contact_tracing,width="51")
    contnum_entry.place(x=145, y=170)
    # Input Email
    email_label = Label(Contact_tracing, text= "E-MAIL : ")
    email_label.place(x=10, y=200)
    email_entry = Entry(Contact_tracing,width="62")
    email_entry.place(x=80, y=200)
    # create a padding for asking users for their contact history
    tracing_frame = Frame(Contact_tracing, bd=2, relief="groove")
    tracing_frame.place(x=5, y=250, width=490, height=185)
    tracing_label = Label(Contact_tracing,text = "CONTACT TRACING")
    tracing_label.place(x=15, y=240)
    # Ask the user if they are vaccinated
    vacstatus_label = Label(Contact_tracing, text= "VACCINE STATUS : ")
    vacstatus_label.place(x=10, y=265)
    vacstatus_entry = ttk.Combobox(Contact_tracing, width="50",values=["None", "First Dose", "Second Dose (Fully Vaccinated)", "First Booster Shot", "Second Booster Shot"])
    vacstatus_entry.place(x=120,y=265)
    # Ask the users if they experience any symptoms of the disease for the past weeks
    symptoms_label = Label(Contact_tracing, text="HAVE YOU EXPERIENCE THESE SYPMTOMS FOR PAST 7 DAYS?")
    symptoms_label.place(x=10,y=295)
    # create checkbutton for each symptoms
    # fever
    fever_btn = Checkbutton(Contact_tracing, text="Fever") 
    fever_btn.place(x=10,y=315)
    # cough
    cough_btn = Checkbutton(Contact_tracing, text="Cough") 
    cough_btn.place(x=10,y=335)
    # colds
    cold_btn = Checkbutton(Contact_tracing, text="Colds") 
    cold_btn.place(x=10,y=355)
    # Body pains
    bodypain_btn = Checkbutton(Contact_tracing, text="Body Pain") 
    bodypain_btn.place(x=110,y=315)
    # sore throat
    sorethroat_btn = Checkbutton(Contact_tracing, text="Sore Throat") 
    sorethroat_btn.place(x=110,y=335)
    # diarrhea
    diarrhea_btn = Checkbutton(Contact_tracing, text="Diarrhea") 
    diarrhea_btn.place(x=110,y=355)
    # headache
    headache_btn = Checkbutton(Contact_tracing, text="Headache") 
    headache_btn.place(x=210,y=315)
    # shortness of breath
    shortbreath_btn = Checkbutton(Contact_tracing, text="Shortness of Breath") 
    shortbreath_btn.place(x=210,y=335)
    # difficulty of breathing
    diffbreath_btn = Checkbutton(Contact_tracing, text="Difficulty of Breathing") 
    diffbreath_btn.place(x=210,y=355)
    # loss of taste
    ltaste_btn = Checkbutton(Contact_tracing, text="Loss of Taste") 
    ltaste_btn.place(x=10,y=375)
    # loss of smell
    lsmell_btn = Checkbutton(Contact_tracing, text="Loss of Smell") 
    lsmell_btn.place(x=110,y=375)
    # none of the above
    none_btn = Checkbutton(Contact_tracing, text="None of the Above") 
    none_btn.place(x=210,y=375)
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