# 1. В проекте Django создать Категория (поля post, name, description), связать с моделью Пост по М2М.
# 2. Создать модель Комментарий (поля User, Text)

from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    STATUS_CHOICES = (('Published', 'Published'),
                      ('Unpublished', 'Unpublished'))
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    name = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    description = models.TextField('Описание', null=True)
    photo = models.ImageField('Фотография', upload_to='photo_post/', null=True, blank=True)
    status = models.CharField('Статус публикации', max_length=200, choices=STATUS_CHOICES)
    rating = models.PositiveSmallIntegerField('Рейтинг', choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.name} - {self.rating}'


class Category(models.Model):
    post = models.ManyToManyField(Post,
                                  related_name='categories',
                                  verbose_name='Post')
    name = models.CharField('Наименование столбца', max_length=50, null=True)
    description = models.TextField('opisanie', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_comment',
        verbose_name='coment'
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comment_to_post',
                             verbose_name='Post')
    comment_txt = models.CharField('text', max_length=134)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.user} : {self.comment_txt}'

# Create your models here.
