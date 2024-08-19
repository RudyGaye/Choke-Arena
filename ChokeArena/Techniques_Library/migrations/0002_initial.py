# Generated by Django 5.1 on 2024-08-19 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Techniques_Library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='followers',
            field=models.ManyToManyField(related_name='followed_techniques', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='technique',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techniques', to='Techniques_Library.position'),
        ),
        migrations.AddField(
            model_name='type',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='Techniques_Library.category'),
        ),
        migrations.AddField(
            model_name='technique',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techniques', to='Techniques_Library.type'),
        ),
    ]
