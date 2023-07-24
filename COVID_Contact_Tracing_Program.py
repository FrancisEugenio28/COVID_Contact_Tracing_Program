from tkinter import *
from tkinter import ttk
# Create a simple GUI for COVID contract tracing
Contact_tracing = Tk()
Contact_tracing.title("COVID-19 Contact Tracing")
Contact_tracing.geometry("515x500")
radio = IntVar()
# scrolling feature
# creatte a main frame
main_frame = Frame(Contact_tracing)
main_frame.pack(fill=BOTH, expand=1)
# create a canvas 
frame_canvas = Canvas(main_frame)
frame_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add a scrollbar to the canvas
frame_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=frame_canvas.yview)
frame_canvas.pack(side=RIGHT, fill=Y)

# configure the canvas
frame_canvas.configure(yscrollcommand=frame_scrollbar.set)
frame_canvas.bind('<Configure>', lambda e: frame_canvas.configure(scrollregion=frame_canvas.bbox("all")))

# create another frame inside the canvas
second_frame = Frame(frame_canvas)

# add the new frame to a window in a canvas 
frame_canvas.create_window((0,0), window=second_frame, anchor="nw")
# Make a simple program wherein the user will able to input all the information
def Gui_display():
    # create a padding for personal information
    personalinfo_label = Label(second_frame,text = "PERSONAL INFORMATION")
    personalinfo_label.place(x=15, y=40)
    # Input name
    name_label = Label(second_frame,text = "NAME : ")
    name_label.place(x=10, y=70)
    name_entry = Entry(second_frame,width="30") 
    name_entry.place(x=70,y=70)
    # Suffix
    suffix_label = Label(second_frame, text= "SUFFIX : ")
    suffix_label.place(x=275,y=70)
    suffix_entry = Entry(second_frame,width="18")
    suffix_entry.place(x=340,y=70)
    # Input age
    age_label = Label(second_frame, text= "AGE : ")
    age_label.place(x=10, y=110)
    age_entry = Scale(second_frame, from_=1, to=100, length="385",orient="horizontal")
    age_entry.place(x=65,y=90)
    # Input Address
    address_label = Label(second_frame, text= "ADDRESS : ")
    address_label.place(x=10, y=140)
    address_entry = Entry(second_frame,width="60") 
    address_entry.place(x=90,y=140)
    # Input Phone number
    contnum_label = Label(second_frame, text= "CONTACT NUMBER : ")
    contnum_label.place(x=10, y=170)
    contnum_entry = Entry(second_frame,width="51")
    contnum_entry.place(x=145, y=170)
    # Input Email
    email_label = Label(second_frame, text= "E-MAIL : ")
    email_label.place(x=10, y=200)
    email_entry = Entry(second_frame,width="62")
    email_entry.place(x=80, y=200)
    # create a padding for asking users for their contact history
    tracing_label = Label(second_frame,text = "CONTACT TRACING")
    tracing_label.place(x=15, y=240)
    # Ask the user if they are vaccinated
    vacstatus_label = Label(second_frame, text= "VACCINE STATUS : ")
    vacstatus_label.place(x=10, y=265)
    vacstatus_entry = ttk.Combobox(second_frame, width="50",values=["None", "First Dose", "Second Dose (Fully Vaccinated)", "First Booster Shot", "Second Booster Shot"])
    vacstatus_entry.place(x=120,y=265)
    # Ask the users if they experience any symptoms of the disease for the past weeks
    symptoms_label = Label(second_frame, text="HAVE YOU EXPERIENCE THESE SYPMTOMS FOR PAST 7 DAYS?")
    symptoms_label.place(x=10,y=295)
    # create checkbutton for each symptoms
    # fever
    fever_btn = Checkbutton(second_frame, text="Fever") 
    fever_btn.place(x=10,y=315)
    # cough
    cough_btn = Checkbutton(second_frame, text="Cough") 
    cough_btn.place(x=10,y=335)
    # colds
    cold_btn = Checkbutton(second_frame, text="Colds") 
    cold_btn.place(x=10,y=355)
    # Body pains
    bodypain_btn = Checkbutton(second_frame, text="Body Pain") 
    bodypain_btn.place(x=110,y=315)
    # sore throat
    sorethroat_btn = Checkbutton(second_frame, text="Sore Throat") 
    sorethroat_btn.place(x=110,y=335)
    # diarrhea
    diarrhea_btn = Checkbutton(second_frame, text="Diarrhea") 
    diarrhea_btn.place(x=110,y=355)
    # headache
    headache_btn = Checkbutton(second_frame, text="Headache") 
    headache_btn.place(x=210,y=315)
    # shortness of breath
    shortbreath_btn = Checkbutton(second_frame, text="Shortness of Breath") 
    shortbreath_btn.place(x=210,y=335)
    # difficulty of breathing
    diffbreath_btn = Checkbutton(second_frame, text="Difficulty of Breathing") 
    diffbreath_btn.place(x=210,y=355)
    # loss of taste
    ltaste_btn = Checkbutton(second_frame, text="Loss of Taste") 
    ltaste_btn.place(x=10,y=375)
    # loss of smell
    lsmell_btn = Checkbutton(second_frame, text="Loss of Smell") 
    lsmell_btn.place(x=110,y=375)
    # none of the above
    none_btn = Checkbutton(second_frame, text="None of the Above") 
    none_btn.place(x=210,y=375)
    # Ask the users if they been with a person with possible symptoms
    exposure_label = Label(second_frame, text="HAVE YOU HAD EXPOSURE TO A PROBABLE OR CONFIRMED CASE IN LAST 14 DAYS?")
    exposure_label.place(x=10,y=405)
    # create radiobutton for yes and no option
    # yes
    yes_btn = Radiobutton(second_frame, text="YES",variable=radio,value="1") 
    yes_btn.place(x=10,y=425)
    # no
    no_btn = Radiobutton(second_frame, text="NO",variable=radio,value="2") 
    no_btn.place(x=10,y=445)
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
main_frame.mainloop()