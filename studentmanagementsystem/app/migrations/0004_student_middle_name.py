# Generated by Django 4.0.6 on 2022-07-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
