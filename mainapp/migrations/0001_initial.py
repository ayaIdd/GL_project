# Generated by Django 4.1.4 on 2022-12-29 14:07

import cloudinary.models
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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('modalite', models.CharField(choices=[('0', 'hors ligne'), ('1', 'en ligne')], default='1', max_length=1)),
                ('tarif', models.CharField(max_length=255)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('0', 'Primaire'), ('1', 'Cem'), ('2', 'Lycee')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('0', 'mathematique'), ('1', 'physique'), ('2', 'science')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wilaya', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.annonce')),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=700)),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.annonce')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.annonce')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.wilaya')),
            ],
        ),
        migrations.AddField(
            model_name='annonce',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.categorie'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.theme'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user'),
        ),
        migrations.AddField(
            model_name='address',
            name='commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.commune'),
        ),
    ]