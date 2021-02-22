from django.shortcuts import render, redirect
from .models import ToDoList, Item
from .forms import CreateNewListForm


def homepage(request):
    return redirect('/home')


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls in request.user.todolist.all():
        print(f'POST: {request.POST}')
        if request.method == 'POST':
            if request.POST.get('save'):
                for ind, item in enumerate(ls.item_set.all()):
                    if request.POST.get(f'c{item.id}') == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.text = request.POST.getlist('items_text')[ind]
                    item.save()
            elif request.POST.get('newItem'):
                txt = request.POST.get('new')
                if len(txt) > 1:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    pass
            elif tmp := request.POST.get(f'deleteItem'):
                item = ls.item_set.get(id=tmp)
                item.delete()

        return render(request, 'main/list.html', {'ls': ls})
    return render(request, 'main/view.html', {})


def home(request):
    return render(request, 'main/home.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewListForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

        return redirect(f'/{t.id}')
    else:
        form = CreateNewListForm()
    return render(request, 'main/create.html', {'form': form})


def view(request):
    return render(request, 'main/view.html', {})
