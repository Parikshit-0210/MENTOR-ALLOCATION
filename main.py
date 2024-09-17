import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from ALLOCATION import allocation,mentor,student
class AllocationApp(tk.Tk):
    def __init__(self, students_file, mentors_file):
        super().__init__()
        self.title("Mentor-Student Allocation System")
        self.geometry("800x600")  # Larger window size
        self.style = ttk.Style()
        self.style.configure('TButton', font=('calibri', 12, 'bold'), borderwidth='4', foreground='black', background='#ffff00')  # yellow button with black text
        self.style.configure('TLabel', font=('calibri', 14), background='#f0f0f0')
        self.style.configure('TEntry', font=('calibri', 14))

        self.configure(background='#ADD8E6')  # Light blue background

        self.students_file = students_file
        self.mentors_file = mentors_file
        self.allocation_system = allocation.Allocation(self.students_file, self.mentors_file)

        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(fill="both", expand=True)
        # Increase the size of the tab button
        self.style.configure('TNotebook.Tab', padding=[10, 5])
        self.style.configure('My.Yellow.TButton', font=('calibri', 12, 'bold'), borderwidth='4', foreground='black',
                             background='#ffff00')

        # Add a frame for the main menu
        self.main_frame = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.main_frame, text="Main Menu")

        # Add button to go to Add page
        self.add_button = ttk.Button(self.main_frame, text="Add", command=self.show_add_page, style='My.Yellow.TButton')
        self.add_button.pack(pady=10)

        # Add button to go to Delete page
        self.delete_button = ttk.Button(self.main_frame, text="Delete", command=self.show_delete_page,
                                        style='My.TButton')
        self.delete_button.pack(pady=10)
        # Adding the update button
        self.update_button = ttk.Button(self.main_frame, text="Update", command=self.show_update_page,
                                        style='My.TButton')
        self.update_button.pack(pady=10)
        # Add button to allocate
        self.allocate_button = ttk.Button(self.main_frame, text="Allocate", command=self.allocate, style='My.TButton')
        self.allocate_button.pack(pady=10)

        # Add the frames for Add and Delete pages
        self.add_frame = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.add_frame, text="Add Student/Mentor")

        self.delete_frame = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.delete_frame, text="Delete Student/Mentor")

        # Configure the style of the frames to light blue
        self.style.configure('My.TFrame', background='#ADD8E6')

        # Add student widgets
        ttk.Label(self.add_frame, text="Student ID:").pack(pady=5)
        self.add_student_id_entry = ttk.Entry(self.add_frame)
        self.add_student_id_entry.pack()

        ttk.Label(self.add_frame, text="Student Name:").pack(pady=5)
        self.add_student_name_entry = ttk.Entry(self.add_frame)
        self.add_student_name_entry.pack()

        ttk.Label(self.add_frame, text="Student Interest:").pack(pady=5)
        self.add_student_interest_entry = ttk.Entry(self.add_frame)
        self.add_student_interest_entry.pack()

        ttk.Button(self.add_frame, text="Add Student", command=self.add_student).pack(pady=10)

        # Add mentor widgets
        ttk.Label(self.add_frame, text="Mentor ID:").pack(pady=5)
        self.add_mentor_id_entry = ttk.Entry(self.add_frame)
        self.add_mentor_id_entry.pack()

        ttk.Label(self.add_frame, text="Mentor Name:").pack(pady=5)
        self.add_mentor_name_entry = ttk.Entry(self.add_frame)
        self.add_mentor_name_entry.pack()

        ttk.Label(self.add_frame, text="Mentor Expertise:").pack(pady=5)
        self.add_mentor_expertise_entry = ttk.Entry(self.add_frame)
        self.add_mentor_expertise_entry.pack()

        ttk.Button(self.add_frame, text="Add Mentor", command=self.add_mentor).pack(pady=10)

        # Delete student widgets
        ttk.Label(self.delete_frame, text="Student ID:").pack(pady=5)
        self.delete_student_id_entry = ttk.Entry(self.delete_frame)
        self.delete_student_id_entry.pack()

        ttk.Button(self.delete_frame, text="Delete Student", command=self.delete_student).pack(pady=10)

        # Delete mentor widgets
        ttk.Label(self.delete_frame, text="Mentor ID:").pack(pady=5)
        self.delete_mentor_id_entry = ttk.Entry(self.delete_frame)
        self.delete_mentor_id_entry.pack()

        ttk.Button(self.delete_frame, text="Delete Mentor", command=self.delete_mentor).pack(pady=10)

        self.update_frame = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.update_frame, text="Update Student/Mentor")

        # Update student widgets
        ttk.Label(self.update_frame, text="Student ID:").pack(pady=5)
        self.update_student_id_entry = ttk.Entry(self.update_frame)
        self.update_student_id_entry.pack()

        ttk.Label(self.update_frame, text="New Student Name:").pack(pady=5)
        self.update_student_name_entry = ttk.Entry(self.update_frame)
        self.update_student_name_entry.pack()

        ttk.Label(self.update_frame, text="New Student Interest:").pack(pady=5)
        self.update_student_interest_entry = ttk.Entry(self.update_frame)
        self.update_student_interest_entry.pack()

        ttk.Button(self.update_frame, text="Update Student", command=self.update_student).pack(pady=10)

        # Update mentor widgets
        ttk.Label(self.update_frame, text="Mentor ID:").pack(pady=5)
        self.update_mentor_id_entry = ttk.Entry(self.update_frame)
        self.update_mentor_id_entry.pack()

        ttk.Label(self.update_frame, text="New Mentor Name:").pack(pady=5)
        self.update_mentor_name_entry = ttk.Entry(self.update_frame)
        self.update_mentor_name_entry.pack()

        ttk.Label(self.update_frame, text="New Mentor Expertise:").pack(pady=5)
        self.update_mentor_expertise_entry = ttk.Entry(self.update_frame)
        self.update_mentor_expertise_entry.pack()

        ttk.Button(self.update_frame, text="Update Mentor", command=self.update_mentor).pack(pady=10)

    def update_student(self):
        student_id = self.update_student_id_entry.get()
        student_name = self.update_student_name_entry.get()
        student_interest = self.update_student_interest_entry.get()
        if student_id and student_name and student_interest:
            self.allocation_system.update_student(int(student_id), student_name, student_interest)
            messagebox.showinfo("Success", "Student updated successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def update_mentor(self):
        mentor_id = self.update_mentor_id_entry.get()
        mentor_name = self.update_mentor_name_entry.get()
        mentor_expertise = self.update_mentor_expertise_entry.get()
        if mentor_id and mentor_name and mentor_expertise:
            self.allocation_system.update_mentor(int(mentor_id), mentor_name, mentor_expertise)
            messagebox.showinfo("Success", "Mentor updated successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def show_add_page(self):
        self.tabControl.select(self.add_frame)

    def show_delete_page(self):
        self.tabControl.select(self.delete_frame)

    def show_update_page(self):
        self.tabControl.select(self.update_frame)
    def add_student(self):
        student_id = self.add_student_id_entry.get()
        student_name = self.add_student_name_entry.get()
        student_interest = self.add_student_interest_entry.get()
        if student_id and student_name and student_interest:
            self.allocation_system.add_student(student_id, student_name, student_interest)
            messagebox.showinfo("Success", "Student added successfully.")
            self.add_student_id_entry.delete(0, 'end')  # Clear the entry field
            self.add_student_name_entry.delete(0, 'end')  # Clear the entry field
            self.add_student_interest_entry.delete(0, 'end')  # Clear the entry field
        else:
            messagebox.showerror("Error", "All fields are required.")

    def add_mentor(self):
        mentor_id = self.add_mentor_id_entry.get()
        mentor_name = self.add_mentor_name_entry.get()
        mentor_expertise = self.add_mentor_expertise_entry.get()
        if mentor_id and mentor_name and mentor_expertise:
            self.allocation_system.add_mentor(mentor_id, mentor_name, mentor_expertise)
            messagebox.showinfo("Success", "Mentor added successfully.")
            self.add_mentor_id_entry.delete(0, 'end')  # Clear the entry field
            self.add_mentor_name_entry.delete(0, 'end')  # Clear the entry field
            self.add_mentor_expertise_entry.delete(0, 'end')  # Clear the entry field
        else:
            messagebox.showerror("Error", "All fields are required.")

    def delete_student(self):
        student_id = self.delete_student_id_entry.get()
        if student_id:
            self.allocation_system.delete_student(int(student_id))
            messagebox.showinfo("Success", "Student deleted successfully.")
            self.delete_student_id_entry.delete(0, 'end')  # Clear the entry field
        else:
            messagebox.showerror("Error", "Student ID is required.")

    def delete_mentor(self):
        mentor_id = self.delete_mentor_id_entry.get()
        if mentor_id:
            self.allocation_system.delete_mentor(int(mentor_id))
            messagebox.showinfo("Success", "Mentor deleted successfully.")
            self.delete_mentor_id_entry.delete(0, 'end')  # Clear the entry field
        else:
            messagebox.showerror("Error", "Mentor ID is required.")

    def allocate(self):
        self.allocation_system.allocate()
        self.display_allocation_graph()
        messagebox.showinfo("Success", "Allocation completed successfully.")

    def display_allocation_graph(self):
        allocation_graph = self.allocation_system.create_allocation_graph()

        student_ids = set()
        mentor_ids = set()

        for allocation in allocation_graph:
            student_ids.add(allocation[0])
            mentor_ids.add(allocation[1])

        plt.figure(figsize=(8, 6))
        pos = {}

        for i, student_id in enumerate(student_ids):
            pos[student_id] = (1, i)

        for i, mentor_id in enumerate(mentor_ids):
            pos[mentor_id] = (2, i)

        for allocation in allocation_graph:
            plt.plot([pos[allocation[0]][0], pos[allocation[1]][0]],
                     [pos[allocation[0]][1], pos[allocation[1]][1]], 'k-')

        for node, (x, y) in pos.items():
            plt.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

        plt.xticks([1, 2], ['Students', 'Mentors'])
        plt.yticks([])
        plt.title("Student-Mentor Allocation")
        plt.show()

if __name__ == "__main__":
    app = AllocationApp('students.csv', 'mentors.csv')
    app.mainloop()
