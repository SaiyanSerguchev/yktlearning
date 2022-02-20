# Generated by Django 3.2.4 on 2021-12-18 19:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_alter_donelessonsmodel_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionid', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('variant1', models.CharField(max_length=255)),
                ('variant2', models.CharField(max_length=255)),
                ('variant3', models.CharField(max_length=255)),
                ('variant4', models.CharField(max_length=255)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedtest', to='lessons.lessons')),
            ],
            options={
                'verbose_name': 'Тесты',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.DeleteModel(
            name='PracticeTest',
        ),
    ]