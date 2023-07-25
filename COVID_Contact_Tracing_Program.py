from tkinter import *
from tkinter import ttk
# Create a simple GUI for COVID contract tracing
Contact_tracing = Tk()
Contact_tracing.title("COVID-19 Contact Tracing")
Contact_tracing.geometry("850x590")
radio = IntVar()
# Make a simple program wherein the user will able to input all the information
def Gui_display():
    # create a padding for header
    head_frame = Frame(Contact_tracing, bd=2, relief="groove")
    head_frame.place(x=5, y=5, width=835, height=100)
    head_label = Label(Contact_tracing, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"))
    head_label.pack(pady=10)
    # create a padding for personal information
    personalinfo_frame = Frame(Contact_tracing, bd=2, relief="groove")
    personalinfo_frame.place(x=5, y=50, width=835, height=185)
    personalinfo_label = Label(Contact_tracing,text = "PERSONAL INFORMATION")
    personalinfo_label.place(x=15, y=40)
    # Input last name
    lastname_label = Label(Contact_tracing,text = "LAST NAME : ")
    lastname_label.place(x=10, y=70)
    lastname_labelname_entry = Entry(Contact_tracing,width="28") 
    lastname_labelname_entry.place(x=90,y=70)
    # input middle name
    middlename_label = Label(Contact_tracing, text= "MIDDLE NAME : ")
    middlename_label.place(x=275,y=70)
    middlename_entry = Entry(Contact_tracing,width="28")
    middlename_entry.place(x=370,y=70)
    # input first name
    firstname_label = Label(Contact_tracing,text = "FIRST NAME : ")
    firstname_label.place(x=560, y=70)
    firstname_labelname_entry = Entry(Contact_tracing,width="28") 
    firstname_labelname_entry.place(x=640,y=70)
    # Input age
    age_label = Label(Contact_tracing, text= "AGE : ")
    age_label.place(x=10, y=110)
    age_entry = Scale(Contact_tracing, from_=1, to=100, length="748",orient="horizontal")
    age_entry.place(x=65,y=90)
    # Input Address
    address_label = Label(Contact_tracing, text= "ADDRESS : ")
    address_label.place(x=10, y=140)
    address_entry = Entry(Contact_tracing,width="120") 
    address_entry.place(x=90,y=140)
    # Input Phone number
    contnum_label = Label(Contact_tracing, text= "CONTACT NUMBER : ")
    contnum_label.place(x=10, y=170)
    contnum_entry = Entry(Contact_tracing,width="55")
    contnum_entry.place(x=135, y=170)
    # input gender
    gender_label = Label(Contact_tracing, text= "GENDER : ")
    gender_label.place(x=485, y=170)
    gender_entry = ttk.Combobox(Contact_tracing, width="40",values=["Prefer Not to Say", "Male", "Female", "LGBTQ+", "Other"])
    gender_entry.place(x=550,y=170)
    # Input Email
    email_label = Label(Contact_tracing, text= "E-MAIL : ")
    email_label.place(x=10, y=200)
    email_entry = Entry(Contact_tracing,width="122")
    email_entry.place(x=80, y=200)
    # create a padding for asking users for their contact history
    tracing_frame = Frame(Contact_tracing, bd=2, relief="groove")
    tracing_frame.place(x=5, y=250, width=835, height=160)
    tracing_label = Label(Contact_tracing,text = "CONTACT TRACING")
    tracing_label.place(x=15, y=240)
    # Ask the user if they are vaccinated
    vacstatus_label = Label(Contact_tracing, text= "VACCINE STATUS : ")
    vacstatus_label.place(x=10, y=265)
    vacstatus_entry = ttk.Combobox(Contact_tracing, width="112",values=["None", "First Dose", "Second Dose (Fully Vaccinated)", "First Booster Shot", "Second Booster Shot"])
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
    exposure_label = Label(Contact_tracing, text="HAVE YOU HAD EXPOSURE TO A PROBABLE OR CONFIRMED CASE IN LAST 14 DAYS?")
    exposure_label.place(x=370,y=295)
    # create radiobutton for yes and no option
    # yes
    yes_btn = Radiobutton(Contact_tracing, text="YES",variable=radio,value="1") 
    yes_btn.place(x=390,y=315)
    # no
    no_btn = Radiobutton(Contact_tracing, text="NO",variable=radio,value="2") 
    no_btn.place(x=390,y=335)
    #(PARENT OR GUARDIAN INFORMATION)
    parentinfo_frame = Frame(Contact_tracing, bd=2, relief="groove")
    parentinfo_frame.place(x=5, y=425, width=835, height=80)
    parentinfo_label = Label(Contact_tracing,text = "PARENT / GUARDIAN INFORMATION")
    parentinfo_label.place(x=15, y=415)
    # Input name
    # input last name
    parent_lastname_label = Label(Contact_tracing,text = "LAST NAME : ")
    parent_lastname_label.place(x=10, y=440)
    parent_lastname_labelname_entry = Entry(Contact_tracing,width="28") 
    parent_lastname_labelname_entry.place(x=90,y=440)
    # input first name
    parent_firstname_label = Label(Contact_tracing,text = "FIRST NAME : ")
    parent_firstname_label.place(x=275, y=440)
    parent_firstname_labelname_entry = Entry(Contact_tracing,width="28") 
    parent_firstname_labelname_entry.place(x=370,y=440)
    # Input Relationship to the Guardian/Parent
    relationship_label = Label(Contact_tracing, text= "RELATIONSHIP : ")
    relationship_label.place(x=560, y=440)
    relationship_entry = ttk.Combobox(Contact_tracing, width="20",values=["Mother", "Father", "Step-Mother", "Step-Father", "Auntie", "Uncle", "Sister", "Brother"])
    relationship_entry.place(x=655,y=440)
    # contact number
    parent_contnum_label = Label(Contact_tracing, text= "CONTACT NUMBER : ")
    parent_contnum_label.place(x=10, y=470)
    parent_contnum_entry = Entry(Contact_tracing,width="40")
    parent_contnum_entry.place(x=135, y=470)
    # email 
    parent_email_label = Label(Contact_tracing, text= "E-MAIL : ")
    parent_email_label.place(x=390, y=470)
    parent_email_entry = Entry(Contact_tracing,width="58")
    parent_email_entry.place(x=450, y=470)
    # add a statement assuring that all the data submitted will be confidential and will be protected.
    agreement_label = Label(Contact_tracing,text = "You can be sure that any information you give will be handled with the highest level of confidentiality and won't be shared with any third party.")
    agreement_label.place(x=40, y=510)
    agreement_btn = Checkbutton(Contact_tracing, text="I AGREE") 
    agreement_btn.place(x=360,y=530)
    # create a submit button 
    submit_btn = Button(Contact_tracing, text="SUBMIT", )
    submit_btn.place(x=365, y=555)
# collect all the data
    # create a data base 
    # print all the data into a txt file 
    # store it in the data base
# add a feature wherein the user may search for all the entries 
Gui_display()
Contact_tracing.mainloop()