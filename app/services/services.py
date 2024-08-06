from app.services import students_service, courses_service, colleges_service

def search_all(query):
    students = students_service.search_students(query)
    courses = courses_service.search_courses(query)
    colleges = colleges_service.search_courses(query)

    results = {
        'students': students,
        'courses': courses,
        'colleges': colleges,
    }

    return results
