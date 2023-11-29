from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    img = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    title = models.CharField(max_length=150, verbose_name='название')
    img = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='превью')
    video = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='видео')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
