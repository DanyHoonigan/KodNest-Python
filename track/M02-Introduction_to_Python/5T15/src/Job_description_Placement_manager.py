class JobDescription:
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"


class PlacementManager:
    def __init__(self):
        self.job_descriptions = []

    def add_job_description(self, job_description):
        self.job_descriptions.append(job_description)

    def display_job_descriptions(self):
        if not self.job_descriptions:
            print("No job descriptions available")
            return

        print("JOB DESCRIPTIONS")

        for job_description in self.job_descriptions:
            print(job_description)


manager = PlacementManager()

n = int(input())

for _ in range(n):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    job = JobDescription(job_id, company, role)
    manager.add_job_description(job)

manager.display_job_descriptions()