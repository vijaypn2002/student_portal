# Generated by Django 4.2.10 on 2024-08-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_student_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='exam_address',
            field=models.CharField(default='ENGLISH', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='mediam',
            field=models.CharField(default='ENGLISH', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(default='ENGLISH', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='stud_address',
            field=models.CharField(default='ENGLISH', max_length=50),
        ),
    ]
