from django.contrib import admin
from .models import TrainingPlan

@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty')
    search_fields = ('name', 'description')
    filter_horizontal = ('techniques',)  
