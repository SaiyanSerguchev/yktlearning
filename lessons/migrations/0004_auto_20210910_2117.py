# Generated by Django 3.2.4 on 2021-09-10 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0003_lessons_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='done',
        ),
        migrations.RemoveField(
            model_name='lessons',
            name='user',
        ),
        migrations.CreateModel(
            name='DoneLessonsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('lessons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.lessons')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]