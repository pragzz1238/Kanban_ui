# Generated by Django 5.0.2 on 2024-06-15 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KanbanBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_name', models.CharField(max_length=100)),
                ('assigned_users', models.ManyToManyField(related_name='assigned_boards', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('testing', 'Testing'), ('done', 'Done')], default='todo', max_length=20)),
                ('order', models.PositiveIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='kanban_app.kanbanboard')),
            ],
        ),
    ]
