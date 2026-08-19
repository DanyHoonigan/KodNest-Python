class StudentProfile:
    def __init__(self, name, score):
        self.name = name
        # Private attribute using double underscores
        self.__score = score

    def get_score(self):
        """Getter method to return the private score."""
        return self.__score

    def set_score(self, new_score):
        """Setter method to update score only if valid (0-100)."""
        if 0 <= new_score <= 100:
            self.__score = new_score
            return True
        return False

# --- Main Execution ---

# Read inputs
name = input().strip()
initial_score = int(input())
new_score = int(input())

# Create exactly one StudentProfile object
student = StudentProfile(name, initial_score)

# Attempt to update the score
was_updated = student.set_score(new_score)

# Display output based on the result
if was_updated:
    print("Score Updated")
    print(f"Name: {student.name}")
    print(f"Final Score: {student.get_score()}")
else:
    print("Invalid Score")
    print(f"Name: {student.name}")
    print(f"Final Score: {student.get_score()}")