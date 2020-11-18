

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0006_auto_20201117_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
