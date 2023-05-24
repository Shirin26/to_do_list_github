from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from webapp.forms import TaskForm


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
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                to_do_date=form.cleaned_data['to_do_date'])
            return redirect('task_view', pk=new_task.pk)
        else:
            return render(request, 'task_create.html', {'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'to_do_date': task.to_do_date
        })
        return render(request, 'task_update.html', {'task': task, 'statuses': STATUS_CHOICES, 'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.status = form.cleaned_data.get('status')
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.to_do_date = form.cleaned_data.get('to_do_date')
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'task': task, 'statuses': STATUS_CHOICES, 'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')

