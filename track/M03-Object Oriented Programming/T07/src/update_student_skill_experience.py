class StudentProfile:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills
        
    def update_experience(self, new_experience):
        self.experience = new_experience
        
    def add_skill(self, new_skill):
        # Add the new skill to the existing list
        self.skills.append(new_skill)
        
# Read initial data
name = input().strip()
experience = int(input())
skills = input().split()

# Read new data
new_experience = int(input())
new_skill = input().strip()

# Create one StudentProfile object
student = StudentProfile(name, experience, skills)

# Update the existing object
student.update_experience(new_experience)
student.add_skill(new_skill)

# Print the updated student profile
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")