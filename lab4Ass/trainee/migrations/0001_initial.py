# Generated by Django 4.0.5 on 2022-06-24 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('branch', models.IntegerField(null=True)),
                ('courses', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='trainee.course')),
            ],
        ),
    ]
