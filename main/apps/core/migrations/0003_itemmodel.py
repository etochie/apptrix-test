# Generated by Django 3.0.8 on 2020-11-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201118_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название вещи')),
                ('data_product_lid', models.PositiveIntegerField(blank=True, default='1605722108', null=True, verbose_name='id для генерации в шаблоне')),
                ('is_main', models.BooleanField(default=False, verbose_name='Показывать на главной?')),
                ('image_width', models.PositiveSmallIntegerField(verbose_name='Ширина фото')),
                ('image_height', models.PositiveSmallIntegerField(verbose_name='Высота фото')),
                ('image', models.ImageField(height_field='image_height', upload_to='', verbose_name='Основное фото', width_field='image_width')),
                ('image_mouseover', models.ImageField(height_field='image_height', upload_to='', verbose_name='Фото при наведении мыши', width_field='image_width')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Цена')),
            ],
        ),
    ]
