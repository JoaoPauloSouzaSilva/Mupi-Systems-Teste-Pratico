from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from django.utils.timezone import now  # type: ignore
from .models import Task
from .forms import TaskForm
from .forms import CustomTaskForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    # Filtra as tarefas do usuário autenticado
    tasks = Task.objects.filter(user=request.user)
    # Divide as tarefas em concluídas e pendentes
    completed_tasks = tasks.filter(completed=True).order_by('-created_at')
    pending_tasks = tasks.filter(completed=False).order_by('-created_at')

    return render(request, 'tasks/home.html', {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = CustomTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Tarefa criada com sucesso!")
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CustomTaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    # Busca a tarefa pelo ID (pk) e verifica se pertence ao usuário logado
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        # Atualiza a tarefa com os dados enviados pelo formulário
        form = CustomTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect('home')  # Redireciona para a página inicial
    else:
        # Preenche o formulário com os dados existentes da tarefa
        form = CustomTaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'is_update': True})

@login_required
def task_delete(request, pk):
    # Busca a tarefa pelo ID (pk) e verifica se pertence ao usuário logado
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()  # Deleta a tarefa do banco de dados
        messages.success(request, "Tarefa excluída com sucesso!")
        return redirect('home')  # Redireciona para a página inicial

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_mark_complete(request, pk):
    # Busca a tarefa pelo ID (pk) e verifica se pertence ao usuário logado
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True  # Marca a tarefa como concluída
    task.save()
    return redirect('home')  # Redireciona para a página inicial

@login_required
def task_unmark_complete(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)

    # Verificar se a tarefa está atrasada
    if task.due_date and task.due_date < now():
        messages.error(request, "Você não pode desmarcar uma tarefa atrasada.")
        return redirect("home")

    # Desmarcar como concluída
    task.completed = False
    task.save()
    messages.success(request, "Tarefa desmarcada como concluída com sucesso.")
    return redirect("home")

