# Generated by Django 3.0.6 on 2020-08-23 22:09

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('description', models.TextField(verbose_name='Category Description')),
                ('image', models.ImageField(upload_to='uploads/', verbose_name='Category Image')),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Magazine Issue Name')),
                ('cover_image', models.ImageField(upload_to='uploads/', verbose_name='Cover Image')),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Magazine Issue',
                'verbose_name_plural': 'Magazine Issue',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='News Title')),
                ('image', models.ImageField(upload_to='static/uploads/', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('body', models.TextField(verbose_name='News Body')),
                ('date', models.DateField(verbose_name='Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('name', models.CharField(max_length=20, verbose_name='Image Name')),
                ('caption', models.TextField(verbose_name='Image Caption')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category')),
            ],
            options={
                'verbose_name': 'Image Gallery',
                'verbose_name_plural': 'Image Gallery',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Article Title')),
                ('cover_image', models.ImageField(upload_to='uploads/', verbose_name='Cover Image')),
                ('date', models.DateField(auto_now_add=True)),
                ('tag', models.CharField(choices=[('main', 'Main'), ('featured', 'Featured')], max_length=20, verbose_name='Tag')),
                ('body_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('subheading', models.CharField(max_length=100, verbose_name='Sub Heading')),
                ('body', models.TextField(verbose_name='Article Body')),
                ('subheading1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sub Heading (optional)')),
                ('body1', models.TextField(blank=True, null=True, verbose_name='Article Body (optional)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Magazine')),
            ],
            options={
                'verbose_name': 'Articles',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]