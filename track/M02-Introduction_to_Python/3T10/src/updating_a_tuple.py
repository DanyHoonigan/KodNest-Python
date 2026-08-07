course_name = input("Enter the course name: ")
course_week = input("Enter the week of the course: ")
course_status = input("Enter the status of the course: ")

course_detail = (course_name,course_week,course_status)
print(course_detail)

updated_week = input("Enter the updated week: ")

#updated_course_detail = (course_name,updated_week,course_status)
updated_course_detail = (course_detail[0],updated_week,course_detail[2])
print(updated_course_detail)