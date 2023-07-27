from tkinter import *
# import all the class
from COVID_Contact_Tracing_Program import registration
from Search_Information import search_information
# create a simple GUI for main menu
main_menu = Tk()
main_menu.title("CONTACT TRACING 2023-2024")
main_menu.geometry("550x270")
# header
head_frame = Frame(main_menu, bd=2, relief="groove", bg="#FF0000")
head_frame.place(x=5, y=5, width=540, height=60)
head_label = Label(head_frame, text="CONTACT TRACING 2023-2024", font=("Helvetica", 20, "bold"), bg="#FF0000", fg="white")
head_label.pack(pady=10)
# padding
padding_frame = Frame(main_menu, bd=2, relief="groove")
padding_frame.place(x=5, y=70, width=540, height=195)
# create a button for registration
# create a button for search information
# run main menu class
main_menu.mainloop()