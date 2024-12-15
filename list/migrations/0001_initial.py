# Generated by Django 4.2.17 on 2024-12-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_url', models.CharField(max_length=150)),
                ('short_url', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]