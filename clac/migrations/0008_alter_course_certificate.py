# Generated by Django 4.1.4 on 2023-05-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clac', '0007_alter_course_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
