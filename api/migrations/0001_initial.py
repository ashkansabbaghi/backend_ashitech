# Generated by Django 3.2 on 2021-10-24 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique_for_date='publish')),
                ('caption', models.TextField()),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, verbose_name='عنوان لاتین')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انرژی')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
            ],
        ),
        migrations.CreateModel(
            name='ImageBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='image', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_image', to='api.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='api.Tag', verbose_name='تگ ها'),
        ),
    ]
