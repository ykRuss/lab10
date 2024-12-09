# Generated by Django 5.1.3 on 2024-12-09 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompletedCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.course')),
                ('grade_achieved', models.FloatField()),
            ],
            bases=('api.course',),
        ),
        migrations.CreateModel(
            name='OngoingCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.course')),
                ('remaining_seats', models.IntegerField()),
            ],
            bases=('api.course',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('courses_completed', models.ManyToManyField(to='api.completedcourse')),
                ('courses_enrolled', models.ManyToManyField(to='api.ongoingcourse')),
            ],
        ),
    ]
