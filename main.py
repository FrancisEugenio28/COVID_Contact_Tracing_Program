from tkinter import *
# import all the class
from COVID_Contact_Tracing_Program import registration
from Search_Information import search_information

class main_menu:
    def __init__(self):
        # create a simple GUI for main menu
        self.main_menu = Tk()
        self.main_menu.title("CONTACT TRACING 2023-2024")
        self.main_menu.geometry("550x270")
        # header
        head_frame = Frame(main_menu, bd=2, relief="groove", bg="#e12c2c")
        head_frame.place(x=5, y=5, width=540, height=60)
        head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#e12c2c", fg="white")
        head_label.pack(pady=10)
        # padding
        padding_frame = Frame(main_menu, bd=2, relief="groove")
        padding_frame.place(x=5, y=70, width=540, height=195)
        # create a button for registration
        register_btn = Button(main_menu, text="REGISTER",width="30", bg="maroon", fg="white", activebackground="#d598a3",font=("Helvetica", 10, "bold"), command=self.call_register)
        register_btn.place(x=155,y=100)
        # create a button for search information
        search_btn = Button(main_menu, text="SEARCH",width="30", bg="maroon", fg="white", activebackground="#d598a3",font=("Helvetica", 10, "bold"))
        search_btn.place(x=155,y=140)
    # call registration
    def call_register(self):
        gui_register = registration()
        gui_register()
    # call search information
    def call_search(self):
        gui_search = search_information()
        gui_search()
    # run main menu class
        self.main_menu.mainloop()
        run_program = main_menu()
        run_program()