from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, OngoingCourse, CompletedCourse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def get_all_ongoing_courses(request):
    from .models import OngoingCourse
    courses = OngoingCourse.objects.all()
    course_list = [{"id": course.id, "name": course.name, "department": course.department, "remaining_seats": course.remaining_seats} for course in courses]
    return Response(course_list)

@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    student_list = [{"id": student.id, "name": student.name, "department": student.department, "semester": student.semester} for student in students]
    return Response(student_list)

@api_view(['POST'])
def get_student_details(request):
    student_id = request.data.get('id')
    try:
        student = Student.objects.get(id=student_id)
        student_data = {
            "id": student.id,
            "name": student.name,
            "department": student.department,
            "semester": student.semester,
        }
        return Response(student_data)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
    
@api_view(['POST'])
def get_student_average_grade(request):
    student_id = request.data.get('id')
    try:
        student = Student.objects.get(id=student_id)
        completed_courses = student.courses_completed.all()
        if completed_courses.exists():
            average_grade = sum(course.grade_achieved for course in completed_courses) / completed_courses.count()
            return Response({"average_grade": average_grade})
        return Response({"average_grade": "No completed courses available"})
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)


@api_view(['POST'])
def get_student_ongoing_courses(request):
    student_id = request.data.get('id')
    try:
        student = Student.objects.get(id=student_id)
        ongoing_courses = student.courses_enrolled.all()
        course_list = [{"id": course.id, "name": course.name, "remaining_seats": course.remaining_seats} for course in ongoing_courses]
        return Response(course_list)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

@api_view(['POST'])
def get_student_completed_courses(request):
    student_id = request.data.get('id')
    try:
        student = Student.objects.get(id=student_id)
        completed_courses = student.courses_completed.all()
        course_list = [{"id": course.id, "name": course.name, "grade_achieved": course.grade_achieved} for course in completed_courses]
        return Response(course_list)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

@api_view(['POST'])
def get_grade_of_completed_course(request):
    student_id = request.data.get('id')
    course_name = request.data.get('course_name')
    try:
        student = Student.objects.get(id=student_id)
        completed_course = student.courses_completed.filter(name=course_name).first()
        if completed_course:
            return Response({"course_name": course_name, "grade_achieved": completed_course.grade_achieved})
        return Response({"error": "Course not found or not completed by the student"}, status=404)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)


@api_view(['GET'])
def all_routes(request):
    routes = {
        "GET /api/students": "List all students",
        "GET /api/ongoing-courses": "List all ongoing courses",
        "POST /api/student/<id>": "Get student details",
        "POST /api/student/<id>/average-grade": "Get student's average grade",
        "POST /api/student/<id>/ongoing-courses": "Get student's ongoing courses",
        "POST /api/student/<id>/completed-courses": "Get student's completed courses",
        "POST /api/student/<id>/completed-course/<name>": "Get grade of completed course",
    }
    return Response(routes)
