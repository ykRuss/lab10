from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_all_students, name='get_all_students'),
    path('ongoing-courses/', views.get_all_ongoing_courses, name='get_all_ongoing_courses'),
    path('student/details/', views.get_student_details, name='get_student_details'),
    path('student/average-grade/', views.get_student_average_grade, name='get_student_average_grade'),
    path('student/ongoing-courses/', views.get_student_ongoing_courses, name='get_student_ongoing_courses'),
    path('student/completed-courses/', views.get_student_completed_courses, name='get_student_completed_courses'),
    path('student/completed-course-grade/', views.get_grade_of_completed_course, name='get_grade_of_completed_course'),
]
