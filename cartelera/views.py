from django.shortcuts import render

#vista de la pagina principal
def pag_principal(request):
    return render(request, "index.html")