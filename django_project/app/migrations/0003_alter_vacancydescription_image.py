
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_vacancydescription_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancydescription',
            name='image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
