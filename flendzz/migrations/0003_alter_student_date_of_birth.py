# Generated by Django 3.2.7 on 2021-09-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flendzz', '0002_alter_student_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]
