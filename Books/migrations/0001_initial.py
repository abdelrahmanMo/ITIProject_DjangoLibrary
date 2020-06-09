# Generated by Django 3.0.7 on 2020-06-07 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('description', models.TextField(default=' ')),
                ('bookImg', models.ImageField(default='book_img/default.png', upload_to='book_img')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listbook', to='Authors.Authors')),
                ('statusName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Books.status')),
            ],
        ),
    ]
