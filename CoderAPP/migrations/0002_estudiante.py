# Generated by Django 5.0.6 on 2024-06-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoderAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.IntegerField(max_length=30)),
            ],
        ),
    ]
