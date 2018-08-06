from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def lista(request):
    """
    Função que lista todos os objetos da tabela Produtos do banco de dados.
    """
    data = {}
    data['produtos'] = Produto.objects.all()

    return render(request, 'listacompras/lista.html', data)

def novo_produto(request):
    """
    Função para inserir um novo produto no banco de dados, e consequentemente na lista.
    """
    data = {}
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form

    return render(request, 'listacompras/novo.html', data)

def update(request, pk):
    """
    Essa função além de receber o parâmetro request, recebe o parâmetro pk, pois precisamos saber o id do objeto no
    bando de dados, que é nossa chave primária.
    A função atualiza no banco de dados, os dados da tabela Produtos (nome, quantidade), e consequentemente na lista.
    """
    data = {}
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('url_lista')

    data['form'] = form
    data['produto'] = produto

    return render(request, 'listacompras/novo.html', data)

def delete(request, pk):
    """
    Essa função além de receber o parâmetro request, recebe o parâmetro pk, pois precisamos saber o id do objeto no
    bando de dados, que é nossa chave primária.
    A função atualiza no banco de dados, os dados da tabela Produtos (nome, quantidade), e consequentemente na lista.
    """
    produto = Produto.objects.get(pk=pk)
    produto.delete()

    return redirect('url_lista')








