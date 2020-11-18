

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0004_auto_20200211_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='Customer',
            name='room_number',
        ),
    ]
