from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    # teacher_objects = Teacher.objects.all()
    student_objects = Student.objects.order_by(ordering).prefetch_related('teachers')

    # student = [f'{student.name}' for student in student_objects]

    # all = Student.objects.filter(id=1)
    # print(all)

    # print(teacher_objects, student)

    context = {
        'object_list': student_objects,
        # 'teacher_list': teacher_objects,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
