# training_plans/forms.py
from django import forms
from .models import TrainingPlan

class TrainingPlanForm(forms.ModelForm):
    class Meta:
        model = TrainingPlan
        fields = ['name', 'description','techniques', 'difficulty']


    def clean_difficulty(self):
        difficulty = self.cleaned_data.get('difficulty')
        if difficulty < 0 or difficulty > 5:
            raise forms.ValidationError('Difficulty must be between 0 and 5.')
        return difficulty