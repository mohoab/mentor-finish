# Generated by Django 4.2.4 on 2023-08-26 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 17, 8, 48, 218618)),
        ),
    ]
