# Generated by Django 3.2.9 on 2021-11-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('codeSecret', models.IntegerField()),
                ('solde', models.IntegerField(default=0)),
            ],
        ),
    ]