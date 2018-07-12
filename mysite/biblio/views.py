from django.shortcuts import render

def livro_list(request):
    return render(request, 'biblio/livro_list.html', {})