class CandidateProfile:
    def __init__(self, name, email, score):
        # Public attribute: name
        self.name = name
        # Protected attribute: _email (convention: single underscore)
        self._email = email
        # Private attribute: __score (convention: double underscore triggers name mangling)
        self.__score = score

    def get_email(self):
        """Public method to access the protected email."""
        return self._email

    def get_score(self):
        """Public method to access the private score."""
        return self.__score

# --- Main Execution ---

# Read inputs
name = input().strip()
email = input().strip()
score = int(input())

# Create exactly one CandidateProfile object
candidate = CandidateProfile(name, email, score)

# Print the output in the specified format
print("CANDIDATE PROFILE")
# Access public name directly
print(f"Name: {candidate.name}")
# Access protected email using the method
print(f"Email: {candidate.get_email()}")
# Access private score using the method
print(f"Score: {candidate.get_score()}")