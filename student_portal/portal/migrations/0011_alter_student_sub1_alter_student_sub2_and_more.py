# Generated by Django 4.2.10 on 2024-08-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_alter_student_sub1_alter_student_sub2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sub1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
