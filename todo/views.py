from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoForm

# List all tasks
def todo_list(request):
    tasks = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

# Create a new task
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

# Edit an existing task
def todo_edit(request, pk):
    task = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=task)
    return render(request, 'todo/todo_form.html', {'form': form})

# Delete a task
def todo_delete(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)
    todo_item.delete()  # Delete the item immediately
    return redirect('todo_list')  # Redirect to the todo list after deletion
