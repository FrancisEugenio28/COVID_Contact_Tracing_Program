from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import random

# Make a simple programself. wherein the user will able to input all the information
class registration:
    def __init__(self):
        # Create a simple GUI for COVID contract tracing
        self.Contact_tracing = Tk()
        self.Contact_tracing.title("COVID-19 Contact Tracing")
        self.Contact_tracing.geometry("850x630")
        self.Contact_tracing.resizable(False, False)
        self.radio = IntVar()
        self.agreement_var = IntVar()
        self.fever_btn_var = IntVar()
        self.cough_btn_var = IntVar()
        self.cold_btn_var = IntVar()
        self.bodypain_btn_var = IntVar()
        self.sorethroat_btn_var = IntVar()
        self.diarrhea_btn_var = IntVar()
        self.headache_btn_var = IntVar()
        self.shortbreath_btn_var = IntVar()
        self.diffbreath_btn_var = IntVar()
        self.ltaste_btn_var = IntVar()
        self.lsmell_btn_var = IntVar()
        self.none_var = IntVar()
        # create a padding for header
        self.head_frame = Frame(self.Contact_tracing, bd=2, relief="groove", bg="#FF0000")  # Stylish red color
        self.head_frame.place(x=5, y=5, width=835, height=60)
        self.head_label = Label(self.head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
        self.head_label.pack(pady=10)
        # create a padding for personal information
        self.personalinfo_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.personalinfo_frame.place(x=5, y=80, width=835, height=185)
        self.personalinfo_label = Label(self.Contact_tracing,text = "PERSONAL INFORMATION")
        self.personalinfo_label.place(x=15, y=70)
        # Input last name
        lastname_label = Label(self.Contact_tracing,text = "LAST NAME : ")
        lastname_label.place(x=10, y=100)
        self.lastname_entry = Entry(self.Contact_tracing,width="28") 
        self.lastname_entry.place(x=90,y=100)
        # input middle name
        middlename_label = Label(self.Contact_tracing, text= "MIDDLE NAME : ")
        middlename_label.place(x=275,y=100)
        self.middlename_entry = Entry(self.Contact_tracing,width="28")
        self.middlename_entry.place(x=370,y=100)
        # input first name
        firstname_label = Label(self.Contact_tracing,text = "FIRST NAME : ")
        firstname_label.place(x=560, y=100)
        self.firstname_entry = Entry(self.Contact_tracing,width="28") 
        self.firstname_entry.place(x=640,y=100)
        # Input age
        age_label = Label(self.Contact_tracing, text= "AGE : ")
        age_label.place(x=10, y=140)
        self.age_entry = Scale(self.Contact_tracing, from_=1, to=100, length="748",orient="horizontal")
        self.age_entry.place(x=65,y=120)
        # Input Address
        address_label = Label(self.Contact_tracing, text= "ADDRESS : ")
        address_label.place(x=10, y=170)
        self.address_entry = Entry(self.Contact_tracing,width="120") 
        self.address_entry.place(x=90,y=170)
        # Input Phone number
        contnum_label = Label(self.Contact_tracing, text= "CONTACT NUMBER : ")
        contnum_label.place(x=10, y=200)
        self.contnum_entry = Entry(self.Contact_tracing,width="55")
        self.contnum_entry.place(x=135, y=200)
        # input gender
        gender_label = Label(self.Contact_tracing, text= "GENDER : ")
        gender_label.place(x=485, y=200)
        self.gender_entry = ttk.Combobox(self.Contact_tracing, width="40",values=["Prefer Not to Say", "Male", "Female", "LGBTQ+", "Other"])
        self.gender_entry.place(x=550,y=200)
        # Input Email
        email_label = Label(self.Contact_tracing, text= "E-MAIL : ")
        email_label.place(x=10, y=230)
        self.email_entry = Entry(self.Contact_tracing,width="122")
        self.email_entry.place(x=80, y=230)
        # create a padding for asking users for their contact history
        self.tracing_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.tracing_frame.place(x=5, y=280, width=835, height=160)
        self.tracing_label = Label(self.Contact_tracing,text = "CONTACT TRACING")
        self.tracing_label.place(x=15, y=270)
        # Ask the user if they are vaccinated
        vacstatus_label = Label(self.Contact_tracing, text= "VACCINE STATUS : ")
        vacstatus_label.place(x=10, y=295)
        self.vacstatus_entry = ttk.Combobox(self.Contact_tracing, width="112",values=["None", "First Dose", "Second Dose (Fully Vaccinated)", "First Booster Shot", "Second Booster Shot"])
        self.vacstatus_entry.place(x=120,y=295)
        # Ask the users if they experience any symptoms of the disease for the past weeks
        symptoms_label = Label(self.Contact_tracing, text="HAVE YOU EXPERIENCE THESE SYPMTOMS FOR PAST 7 DAYS?")
        symptoms_label.place(x=10,y=325)
        # create checkbutton for each symptoms
        # fever
        self.fever_btn = Checkbutton(self.Contact_tracing, text="Fever", variable=self.fever_btn_var) 
        self.fever_btn.place(x=10,y=345)
        # cough
        self.cough_btn = Checkbutton(self.Contact_tracing, text="Cough", variable=self.cough_btn_var) 
        self.cough_btn.place(x=10,y=365)
        # colds
        self.cold_btn = Checkbutton(self.Contact_tracing, text="Colds", variable=self.cold_btn_var) 
        self.cold_btn.place(x=10,y=385)
        # Body pains
        self.bodypain_btn = Checkbutton(self.Contact_tracing, text="Body Pain", variable=self.bodypain_btn_var) 
        self.bodypain_btn.place(x=110,y=345)
        # sore throat
        self.sorethroat_btn = Checkbutton(self.Contact_tracing, text="Sore Throat", variable=self.sorethroat_btn_var) 
        self.sorethroat_btn.place(x=110,y=365)
        # diarrhea
        self.diarrhea_btn = Checkbutton(self.Contact_tracing, text="Diarrhea", variable=self.diarrhea_btn_var) 
        self.diarrhea_btn.place(x=110,y=385)
        # headache
        self.headache_btn = Checkbutton(self.Contact_tracing, text="Headache", variable=self.headache_btn_var) 
        self.headache_btn.place(x=210,y=345)
        # shortness of breath
        self.shortbreath_btn = Checkbutton(self.Contact_tracing, text="Shortness of Breath", variable=self.shortbreath_btn_var) 
        self.shortbreath_btn.place(x=210,y=365)
        # difficulty of breathing
        self.diffbreath_btn = Checkbutton(self.Contact_tracing, text="Difficulty of Breathing", variable=self.diffbreath_btn_var) 
        self.diffbreath_btn.place(x=210,y=385)
        # loss of taste
        self.ltaste_btn = Checkbutton(self.Contact_tracing, text="Loss of Taste", variable=self.ltaste_btn_var) 
        self.ltaste_btn.place(x=10,y=405)
        # loss of smell
        self.lsmell_btn = Checkbutton(self.Contact_tracing, text="Loss of Smell", variable=self.lsmell_btn_var) 
        self.lsmell_btn.place(x=110,y=405)
        # none of the above
        self.none_btn = Checkbutton(self.Contact_tracing, text="None of the Above", variable=self.none_var)
        self.none_btn.place(x=210, y=405)
        # Ask the users if they been with a person with possible symptoms
        exposure_label = Label(self.Contact_tracing, text="HAVE YOU HAD EXPOSURE TO A PROBABLE OR CONFIRMED CASE IN LAST 14 DAYS?")
        exposure_label.place(x=370,y=325)
        # create radiobutton for yes and no option
        # yes
        self.yes_btn = Radiobutton(self.Contact_tracing, text="YES",variable=self.radio,value="1") 
        self.yes_btn.place(x=390,y=345)
        # no
        self.no_btn = Radiobutton(self.Contact_tracing, text="NO",variable=self.radio,value="2") 
        self.no_btn.place(x=390,y=365)
        #(PARENT OR GUARDIAN INFORMATION)
        self.parentinfo_frame = Frame(self.Contact_tracing, bd=2, relief="groove")
        self.parentinfo_frame.place(x=5, y=455, width=835, height=80)
        self.parentinfo_label = Label(self.Contact_tracing,text = "PARENT / GUARDIAN INFORMATION")
        self.parentinfo_label.place(x=15, y=445)
        # Input name
        # input last name
        parent_lastname_label = Label(self.Contact_tracing,text = "LAST NAME : ")
        parent_lastname_label.place(x=10, y=470)
        self.parent_lastname_entry = Entry(self.Contact_tracing,width="28") 
        self.parent_lastname_entry.place(x=90,y=470)
        # input first name
        parent_firstname_label = Label(self.Contact_tracing,text = "FIRST NAME : ")
        parent_firstname_label.place(x=275, y=470)
        self.parent_firstname_entry = Entry(self.Contact_tracing,width="28") 
        self.parent_firstname_entry.place(x=370,y=470)
        # Input Relationship to the Guardian/Parent
        relationship_label = Label(self.Contact_tracing, text= "RELATIONSHIP : ")
        relationship_label.place(x=560, y=470)
        self.relationship_entry = ttk.Combobox(self.Contact_tracing, width="20",values=["Mother", "Father", "Step-Mother", "Step-Father", "Auntie", "Uncle", "Sister", "Brother"])
        self.relationship_entry.place(x=655,y=470)
        # contact number
        parent_contnum_label = Label(self.Contact_tracing, text= "CONTACT NUMBER : ")
        parent_contnum_label.place(x=10, y=500)
        self.parent_contnum_entry = Entry(self.Contact_tracing,width="40")
        self.parent_contnum_entry.place(x=135, y=500)
        # email 
        parent_email_label = Label(self.Contact_tracing, text= "E-MAIL : ")
        parent_email_label.place(x=390, y=500)
        self.parent_email_entry = Entry(self.Contact_tracing,width="58")
        self.parent_email_entry.place(x=450, y=500)
        # add a statement assuring that all the data submitted will be confidential and will be protected.
        agreement_label = Label(self.Contact_tracing, text="You can be sure that any information you give will be handled with the highest level of confidentiality and won't be shared with any third party.")
        agreement_label.place(x=40, y=540)
        self.agreement_btn = Checkbutton(self.Contact_tracing, text="I AGREE", variable=self.agreement_var) 
        self.agreement_btn.place(x=360, y=560)
        # create a submit button 
        self.submit_btn = Button(self.Contact_tracing, text="SUBMIT", command= self.collect_data )
        self.submit_btn.place(x=365, y=595)
        # mainloop
        self.Contact_tracing.mainloop()

    # Function to generate a random referral number
    def generate_reference_number(self):
        return random.randint(100000, 999999)
    
    # collect all the data
    def collect_data(self):
        last_name = self.lastname_entry.get().upper()
        middle_name = self.middlename_entry.get().upper()
        first_name = self.firstname_entry.get().upper()
        age = self.age_entry.get()
        address = self.address_entry.get().upper()
        contact_num = self.contnum_entry.get()
        gender = self.gender_entry.get()
        email = self.email_entry.get().upper()
        vaccination_status = self.vacstatus_entry.get()
        guardian_last_name = self.parent_lastname_entry.get().upper()
        guardian_first_name = self.parent_firstname_entry.get().upper()
        guardian_relationship = self.relationship_entry.get()
        guardian_contact_num = self.parent_contnum_entry.get()
        guardian_email = self.parent_email_entry.get().upper()
        agreement = self.agreement_var.get() == 1

        # Get the value of the selected radio button (1 for YES, 2 for NO)
        exposure_value = self.radio.get()
        yes = True if exposure_value == 1 else False
        no = True if exposure_value == 2 else False

        # Create a dictionary to store the symptoms data
        symptoms_data = {
        "Fever": self.fever_btn_var.get(),
        "Cough": self.cough_btn_var.get(),
        "Colds": self.cold_btn_var.get(),
        "Body Pain": self.bodypain_btn_var.get(),
        "Sore Throat": self.sorethroat_btn_var.get(),
        "Diarrhea": self.diarrhea_btn_var.get(),
        "Headache": self.headache_btn_var.get(),
        "Shortness of Breath": self.shortbreath_btn_var.get(),
        "Difficulty of Breathing": self.diffbreath_btn_var.get(),
        "Loss of Taste": self.ltaste_btn_var.get(),
        "Loss of Smell": self.lsmell_btn_var.get(),
        "None of the Above": self.none_var.get()
    }

        # Generate a random referral number
        reference_number = self.generate_reference_number()
        
        if all(value == '' for value in symptoms_data.values()):
            messagebox.showwarning("Symptoms Not Selected", "Please select at least one symptom.")
            return
        
        if not agreement:
            messagebox.showwarning("Agreement Required", "Please check the agreement box before submitting.")
            return
        
        if not last_name or not middle_name or not first_name or not age or not address or not contact_num or not gender or not email or not vaccination_status or not guardian_last_name or not guardian_first_name or not guardian_relationship or not guardian_contact_num or not guardian_email:
            messagebox.showwarning("Please fill up all the Entries.")
            return

        # Create a list of collected data
        data = [
            reference_number, # we add a reference number for the data 
            last_name,
            middle_name,
            first_name,
            age,
            address,
            contact_num,
            gender,
            email,
            vaccination_status,
            symptoms_data,
            yes,
            no,
            guardian_last_name,
            guardian_first_name,
            guardian_relationship,
            guardian_contact_num,
            guardian_email
        ]

        # Check if a csv file exists
        file_checker = False
        try:
            with open("Data_List.csv", "r") as List:
                read = csv.reader(List)
                if any(read):
                    file_checker = True
        except FileNotFoundError:
            pass
        
        # Write data to CSV file
        with open('contact_tracing_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_checker:
                writer.writerow([
                    "Reference Number", 
                    "Last Name",
                    "Middle Name",
                    "First Name",
                    "Age",
                    "Address",
                    "Contact Number",
                    "Gender",
                    "Email",
                    "Vaccination Status",
                    "Symptoms",
                    "Exposure[yes]",
                    "Exposure[no]",
                    "Guardian Last Name",
                    "Guardian First Name",
                    "Guardian Relationship",
                    "Guardian Contact Number",
                    "Guardian Email"
                ])
            writer.writerow(data)

        # Show a success message after storing the data
        messagebox.showinfo("Data Saved", f"Your data has been saved successfully! Reference Number: {reference_number}")
        # Close the program
        self.Contact_tracing.destroy()
if __name__ == "__main__":
    run_program = registration()