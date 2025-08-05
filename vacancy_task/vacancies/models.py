from django.contrib.auth.models import User
from django.db import models

VACANCY_STATUS = '{vacancy} со статусом {status}'


class Vacancy(models.Model):

    STATUS_CHOICES = (
        ('archive', 'ARCHIVE'),
        ('active', 'ACTIVE'),
    )

    title = models.CharField('Заголовок', max_length=32)
    status = models.CharField(
        'Статус', choices=STATUS_CHOICES, default='active', max_length=16,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='vacancies',
        verbose_name='Владелец',
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return VACANCY_STATUS.format(vacancy=self.title, status=self.status)
