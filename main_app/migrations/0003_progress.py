# Generated by Django 4.1.6 on 2023-02-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_year_vid_release'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('S', 'Started'), ('I', 'In-progress'), ('C', 'Completed')], default='S', max_length=1)),
            ],
        ),
    ]