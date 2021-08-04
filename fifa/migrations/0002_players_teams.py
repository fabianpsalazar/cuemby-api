# Generated by Django 2.2.12 on 2021-08-04 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('page', models.IntegerField()),
                ('total_pages', models.IntegerField()),
                ('items', models.IntegerField()),
                ('total_items', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=5)),
                ('nation', models.CharField(max_length=20)),
                ('players_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.Teams', verbose_name='related players')),
            ],
        ),
    ]