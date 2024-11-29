from datetime import timezone
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from collec_management.forms import CollecForm, ElementForm
from collec_management.models import Collec, Element
from django.contrib import messages

def about(request):
    return render(request, 'about.html')

def collection(request,collec_id) :
    try:
        collec = Collec.objects.get(pk=collec_id)
    except Collec.DoesNotExist:
        raise Http404("La collection n'existe pas")
    return render(request,"collec_detail.html",{"collec":collec})

def collectionList(request):
    try:
        collec = Collec.objects.all()
    except Collec.DoesNotExist:
        raise Http404("La collection n'existe pas")
    return render(request,"collec_list.html",{"collec":collec})

def new_collec(request) :
    if request.method == "POST" :
        form = CollecForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, "Le jeu vidéo a bien été ajouté")
            return redirect('collec_list')
        else :
            messages.error(request, "Erreur dans l'ajout du jeu vidéo")
    else :
        form = CollecForm()
    return render(request,"collec_form.html",{"form":form})

def del_collec(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if request.method == "POST":
        collec.delete()
        messages.success(request, "Le jeu vidéo a bien été supprimé")
        return redirect('collec_list')
    
    
    return render(request, "collec_del.html", {"collec": collec})

def change_collec(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if request.method == "POST":
        form = CollecForm(request.POST, instance=collec)
        if form.is_valid():
            form.save()
            messages.success(request, "Le jeu vidéo a bien été modifié")
            return redirect('collec_list')
        else:
            messages.error(request, "Erreur dans la modification du jeu vidéo")
    else:
        form = CollecForm(instance=collec)
    return render(request, "collec_form_change.html", {"form": form, "collec": collec})

def home(request):
    return render(request, 'home.html')

def add_element(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'élément a bien été ajouté")
            return redirect('collec_list')
        else:
            messages.error(request, "Erreur dans l'ajout de l'élément")
    else:
        form = ElementForm()
    return render(request, "element_form.html", {"form": form})

def del_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if request.method == "POST":
        element.delete()
        messages.success(request, "L'élément a bien été supprimé")
        return redirect('collec_list')
    return render(request, "element_del.html", {"element": element})

