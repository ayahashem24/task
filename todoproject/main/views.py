from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task , Category ,Todo
from .forms import TaskForm , CategoryForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

@login_required
def index(request):
    todos = Todo.objects.all()
    tasks = Task.objects.all()
    categories = Category.objects.all()

    context = { 'tasks':tasks ,
                'categories' :categories,
                'todos': todos
                }
    
    return render(request , 'main/index.html',context)



@login_required
def category_tasks(request, category_id):
    category = Category.objects.get(id=category_id)
    tasks = Todo.objects.filter(category=category)
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})

@login_required
def detailed_task(request ,id):
    task = Task.objects.get(id=id)
    context = {
        'task':task
    }
    return render(request , 'main/detailed.html' , context)

@login_required
def todo_by_status(request , st):
    todos = Task.objects.filter(status = st)
    context = {
        'todos' :todos
    }
    return render(request , 'main/todosstatus.html' , context)


@login_required
def tasks_by_status(request, status):
    tasks = Todo.objects.filter(status=status)
    return render(request, 'tasks_by_status.html', {'tasks': tasks, 'status': status})

@login_required
def tasks_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    tasks = Todo.objects.filter(category=category)
    return render(request, 'tasks_by_category.html', {'tasks': tasks, 'category': category})


@login_required
def Todo_list_Category(request  , id):
    todos = Task.objects.filter(category=id)
    categories = Category.objects.all()

    context = {
        "tasks" : todos ,
        'categories' :categories

    }
    return render(request , 'main/index.html',context)

@login_required
def Createtodo(request ,task_id=None):
    if task_id:
        task = get_object_or_404(Task, id=task_id)
    else:
        task = None

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'main/create_todo.html', {'form': form})

@login_required
def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save()          
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request , 'main/createCategorys.html' ,{'form':form})


@login_required
def update_task(request , id ):
    task = get_object_or_404(Task , id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form})


@login_required
def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')




@login_required
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})