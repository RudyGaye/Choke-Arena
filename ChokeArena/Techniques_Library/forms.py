from django import forms
from .models import Technique, Category, Type

class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = ['name', 'description', 'video_url', 'category', 'type', 'position']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
        }
