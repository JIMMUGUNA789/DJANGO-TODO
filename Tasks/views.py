from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# list all todos
def list_todos(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "list_todos.html", context)

# todo detail
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'todo_detail.html', context)


# create todo
def create_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        # title = form.cleaned_data["title"]
        # due_date = form.cleaned_data["due_date"]
        # Todo.objects.create(title=title, due_date=due_date)

        # since we are using forms then use this instead
        form.save()
        return redirect("/")

    context = {"form": form}

    return render(request, "create_todo.html", context)


# update todo
def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/')
    context={
        'form':form
    }
    return render(request, 'update_todo.html', context)


# delete todo
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
