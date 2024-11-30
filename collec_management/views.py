from datetime import timezone
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from collec_management.forms import CollecForm, ElementForm, loginForm, registerForm
from collec_management.models import Collec, Element
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def about(request):
    return render(request, 'about.html')

@login_required
def collection(request,collec_id) :
    collec = get_object_or_404(Collec,pk=collec_id)
    if collec.user != request.user :
        raise Http404("Vous n'avez pas accès à cette collection")
    elements = Element.objects.filter(collec=collec)
    return render(request,"collec_detail.html",{"collec":collec, "elements":elements})

def collectionList(request):
    try:
        collec = Collec.objects.all()
    except Collec.DoesNotExist:
        raise Http404("La collection n'existe pas")
    return render(request,"collec_list.html",{"collec":collec})

@login_required
def new_collec(request) :
    if request.method == "POST" :
        form = CollecForm(request.POST)
        if form.is_valid() :
            user = request.user
            form.instance.user = user
            form.save()
            messages.success(request, "Le jeu vidéo a bien été ajouté")
            return redirect('collec_list')
        else :
            messages.error(request, "Erreur dans l'ajout du jeu vidéo")
    else :
        form = CollecForm()
    return render(request,"collec_form.html",{"form":form})

@login_required
def del_collec(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if collec.user != request.user:
        raise Http404("Vous n'avez pas la permission de supprimer cette collection")
    if request.method == "POST":
        collec.delete()
        messages.success(request, "Le jeu vidéo a bien été supprimé")
        return redirect('collec_list')
    
    
    return render(request, "collec_del.html", {"collec": collec})

@login_required
def change_collec(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if collec.user != request.user:
        raise Http404("Vous n'avez pas la permission de modifier cette collection")
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

@login_required
def add_element(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.user = user
            form.save()
            messages.success(request, "L'élément a bien été ajouté")
            return redirect('collec_list')
        else:
            messages.error(request, "Erreur dans l'ajout de l'élément")
    else:
        form = ElementForm()
    return render(request, "element_form.html", {"form": form})

@login_required
def del_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if element.user != request.user:
        raise Http404("Vous n'avez pas la permission de supprimer cet élément")
    if request.method == "POST":
        element.delete()
        messages.success(request, "L'élément a bien été supprimé")
        return redirect('collec_list')
    return render(request, "element_del.html", {"element": element})

def element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if element.user != request.user:
        raise Http404("Vous n'avez pas accès à cet élément")
    return render(request, "element_detail.html", {"element": element})

@login_required
def edit_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if element.user != request.user:
        raise Http404("Vous n'avez pas la permission de modifier cet élément")
    if request.method == "POST":
        form = ElementForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            messages.success(request, "L'élément a bien été modifié")
            return redirect('element_detail', element_id=element_id)
        else:
            messages.error(request, "Erreur dans la modification de l'élément")
    else:
        form = ElementForm(instance=element)
    return render(request, "element_form_edit.html", {"form": form, "element": element})

def login(request):
    form = loginForm(request.POST or None)
    next_url = request.GET.get('next', 'home')
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            auth_login(request, user)
            return redirect(next_url)
    return render(request, "login.html", {"form": form})

def logout(request):
    auth_logout(request)
    return redirect('home')

def register(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, "register.html", {"form": form})