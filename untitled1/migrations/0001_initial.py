# Generated by Django 4.1.6 on 2023-02-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='andouuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('account', models.DecimalField(decimal_places=10, max_digits=10)),
                ('address', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
