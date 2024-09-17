import pandas as pd
class Allocation:
    def __init__(self, students_file, mentors_file):
        self.students_file = students_file
        self.mentors_file = mentors_file
        self.allocations = []  # Initialize the allocations attribute
        self.load_data()

    def load_data(self):
        self.students_df = pd.read_csv(self.students_file)
        self.mentors_df = pd.read_csv(self.mentors_file)

    def allocate(self):
        self.allocations = []
        for _, student in self.students_df.iterrows():
            matched_mentors = self.mentors_df[self.mentors_df['expertise'].str.lower() == student['interest'].lower()]
            if not matched_mentors.empty:
                mentor = matched_mentors.iloc[0]
                self.allocations.append({'student_id': student['id'], 'mentor_id': mentor['id']})
        self.save_allocations()

    def add_student(self, id, name, interest):
        new_student = pd.DataFrame([[id, name, interest]], columns=['id', 'name', 'interest'])
        self.students_df = pd.concat([self.students_df, new_student], ignore_index=True)
        self.students_df.to_csv(self.students_file, index=False)

    def add_mentor(self, id, name, expertise):
        new_mentor = pd.DataFrame([[id, name, expertise]], columns=['id', 'name', 'expertise'])
        self.mentors_df = pd.concat([self.mentors_df, new_mentor], ignore_index=True)
        self.mentors_df.to_csv(self.mentors_file, index=False)

    def update_student(self, id, name, interest):
        self.students_df.loc[self.students_df['id'] == id, ['name', 'interest']] = [name, interest]
        self.students_df.to_csv(self.students_file, index=False)

    def update_mentor(self, id, name, expertise):
        self.mentors_df.loc[self.mentors_df['id'] == id, ['name', 'expertise']] = [name, expertise]
        self.mentors_df.to_csv(self.mentors_file, index=False)

    def delete_student(self, id):
        self.students_df = self.students_df[self.students_df['id'] != id]
        self.students_df.to_csv(self.students_file, index=False)

    def delete_mentor(self, id):
        self.mentors_df = self.mentors_df[self.mentors_df['id'] != id]
        self.mentors_df.to_csv(self.mentors_file, index=False)

    def save_allocations(self, filename="allocations.csv"):
        allocations_df = pd.DataFrame(self.allocations)
        allocations_df.to_csv(filename, index=False)

    def create_allocation_graph(self):
        allocation_graph = []
        student_dict = dict(zip(self.students_df['id'], self.students_df['name']))
        mentor_dict = dict(zip(self.mentors_df['id'], self.mentors_df['name']))

        for allocation in self.allocations:
            student_id = allocation['student_id']
            mentor_id = allocation['mentor_id']
            allocation_graph.append((student_dict[student_id], mentor_dict[mentor_id]))
        return allocation_graph
