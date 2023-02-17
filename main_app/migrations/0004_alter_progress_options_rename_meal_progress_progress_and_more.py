# Generated by Django 4.1.6 on 2023-02-10 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_progress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='meal',
            new_name='progress',
        ),
        migrations.AddField(
            model_name='progress',
            name='vid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Vid'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.DateField(verbose_name='Progress date'),
        ),
    ]
