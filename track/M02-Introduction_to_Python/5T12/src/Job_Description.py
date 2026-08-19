class JobDescription:
    def __init__(self, job_id, company, role, location="Remote", is_active=True):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.job_id} | {self.company} | {self.role} | {self.location} | {status}"

# Create three JobDescription objects using keyword arguments
job_one = JobDescription(
    job_id=501,
    company="TechNova",
    role="Python Developer",
    location="Bengaluru",
    is_active=True
)

job_two = JobDescription(
    job_id=502,
    company="CodeWorks",
    role="Java Developer",
    location="Hyderabad",
    is_active=True
)

job_three = JobDescription(
    job_id=503,
    company="CloudNine",
    role="Support Engineer",
    location="Remote",
    is_active=False
)

# Store the objects in a list
job_descriptions = [job_one, job_two, job_three]

# Use a for loop to print each object
for job in job_descriptions:
    print(job)