from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

# Make a simple programself. wherein the user will able to input all the information
class registration:
    def __init__(self):
        # Create a simple GUI for COVID contract tracing
        self.Contact_tracing = Tk()
        self.Contact_tracing.title("COVID-19 Contact Tracing")
        self.Contact_tracing.geometry("850x590")
        self.radio = IntVar()
        # create a padding for header
        self.head_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.head_frame.place(x=5, y=5, width=835, height=100)
        self.head_label = Label(self.Contact_tracing, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"))
        self.head_label.pack(pady=10)
        # create a padding for personal information
        self.personalinfo_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.personalinfo_frame.place(x=5, y=50, width=835, height=185)
        self.personalinfo_label = Label(self.Contact_tracing,text = "PERSONAL INFORMATION")
        self.personalinfo_label.place(x=15, y=40)
        # Input last name
        lastname_label = Label(self.Contact_tracing,text = "LAST NAME : ")
        lastname_label.place(x=10, y=70)
        self.lastname_entry = Entry(self.Contact_tracing,width="28") 
        self.lastname_entry.place(x=90,y=70)
        # input middle name
        middlename_label = Label(self.Contact_tracing, text= "MIDDLE NAME : ")
        middlename_label.place(x=275,y=70)
        self.middlename_entry = Entry(self.Contact_tracing,width="28")
        self.middlename_entry.place(x=370,y=70)
        # input first name
        firstname_label = Label(self.Contact_tracing,text = "FIRST NAME : ")
        firstname_label.place(x=560, y=70)
        self.firstname_entry = Entry(self.Contact_tracing,width="28") 
        self.firstname_entry.place(x=640,y=70)
        # Input age
        age_label = Label(self.Contact_tracing, text= "AGE : ")
        age_label.place(x=10, y=110)
        self.age_entry = Scale(self.Contact_tracing, from_=1, to=100, length="748",orient="horizontal")
        self.age_entry.place(x=65,y=90)
        # Input Address
        address_label = Label(self.Contact_tracing, text= "ADDRESS : ")
        address_label.place(x=10, y=140)
        self.address_entry = Entry(self.Contact_tracing,width="120") 
        self.address_entry.place(x=90,y=140)
        # Input Phone number
        contnum_label = Label(self.Contact_tracing, text= "CONTACT NUMBER : ")
        contnum_label.place(x=10, y=170)
        self.contnum_entry = Entry(self.Contact_tracing,width="55")
        self.contnum_entry.place(x=135, y=170)
        # input gender
        gender_label = Label(self.Contact_tracing, text= "GENDER : ")
        gender_label.place(x=485, y=170)
        self.gender_entry = ttk.Combobox(self.Contact_tracing, width="40",values=["Prefer Not to Say", "Male", "Female", "LGBTQ+", "Other"])
        self.gender_entry.place(x=550,y=170)
        # Input Email
        email_label = Label(self.Contact_tracing, text= "E-MAIL : ")
        email_label.place(x=10, y=200)
        self.email_entry = Entry(self.Contact_tracing,width="122")
        self.email_entry.place(x=80, y=200)
        # create a padding for asking users for their contact history
        self.tracing_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.tracing_frame.place(x=5, y=250, width=835, height=160)
        self.tracing_label = Label(self.Contact_tracing,text = "CONTACT TRACING")
        self.tracing_label.place(x=15, y=240)
        # Ask the user if they are vaccinated
        vacstatus_label = Label(self.Contact_tracing, text= "VACCINE STATUS : ")
        vacstatus_label.place(x=10, y=265)
        self.vacstatus_entry = ttk.Combobox(self.Contact_tracing, width="112",values=["None", "First Dose", "Second Dose (Fully Vaccinated)", "First Booster Shot", "Second Booster Shot"])
        self.vacstatus_entry.place(x=120,y=265)
        # Ask the users if they experience any symptoms of the disease for the past weeks
        symptoms_label = Label(self.Contact_tracing, text="HAVE YOU EXPERIENCE THESE SYPMTOMS FOR PAST 7 DAYS?")
        symptoms_label.place(x=10,y=295)
        # create checkbutton for each symptoms
        # fever
        self.fever_btn = Checkbutton(self.Contact_tracing, text="Fever") 
        self.fever_btn.place(x=10,y=315)
        # cough
        self.cough_btn = Checkbutton(self.Contact_tracing, text="Cough") 
        self.cough_btn.place(x=10,y=335)
        # colds
        self.cold_btn = Checkbutton(self.Contact_tracing, text="Colds") 
        self.cold_btn.place(x=10,y=355)
        # Body pains
        self.bodypain_btn = Checkbutton(self.Contact_tracing, text="Body Pain") 
        self.bodypain_btn.place(x=110,y=315)
        # sore throat
        self.sorethroat_btn = Checkbutton(self.Contact_tracing, text="Sore Throat") 
        self.sorethroat_btn.place(x=110,y=335)
        # diarrhea
        self.diarrhea_btn = Checkbutton(self.Contact_tracing, text="Diarrhea") 
        self.diarrhea_btn.place(x=110,y=355)
        # headache
        self.headache_btn = Checkbutton(self.Contact_tracing, text="Headache") 
        self.headache_btn.place(x=210,y=315)
        # shortness of breath
        self.shortbreath_btn = Checkbutton(self.Contact_tracing, text="Shortness of Breath") 
        self.shortbreath_btn.place(x=210,y=335)
        # difficulty of breathing
        self.diffbreath_btn = Checkbutton(self.Contact_tracing, text="Difficulty of Breathing") 
        self.diffbreath_btn.place(x=210,y=355)
        # loss of taste
        self.ltaste_btn = Checkbutton(self.Contact_tracing, text="Loss of Taste") 
        self.ltaste_btn.place(x=10,y=375)
        # loss of smell
        self.lsmell_btn = Checkbutton(self.Contact_tracing, text="Loss of Smell") 
        self.lsmell_btn.place(x=110,y=375)
        # none of the above
        self.none_btn = Checkbutton(self.Contact_tracing, text="None of the Above") 
        self.none_btn.place(x=210,y=375)
        # Ask the users if they been with a person with possible symptoms
        exposure_label = Label(self.Contact_tracing, text="HAVE YOU HAD EXPOSURE TO A PROBABLE OR CONFIRMED CASE IN LAST 14 DAYS?")
        exposure_label.place(x=370,y=295)
        # create radiobutton for yes and no option
        # yes
        self.yes_btn = Radiobutton(self.Contact_tracing, text="YES",variable=self.radio,value="1") 
        self.yes_btn.place(x=390,y=315)
        # no
        self.no_btn = Radiobutton(self.Contact_tracing, text="NO",variable=self.radio,value="2") 
        self.no_btn.place(x=390,y=335)
        #(PARENT OR GUARDIAN INFORMATION)
        self.parentinfo_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.parentinfo_frame.place(x=5, y=425, width=835, height=80)
        self.parentinfo_label = Label(self.Contact_tracing,text = "PARENT / GUARDIAN INFORMATION")
        self.parentinfo_label.place(x=15, y=415)
        # Input name
        # input last name
        parent_lastname_label = Label(self.Contact_tracing,text = "LAST NAME : ")
        parent_lastname_label.place(x=10, y=440)
        self.parent_lastname_entry = Entry(self.Contact_tracing,width="28") 
        self.parent_lastname_entry.place(x=90,y=440)
        # input first name
        parent_firstname_label = Label(self.Contact_tracing,text = "FIRST NAME : ")
        parent_firstname_label.place(x=275, y=440)
        self.parent_firstname_entry = Entry(self.Contact_tracing,width="28") 
        self.parent_firstname_entry.place(x=370,y=440)
        # Input Relationship to the Guardian/Parent
        relationship_label = Label(self.Contact_tracing, text= "RELATIONSHIP : ")
        relationship_label.place(x=560, y=440)
        self.relationship_entry = ttk.Combobox(self.Contact_tracing, width="20",values=["Mother", "Father", "Step-Mother", "Step-Father", "Auntie", "Uncle", "Sister", "Brother"])
        self.relationship_entry.place(x=655,y=440)
        # contact number
        parent_contnum_label = Label(self.Contact_tracing, text= "CONTACT NUMBER : ")
        parent_contnum_label.place(x=10, y=470)
        self.parent_contnum_entry = Entry(self.Contact_tracing,width="40")
        self.parent_contnum_entry.place(x=135, y=470)
        # email 
        parent_email_label = Label(self.Contact_tracing, text= "E-MAIL : ")
        parent_email_label.place(x=390, y=470)
        self.parent_email_entry = Entry(self.Contact_tracing,width="58")
        self.parent_email_entry.place(x=450, y=470)
        # add a statement assuring that all the data submitted will be confidential and will be protected.
        agreement_label = Label(self.Contact_tracing,text = "You can be sure that any information you give will be handled with the highest level of confidentiality and won't be shared with any third party.")
        agreement_label.place(x=40, y=510)
        self.agreement_btn = Checkbutton(self.Contact_tracing, text="I AGREE") 
        self.agreement_btn.place(x=360,y=530)
        # create a submit button 
        self.submit_btn = Button(self.Contact_tracing, text="SUBMIT", command= self.collect_data )
        self.submit_btn.place(x=365, y=555)
        # mainloop
        self.Contact_tracing.mainloop()
    # collect all the data
    def collect_data(self):
        last_name = self.lastname_entry.get()
        middle_name = self.middlename_entry.get()
        first_name = self.firstname_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        contact_num = self.contnum_entry.get()
        gender = self.gender_entry.get()
        email = self.email_entry.get()
        vacination_status = self.vacstatus_entry.get()
        fever = self.fever_btn.getboolean()
        cough = self.cough_btn.getboolean()
        cold = self.cold_btn.getboolean()
        body_pain = self.bodypain_btn.getboolean()
        sore_throat = self.sorethroat_btn.getboolean()
        diarrhea = self.diarrhea_btn.getboolean()
        headache = self.headache_btn.getboolean()
        short_breath = self.shortbreath_btn.getboolean()
        diff_breath = self.diffbreath_btn.getboolean()
        loss_taste = self.ltaste_btn.getboolean()
        loss_smell = self.lsmell_btn.getboolean()
        none = self.none_btn.getboolean()
        yes = self.yes_btn.getboolean()
        no = self.no_btn.getboolean()
        guardian_last_name = self.parent_lastname_entry.get()
        guardian_first_name = self.parent_firstname_entry.get()
        guardian_relationship = self.relationship_entry.get()
        guardian_contact_num = self.parent_contnum_entry.get()
        guardian_email = self.parent_email_entry.get()
        agreement = self.agreement_btn.getboolean()
        if not agreement:
            messagebox.showwarning("Agreement Required", "Please check the agreement box before submitting.")
            return
        if not last_name or not middle_name or not first_name or not age or not address or not contact_num or not gender or not email or not vacination_status or not fever or not cough or not cold or not body_pain or not sore_throat or not diarrhea or not headache or not short_breath or not diff_breath or not loss_smell or not loss_taste or not none or not yes or not no or not guardian_last_name or not guardian_first_name or not guardian_relationship or not guardian_contact_num or not guardian_email:
            messagebox.showwarning("Please fill up all the Entries.")
            return
        # create a data base 
        # Create a list of collected data
        data = [
            last_name,
            middle_name,
            first_name,
            age,
            address,
            contact_num,
            gender,
            email,
            vacination_status,
            fever,
            cough,
            cold,
            body_pain,
            sore_throat,
            diarrhea,
            headache,
            short_breath,
            diff_breath,
            loss_taste,
            loss_smell,
            none,
            yes,
            no,
            guardian_last_name,
            guardian_first_name,
            guardian_relationship,
            guardian_contact_num,
            guardian_email
        ]

        # Write data to CSV file
        with open('contact_tracing_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        # Show a success message after storing the data
        messagebox.showinfo("Data Saved", "Your data has been saved successfully!")
        # print all the data into a txt file 
        # store it in the data base

        