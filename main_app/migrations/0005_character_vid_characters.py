# Generated by Django 4.1.6 on 2023-02-17 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_progress_options_rename_meal_progress_progress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='vid',
            name='characters',
            field=models.ManyToManyField(to='main_app.character'),
        ),
    ]
