from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, main):
        self.main = main
        self.T_Frame = Frame(self.main, height=50, width=1200, background="purple", bd=2, relief="groove")
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200, bg="purple")
        self.Title.pack()

        self.Frame_1 = Frame(self.main, height=580, width=400, bd=2, relief=GROOVE, bg="purple")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1, text="Student Details", background="purple", font="arial 12 bold").place(x=20, y=20)

        self.ID = Label(self.Frame_1, text="ID:", font="arial 12 bold", bg="purple")
        self.ID.place(x=40, y=60)
        self.ID_Entry = Entry(self.Frame_1, width=40)
        self.ID_Entry.place(x=150, y=60)

        self.Name = Label(self.Frame_1, text="Name:", font="arial 12 bold", bg="purple")
        self.Name.place(x=40, y=100)
        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)

        self.Age = Label(self.Frame_1, text="Age:", font="arial 12 bold", bg="purple")
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB:", font="arial 12 bold", bg="purple")
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="Gender:", font="arial 12 bold", bg="purple")
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)

        self.city = Label(self.Frame_1, text="City:", font="arial 12 bold", bg="purple")
        self.city.place(x=40, y=260)
        self.city_Entry = Entry(self.Frame_1, width=40)
        self.city_Entry.place(x=150, y=260)

        # ===================================BUTTON=====================================
        self.Button_Frame = Frame(self.Frame_1, height=250, width=250, relief=GROOVE, bd=2, background="purple")
        self.Button_Frame.place(x=80, y=350)

        self.Add_Button = Button(self.Button_Frame, text="Add", font="arial 15 bold", width=25, command=self.Add)
        self.Add_Button.pack()

        self.Delete_Button = Button(self.Button_Frame, text="Delete", font="arial 15 bold", width=25, command=self.delete)
        self.Delete_Button.pack()

        self.Update_Button = Button(self.Button_Frame, text="Update", font="arial 15 bold", width=25, command=self.Update)
        self.Update_Button.pack()

        self.Clear_Button = Button(self.Button_Frame, text="Clear", font="arial 15 bold", width=25, command=self.clear)
        self.Clear_Button.pack()

        self.Frame_2 = Frame(self.main, height=580, width=800, bd=2, relief=GROOVE, bg="Purple")
        self.Frame_2.pack(side=RIGHT)

        self.tree = ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=25)
        self.tree.pack()

        self.tree.column("#1", anchor=CENTER, width=40)
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="Age")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="City")

        self.tree.insert("", index=0, values=(1, "anu", "19-10-1998", 24, "female", "kerala"))
        self.tree.pack()

    def Add(self):
        ID = self.ID_Entry.get()
        name = self.Name_Entry.get()
        dob = self.DOB_Entry.get()
        age = self.Age_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.city_Entry.get()
        self.tree.insert("", index=0, values=(ID, name, dob, age, gender, city))

    def delete(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)

    def Update(self):
        ID = self.ID_Entry.get()
        name = self.Name_Entry.get()
        dob = self.DOB_Entry.get()
        age = self.Age_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.city_Entry.get()
        selected_item = self.tree.selection()[0]
        self.tree.item(selected_item, values=(ID, name, dob, age, gender, city))

    def clear(self):
        self.ID_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.city_Entry.delete(0, END)

main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

Student(main)
main.mainloop()
