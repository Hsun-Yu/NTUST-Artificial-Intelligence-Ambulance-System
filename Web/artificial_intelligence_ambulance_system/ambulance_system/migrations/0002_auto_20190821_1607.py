# Generated by Django 2.2.4 on 2019-08-21 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=20)),
                ('Ambulance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Ambulance')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('CountryName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(default=False)),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Location')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsibleUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=15)),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Location')),
            ],
        ),
        migrations.CreateModel(
            name='TrafficCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('DefaultAmbulanceCount', models.IntegerField(default=-1)),
                ('Description', models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficConditionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datetime', models.DateTimeField(auto_now=True)),
                ('Solved', models.BooleanField(default=True)),
                ('Processed', models.BooleanField(default=True)),
                ('Monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.Monitor')),
                ('ResponsibleUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.ResponsibleUnit')),
                ('TrafficCondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.TrafficCondition')),
            ],
        ),
        migrations.RemoveField(
            model_name='ambulanceschedules',
            name='Ambulance',
        ),
        migrations.RemoveField(
            model_name='ambulanceschedules',
            name='TrafficConditionLog',
        ),
        migrations.RemoveField(
            model_name='monitors',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='responsibleunits',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='trafficconditionlogs',
            name='Monitor',
        ),
        migrations.RemoveField(
            model_name='trafficconditionlogs',
            name='ResponsibleUnit',
        ),
        migrations.RemoveField(
            model_name='trafficconditionlogs',
            name='TrafficCondition',
        ),
        migrations.DeleteModel(
            name='Ambulances',
        ),
        migrations.DeleteModel(
            name='AmbulanceSchedules',
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='Monitors',
        ),
        migrations.DeleteModel(
            name='ResponsibleUnits',
        ),
        migrations.DeleteModel(
            name='TrafficConditionLogs',
        ),
        migrations.DeleteModel(
            name='TrafficConditions',
        ),
        migrations.AddField(
            model_name='ambulanceschedule',
            name='TrafficConditionLog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.TrafficConditionLog'),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='ResponsibleUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance_system.ResponsibleUnit'),
        ),
    ]
