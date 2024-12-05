from django.shortcuts import render, get_object_or_404, redirect
from .models import Teachers


def teacher_list(request):
    teachers = Teachers.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teacher-list.html', ctx)


def teacher_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if first_name and last_name and email:
            Teachers.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                email=email

            )
            return redirect('teachers:teacher_list')
    return render(request, 'teachers/teacher-form.html')


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    ctx = {'teachers': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)


def teacher_delete(request, pk):
    person = get_object_or_404(Teachers, pk=pk)
    person.delete()
    return redirect('teachers:teacher_list')
