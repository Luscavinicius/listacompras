from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def lista(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    return render(request, 'listacompras/lista.html', data)

def novo_produto(request):
    data = {}
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form

    return render(request, 'listacompras/novo.html', data)

def update(request, pk):
    data = {}
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form
    data['produto'] = produto

    return render(request, 'listacompras/novo.html', data)








