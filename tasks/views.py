from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def kanban_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/kanban.html', {'tasks': tasks})

@login_required
def change_status(request, task_id, new_status):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if new_status in ['todo', 'doing', 'done']:
        task.status = new_status
        task.save()
        
    return redirect(request.META.get('HTTP_REFERER', 'kanban'))

@login_required
def calendar_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/calendar.html', {'tasks': tasks})

@login_required
def profile_view(request):
    return render(request, 'tasks/profile.html')

@login_required
def task_create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        due_date = request.POST.get('due_date')

        category = None
        if category_id and category_id.isdigit():
            category = Category.objects.get(id=category_id)

        Task.objects.create(
            title=title,
            description=description,
            user=request.user,
            category=category,
            due_date=due_date,
            status='todo'
        )
        return redirect('kanban') 

    return render(request, 'tasks/task_form.html', {'categories': categories})

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER', 'tasks'))

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'tasks/login.html', {'error': 'Usuário ou senha inválidos.'})

    return render(request, 'tasks/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'tasks/register.html', {'error': 'Este nome de utilizador já está em uso.'})
        
        user = User.objects.create_user(username=username, password=password)
        
        login(request, user)
        return redirect('dashboard')

    return render(request, 'tasks/register.html')