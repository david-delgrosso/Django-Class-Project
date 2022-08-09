# Generated by Django 3.1.3 on 2022-08-09 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220809_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson_id',
        ),
        migrations.AddField(
            model_name='question',
            name='course_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
    ]
