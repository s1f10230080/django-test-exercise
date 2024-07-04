from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task


# Create your views here.
def index(request):
    if request.method == 'POST':
        task = Task(title=request.POST['title'],
                    due_at=make_aware(parse_datetime(request.POST['due_at'])))
        task.save()

    order = request.GET.get('order')
    if order == 'post':
        tasks = Task.objects.all().order_by('-posted_at')
    elif order == 'due':
        tasks = Task.objects.all().order_by('due_at')
    else:
        tasks = Task.objects.all()

    context = {
            'tasks': tasks
    }
    return render(request, 'todo/index.html', context)
