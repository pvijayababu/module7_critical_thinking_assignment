# Define the dictionaries
course_room_number = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

course_instructors_name = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

course_meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Get the course number from the user
course_number = input("Enter a course number (CSC101 / CSC102 / CSC103 / NET110 / COM241): ")

# Check if the course number exists in the dictionaries
if course_number in course_room_number and course_number in course_instructors_name and course_number in course_meeting_times:
    # Display the course details
    print(f"Room Number: {course_room_number[course_number]}")
    print(f"Instructor Name: {course_instructors_name[course_number]}")
    print(f"Meeting Time: {course_meeting_times[course_number]}")
else:
    print("Course number not found.")