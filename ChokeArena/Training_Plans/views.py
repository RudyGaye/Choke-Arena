from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TrainingPlan
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import TrainingPlanForm


def training_plan_detail(request, plan_id):
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)
    return render(request, 'training_plan_detail.html', {'training_plan': training_plan})

def index(request):
    return render(request, 'training_plan.html')

@login_required
def add_training_plan(request):
    if not request.user.groups.filter(name='redactor').exists():
        return HttpResponseForbidden("Vous n'êtes pas autorisé à ajouter des plans d'entraînement.")

    if request.method == 'POST':
        form = TrainingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_plans')
        # Rendre le formulaire avec les erreurs s'il est invalide
    else:
        form = TrainingPlanForm()

    return render(request, 'add_training_plan.html', {'form': form})
    
@login_required
def follow_training_plan(request, plan_id):
    training_plan = get_object_or_404(TrainingPlan, id=plan_id)
    request.user.library.training_plans.add(training_plan)
    training_plan.followers.add(request.user)
    return redirect('training_plan_detail', plan_id=plan_id)

@login_required
def unfollow_training_plan(request, plan_id):
    plan = get_object_or_404(TrainingPlan, id=plan_id)  
    request.user.library_plans.remove(plan)  
    training_plan.followers.remove(request.user)
    return redirect('training_plan_detail', plan_id=plan_id)  




def search(request):
    query = request.GET.get('q')  
    training_plans = TrainingPlan.objects.filter(name__icontains=query) if query else []
    techniques = Technique.objects.filter(name__icontains=query) if query else []
    context = {
        'query': query,
        'training_plans': training_plans,
        'techniques': techniques,
    }
    return render(request, 'search_results.html', context)  