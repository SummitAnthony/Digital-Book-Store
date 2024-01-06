from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView




def index(request):
    item_list = Item.objects.all()

    context = {
            'item_list':item_list,
    }
    return render(request, 'game/index.html', context)


class IndexClassView(ListView):
    model = Item;
    template_name = 'game/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("Hello, this is the item page.")

def user(request):
    return HttpResponse("Hello, this is the user page.")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'game/detail.html', context)


class GameDetail(DetailView):
    model = Item
    template_name = 'game/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('game:index')
    
    return render(request, 'game/items-forms.html', {'form':form})



class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'items_price', 'item_image']
    template_name = 'game/items-forms.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    




def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)            

    if form.is_valid():
        form.save()
        return redirect('game:index')
    
    return render(request, 'game/item-form.html',{'form':form, 'item':item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('game:index')
    
    return render(request, 'game/item-delete.html', {'item':item})