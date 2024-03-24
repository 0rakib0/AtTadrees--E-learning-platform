# Generated by Django 4.1.4 on 2023-05-03 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clac', '0004_alter_whats_learn_pont2'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='skill_level',
            field=models.CharField(default=1, max_length=160),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_leson', to='clac.lesson'),
        ),
    ]
