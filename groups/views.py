from django.shortcuts import render, get_object_or_404, redirect
from .models import Groups


def groups_list(request):
    groups = Groups.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/group-list.html', ctx)


def group_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')

        if first_name and last_name:
            Groups.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,

            )
            return redirect('groups:group_list')
    return render(request, 'groups/group-form.html')


def group_detail(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    ctx = {'groups': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_delete(request, pk):
    person = get_object_or_404(Groups, pk=pk)
    person.delete()
    return redirect('groups:group-list.html')
