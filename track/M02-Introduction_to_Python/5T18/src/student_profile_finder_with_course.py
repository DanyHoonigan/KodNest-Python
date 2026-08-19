class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def filter_students_by_course(self, required_course):
        matching_students = []
        # Convert required course to lowercase for case-insensitive comparison
        required_course_lower = required_course.lower()

        for student in self.student_profiles:
            if student.course.lower() == required_course_lower:
                matching_students.append(student)
        
        return matching_students


# Main Execution
manager = PlacementManager()

# Read number of students
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

# Read the course to filter by
required_course = input().strip()

# Get matching students
matching_students = manager.filter_students_by_course(required_course)

# Output results
if matching_students:
    for student in matching_students:
        print(student)
else:
    print(f"No students found for course: {required_course}")