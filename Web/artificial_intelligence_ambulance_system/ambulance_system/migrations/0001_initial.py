# Generated by Django 2.2.4 on 2019-08-21 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('CountryName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(default=False)),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsibleUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=15)),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='TrafficConditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('DefaultAmbulanceCount', models.IntegerField(default=-1)),
                ('Description', models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficConditionLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datetime', models.DateTimeField(auto_now=True)),
                ('Solved', models.BooleanField(default=True)),
                ('Processed', models.BooleanField(default=True)),
                ('Monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Monitors')),
                ('ResponsibleUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.ResponsibleUnits')),
                ('TrafficCondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.TrafficConditions')),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceSchedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=20)),
                ('Ambulance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Ambulances')),
                ('TrafficConditionLog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.TrafficConditionLogs')),
            ],
        ),
        migrations.AddField(
            model_name='ambulances',
            name='ResponsibleUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.ResponsibleUnits'),
        ),
    ]
