# Generated by Django 2.0.2 on 2018-03-13 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id_author', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.TextField()),
                ('link', models.CharField(max_length=200, unique=True)),
                ('crc', models.CharField(max_length=10)),
                ('id_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.Authors')),
            ],
        ),
    ]
