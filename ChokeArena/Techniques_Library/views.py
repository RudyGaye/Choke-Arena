from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TechniqueForm
from .models import Technique, Category, Type

def techniques_library(request):
    techniques = Technique.objects.all()
    return render(request, 'techniques_library.html', {'techniques': techniques})


def type_detail(request, id):
    type_instance = get_object_or_404(Type, id=id)
    return render(request, 'type_detail.html', {'type': type_instance})


@login_required
def add_technique(request):
    if not request.user.groups.filter(name='redactor').exists():
        print("Redirection: L'utilisateur n'est pas un rédacteur")
        return redirect('techniques_library')

    if request.method == 'POST':
        form = TechniqueForm(request.POST)
        if form.is_valid():
            technique = form.save()
            print("Formulaire validé et technique ajoutée")
            return redirect('technique_detail', technique_id=technique.id)
        else:
            print("Formulaire invalide")
            print(form.errors)
    else:
        form = TechniqueForm()

    return render(request, 'add_technique.html', {'form': form})

def technique_detail(request, technique_id):
    technique = get_object_or_404(Technique, id=technique_id)
    return render(request, 'technique_detail.html', {'technique': technique})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'category_detail.html', {'category': category})

@login_required
def follow_technique(request, technique_id):
    if request.method == 'POST':
        technique = get_object_or_404(Technique, id=technique_id)
        technique.followers.add(request.user)
        request.user.library_techniques.add(technique)
        return redirect('technique_detail', technique_id=technique_id)

@login_required
def unfollow_technique(request, technique_id):
    if request.method == 'POST':
        technique = get_object_or_404(Technique, id=technique_id)
        technique.followers.remove(request.user)
        request.user.library_techniques.remove(technique)
        return redirect('technique_detail', technique_id=technique_id)
