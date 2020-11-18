

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0005_remove_customer_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Customer_id',
        ),
        migrations.RemoveField(
            model_name='book',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='start_date',
        ),
        migrations.AddField(
            model_name='book',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental_app.Customer'),
        ),
    ]
