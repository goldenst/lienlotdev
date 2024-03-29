# Generated by Django 2.2.4 on 2019-09-01 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('vin', models.CharField(max_length=17)),
                ('engine', models.CharField(max_length=20)),
                ('fuel', models.CharField(max_length=20)),
                ('catagory', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('keys', models.BooleanField(default=True)),
                ('comment', models.TextField(blank=True)),
                ('avalible_date', models.DateTimeField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y%m/%d/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sellers.Seller')),
            ],
        ),
    ]
