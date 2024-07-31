# Generated by Django 5.0.2 on 2024-07-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=128)),
                ('website', models.CharField(blank=True, max_length=1024, null=True)),
                ('company', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=64)),
            ],
        ),
    ]
