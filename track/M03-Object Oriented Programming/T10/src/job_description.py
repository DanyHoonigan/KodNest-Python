class JobDescription:
    def __init__(self, job_id, company, role, location, required_skills, is_active):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.required_skills = required_skills
        self.is_active = is_active

    def __str__(self):
        # Convert list of skills to a comma-separated string
        skills_text = ", ".join(self.required_skills)
        
        # Convert boolean is_active to "Active" or "Closed"
        status = "Active" if self.is_active else "Closed"
        
        # Return the formatted multi-line string
        return f"""JOB DESCRIPTION
Job ID: {self.job_id}
Company: {self.company}
Role: {self.role}
Location: {self.location}
Required Skills: {skills_text}
Status: {status}"""

# --- Main Execution ---

# Read inputs
job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()

# Read skills as a comma-separated string and split into a list
skills_input = input().strip()
required_skills = skills_input.split(", ")

# Read status (Yes/No) and convert to boolean
status_input = input().strip()
is_active = status_input.lower() == "yes"

# Create exactly one JobDescription object
job = JobDescription(job_id, company, role, location, required_skills, is_active)

# Display the object
# Python automatically calls job.__str__() when printing the object
print(job)