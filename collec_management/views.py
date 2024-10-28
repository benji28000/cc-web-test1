from django.shortcuts import render, redirect
from .models import Collec
from .forms import CollecForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def list(request):
    collections = Collec.objects.all()
    return render(request, 'list.html', {'collections':collections})

def detailCollection(request,id):
    collection= Collec.objects.get(id=id)
    return render(request, 'detailCollection.html', {'collection':collection})

def CreateCollection(request):
    if request.method == 'POST':
        form = CollecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collec_management:all')
    else:
        form = CollecForm()
    return render(request, 'new.html', {'form': form})

def deleteCollection(request, id):
    collection = Collec.objects.get(id=id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collec_management:all')
    return render(request, 'delete.html', {'collection': collection})

def changeCollection(request, id):
    collection = Collec.objects.get(id=id)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collec_management:all')
    else:
        form = CollecForm(instance=collection)
    return render(request, 'edit.html', {'form': form})
