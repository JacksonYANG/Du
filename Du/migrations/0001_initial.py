# Generated by Django 2.0.1 on 2018-08-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rank', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('article', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('browse', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Du.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('source', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('browse', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Du.Category')),
            ],
        ),
    ]
