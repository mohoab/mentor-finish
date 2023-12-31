# Generated by Django 4.2.4 on 2023-08-26 10:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=200)),
                ('twitter', models.TextField(null=True)),
                ('facebook', models.TextField(null=True)),
                ('linkdien', models.TextField(null=True)),
                ('instagram', models.TextField(null=True)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(to='course.skills')),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='course')),
                ('counted_views', models.IntegerField(default=0)),
                ('counted_likes', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('schedule', models.DateTimeField(default=datetime.datetime(2023, 8, 26, 13, 55, 5, 371551))),
                ('available_seats', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='course.category')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.trainer')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
