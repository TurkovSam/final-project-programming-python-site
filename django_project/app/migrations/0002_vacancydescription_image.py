
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancydescription',
            name='image',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Изображение'),
        ),
    ]
