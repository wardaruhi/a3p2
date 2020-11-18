

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),

        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=12, unique=True)),
                ('room_number', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('room_number', models.PositiveIntegerField()),
                ('special_req', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('BedType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_app.BedType')),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_app.Customer')),
            ],
        ),
    ]
