# Generated by Django 4.0.4 on 2022-05-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsaffair', '0002_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.PositiveIntegerField(choices=[('Level-1', 'Level-1'), ('Level-2', 'Level-2'), ('Level-3', 'Level-3'), ('Level-4', 'Level-4')]),
        ),
    ]