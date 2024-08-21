from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TrainingPlan
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import TrainingPlanForm
from Techniques_Library.models import Technique
from django.db.models import Q

def training_plan_detail(request, plan_id):
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)
    stars = range(1, 6)
    return render(request, 'training_plan_detail.html', {'training_plan': training_plan,'stars': stars})

def index(request):
    plans = TrainingPlan.objects.all()  # Remplacez par votre propre requête pour récupérer les plans
    stars = range(1, 6)
    return render(request, 'training_plan.html', {'plans': plans, 'stars': stars})

@login_required
def add_training_plan(request):
    if not request.user.groups.filter(name='redactor').exists():
        return HttpResponseForbidden("Vous n'êtes pas autorisé à ajouter des plans d'entraînement.")

    if request.method == 'POST':
        form = TrainingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_plans_index')
        # Rendre le formulaire avec les erreurs s'il est invalide
    else:
        form = TrainingPlanForm()

    return render(request, 'add_training_plan.html', {'form': form})
    
@login_required
def follow_training_plan(request, plan_id):
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)
    request.user.library_plans.add(training_plan)  # Assurez-vous que 'library_plans' existe dans votre modèle utilisateur
    training_plan.followers.add(request.user)  # Assurez-vous que 'followers' est défini dans 'TrainingPlan'
    return redirect('training_plan_detail', plan_id=plan_id)


@login_required
def unfollow_training_plan(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id)
    
    # Retirer le plan d'entraînement de la bibliothèque de l'utilisateur
    request.user.library_plans.remove(plan)

    # Retirer l'utilisateur de la liste des followers du plan
    plan.followers.remove(request.user)
    
    return redirect('training_plan_detail', plan_id=plan_id)


def search(request):
    query = request.GET.get('q')
    
    if query:
        # Rechercher dans les noms et descriptions
        training_plans = TrainingPlan.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        techniques = Technique.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        training_plans = []
        techniques = []

    context = {
        'query': query,
        'training_plans': training_plans,
        'techniques': techniques,
    }
    return render(request, 'search_results.html', context)