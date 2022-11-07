from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    student_objects = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {
        'object_list': student_objects,
        # 'teacher_list': teacher_objects,
    }
    return render(request, template, context)
