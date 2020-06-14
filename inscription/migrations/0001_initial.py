# Generated by Django 3.0.7 on 2020-06-14 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section', '0001_initial'),
        ('grade', '0001_initial'),
        ('alumn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('alumn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumn.Alumn')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.Grade')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.Section')),
            ],
        ),
    ]