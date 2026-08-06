students_count= int(input("Enter number of students: "))
total = 0
passed = 0
failed = 0
count = 0
for i in range (students_count):
    mark = int(input("Mark of the student: "))
    if mark >= 40:
        passed += 1
    else:
        failed += 1
    total += mark
    count += 1 
print(f"Total: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
if students_count == passed:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")
average = total/count
print(f"Average of all student's mark is {average}")