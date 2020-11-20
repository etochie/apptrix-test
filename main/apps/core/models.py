from time import time

from django.db import models


def image_upload_path(instance, filename):
    return '{0}/{1}'.format(instance.title, filename)

def generate_product_lid():
    return str(int(time()))


class TopBackgroundImage(models.Model):
    image_width = models.PositiveSmallIntegerField(
        verbose_name='Ширина фото',
        default=1680
    )
    image_height = models.PositiveSmallIntegerField(
        verbose_name='Высота фото',
        default=945
    )
    image = models.ImageField(
        verbose_name='Фото верхнего фона',
        upload_to='top_background/',
        width_field='image_width',
        height_field='image_height',
        blank=False,
        null=False
    )


class ItemModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название вещи',
        unique=True,
        blank=False,
        null=False
    )
    data_product_lid = models.PositiveIntegerField(
        verbose_name='id для генерации в шаблоне',
        default=generate_product_lid(),
        blank=True,
        null=True
    )
    is_main = models.BooleanField(
        verbose_name='Показывать на главной?',
        default=False
    )
    image_width = models.PositiveSmallIntegerField(
        verbose_name='Ширина фото',
        default=634
    )
    image_height = models.PositiveSmallIntegerField(
        verbose_name='Высота фото',
        default=561
    )
    image = models.ImageField(
        verbose_name='Основное фото',
        upload_to=image_upload_path,
        width_field='image_width',
        height_field='image_height',
        blank=False,
        null=False
    )
    image_mouseover = models.ImageField(
        verbose_name='Фото при наведении мыши',
        upload_to=image_upload_path,
        width_field='image_width',
        height_field='image_height',
        blank=False,
        null=False
    )
    old_price = models.PositiveIntegerField(
        verbose_name='Старая цена (будет зачеркнута)',
        blank=True,
        null=True
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена',
        blank=False,
        null=False
    )

    def __str__(self):
        return self.title


class Block3Image(models.Model):
    image_width = models.PositiveSmallIntegerField(
        verbose_name='Ширина фото',
        default=1680
    )
    image_height = models.PositiveSmallIntegerField(
        verbose_name='Высота фото',
        default=2519
    )
    first_image = models.ImageField(
        verbose_name='Первое фото третьего блока',
        upload_to='block3_images/',
        width_field='image_width',
        height_field='image_height',
        blank=False,
        null=False
    )
    second_image = models.ImageField(
        verbose_name='Второе фото третьего блока',
        upload_to='block3_images/',
        width_field='image_width',
        height_field='image_height',
        blank=False,
        null=False
    )


class Reviews(models.Model):
    first_reviewer_name = models.CharField(
        verbose_name='Имя первого автора',
        max_length=255
    )
    first_review = models.CharField(
        verbose_name='Первый отзыв',
        max_length=255
    )
    second_reviewer_name = models.CharField(
        verbose_name='Имя второго автора',
        max_length=255
    )
    second_review = models.CharField(
        verbose_name='Второй отзыв',
        max_length=255
    )
    third_reviewer_name = models.CharField(
        verbose_name='Имя третьего автора',
        max_length=255
    )
    third_review = models.CharField(
        verbose_name='Третий отзыв',
        max_length=255
    )
    fourth_reviewer_name = models.CharField(
        verbose_name='Имя четвертого автора',
        max_length=255
    )
    fourth_review = models.CharField(
        verbose_name='Четвертый отзыв',
        max_length=255
    )
    fifth_reviewer_name = models.CharField(
        verbose_name='Имя пятого автора',
        max_length=255
    )
    fifth_review = models.CharField(
        verbose_name='Пятый отзыв',
        max_length=255
    )
    sixth_reviewer_name = models.CharField(
        verbose_name='Имя шестого автора',
        max_length=255
    )
    sixth_review = models.CharField(
        verbose_name='Шестой отзыв',
        max_length=255
    )

class Contacts(models.Model):
    phone_number = models.CharField(
        verbose_name='Номер телефона в футере',
        max_length=20
    )
    email = models.CharField(
        verbose_name='Email в футере',
        max_length=255
    )
    address = models.CharField(
        verbose_name='Адрес в футере',
        max_length=255
    )
