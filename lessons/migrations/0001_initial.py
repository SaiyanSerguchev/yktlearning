# Generated by Django 3.2.4 on 2021-07-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theory', models.TextField(blank=True)),
                ('words', models.TextField(blank=True)),
                ('question1', models.CharField(max_length=255)),
                ('answer1', models.CharField(max_length=255)),
                ('variant11', models.CharField(max_length=255)),
                ('variant21', models.CharField(max_length=255)),
                ('variant31', models.CharField(max_length=255)),
                ('variant41', models.CharField(max_length=255)),
                ('question2', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('variant12', models.CharField(max_length=255)),
                ('variant22', models.CharField(max_length=255)),
                ('variant32', models.CharField(max_length=255)),
                ('variant42', models.CharField(max_length=255)),
                ('question3', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('variant13', models.CharField(max_length=255)),
                ('variant23', models.CharField(max_length=255)),
                ('variant33', models.CharField(max_length=255)),
                ('variant43', models.CharField(max_length=255)),
                ('question4', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
                ('variant14', models.CharField(max_length=255)),
                ('variant24', models.CharField(max_length=255)),
                ('variant34', models.CharField(max_length=255)),
                ('variant44', models.CharField(max_length=255)),
                ('question5', models.CharField(max_length=255)),
                ('answer5', models.CharField(max_length=255)),
                ('variant15', models.CharField(max_length=255)),
                ('variant25', models.CharField(max_length=255)),
                ('variant35', models.CharField(max_length=255)),
                ('variant45', models.CharField(max_length=255)),
            ],
        ),
    ]