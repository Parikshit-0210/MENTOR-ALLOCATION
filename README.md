# MENTOR-ALLOCATION
This project is a **Mentor-Student Allocation System** developed using Python and the Tkinter library for the graphical user interface (GUI). It allows for the management of student and mentor data, facilitating the allocation of students to mentors based on their interests and expertise. Here’s an overview of the key components and functionality:

### Key Features:
1. **GUI Design**: 
   - Built using Tkinter with a clean, simple, and user-friendly interface. 
   - It has a light blue background for a modern look, and button styles have been customized to be bold with a yellow background.
   - The GUI is divided into tabs for easy navigation between the main menu, add, delete, and update functionalities.

2. **Tabs for Different Operations**:
   - **Main Menu Tab**: Provides buttons to navigate to different pages for adding, deleting, and updating students and mentors.
   - **Add Student/Mentor Tab**: Allows the user to input details such as Student ID, Name, and Interest, or Mentor ID, Name, and Expertise, and add them to the system.
   - **Delete Student/Mentor Tab**: Enables the user to delete students or mentors from the system by providing their ID.
   - **Update Student/Mentor Tab**: Offers the ability to update the details of existing students and mentors.

3. **Backend Data Management**:
   - Data for students and mentors is stored in CSV files (`students.csv` and `mentors.csv`), which are loaded and manipulated using the Pandas library.
   - The system allows adding, deleting, and updating of student and mentor records programmatically.

4. **Student-Mentor Allocation**:
   - The system implements an allocation algorithm to assign students to mentors. 
   - After allocation, the program visualizes the relationship between students and mentors using **matplotlib**. The graph shows the connections, with student names on one side and mentor names on the other.

5. **Graphical Visualization**:
   - The allocation graph visually represents the allocations of students to mentors with lines connecting students to their respective mentors.
   - It uses **matplotlib** to create the graphical representation, giving users an easy-to-understand visual breakdown of the allocation process.

### Technologies and Libraries Used:
- **Tkinter**: For creating the GUI (buttons, labels, entries, and tabs).
- **Pandas**: For handling CSV data (loading and saving student and mentor information).
- **Matplotlib**: For graphical visualization of student-mentor allocations.
- **OOPS** (`allocation`, `student`, `mentor`): To handle the core functionality of allocation and data management in the backend.

### Application Purpose:
This system can be useful in educational settings where mentors are assigned to students, such as internship programs, university projects, or mentoring programs. It allows easy management of large groups of students and mentors and simplifies the process of allocating mentors based on student interests and mentor expertise.
---

