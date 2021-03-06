# Generated by Django 3.1.4 on 2020-12-02 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(default='', max_length=200)),
                ('id', models.CharField(default='', max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id_name', models.CharField(default='', max_length=32, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='TopicTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['taken'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('image', models.ImageField(default=None, upload_to='cards')),
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(default='', max_length=32, primary_key=True, serialize=False, unique=True)),
                ('prerequisites', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('card_category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
