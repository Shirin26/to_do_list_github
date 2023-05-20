from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES

def index_views(request):
    tasks = Task.objects.order_by('-to_do_date')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context)



def task_create_views(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'statuses': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        to_do_date = request.POST.get('to_do_date')
        if not to_do_date:
            to_do_date = None
        new_task = Task.objects.create(description=description, status=status, to_do_date=to_do_date)
        context = {'task': new_task}
        return render(request, 'task_view.html', context)


