class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        # Join the list of skills with a comma and a space
        skills_text = ", ".join(self.skills)
        
        # Return the formatted multi-line string
        return f"""STUDENT PROFILE
Student ID: {self.student_id}
Name: {self.name}
Course: {self.course}
Experience in Years: {self.experience}
Skills: {skills_text}"""

# Read inputs
student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills_input = input().strip()

# Convert the space-separated skills string into a list
skills = skills_input.split()

# Create exactly one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Display the object using print(student)
# This automatically calls student.__str__()
print(student)