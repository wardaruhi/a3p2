

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='Book',
            name='check_out',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
