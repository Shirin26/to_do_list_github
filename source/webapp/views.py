from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES


def index_views(request):
    tasks = Task.objects.order_by('-to_do_date')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def task_view(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def task_create_views(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'statuses': STATUS_CHOICES})
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        to_do_date = request.POST.get('to_do_date')
        if not to_do_date:
            to_do_date = None
        new_task = Task.objects.create(title=title, description=description, status=status, to_do_date=to_do_date)
        return redirect('task_view', pk=new_task.pk)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {'task': task, 'statuses': STATUS_CHOICES})
    elif request.method == 'POST':
        task.status = request.POST.get('status')
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.to_do_date = request.POST.get('to_do_date')
        task.save()
        return redirect('task_view', pk=task.pk)

def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')

