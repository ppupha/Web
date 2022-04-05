# Generated by Django 3.2.12 on 2022-03-01 18:59

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=' ', max_length=100)),
                ('Rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('Address', models.CharField(default='', max_length=100)),
                ('Description', models.TextField(default='')),
                ('Type', models.IntegerField(default=1)),
                ('Site', models.CharField(default='', max_length=100)),
                ('Tel', models.CharField(default='', max_length=20)),
                ('City', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.city')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('createTime', models.DateTimeField(verbose_name=datetime.datetime(2022, 3, 1, 21, 59, 35, 839592))),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.place')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='./icon-login.png', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(default='', max_length=100, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.place')),
            ],
        ),
    ]
