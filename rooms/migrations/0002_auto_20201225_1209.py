# Generated by Django 3.1.4 on 2020-12-25 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.abstractitem')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitem',),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, to='rooms.Roomtype'),
        ),
    ]
