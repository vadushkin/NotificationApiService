from django.core.validators import RegexValidator
from django.db import models


class Operator(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=33, verbose_name='Оператор')
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name='Код оператора'
    )

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Tag(models.Model):
    objects = models.Manager()
    name = models.CharField(
        max_length=33,
        unique=True,
        verbose_name='Тэг'
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('name',)

    def __str__(self):
        return '{}'.format(self.name)


class Mailing(models.Model):
    objects = models.Manager()
    start_datetime = models.DateTimeField(
        verbose_name='Дата начала рассылки',
    )
    text = models.TextField(max_length=255, verbose_name='Текст')
    finish_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата окончания рассылки'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='mailing_tags',
        blank=True,
        verbose_name='Тэг'
    )
    operators = models.ManyToManyField(
        Operator,
        related_name='mailings_operator',
        blank=True,
        verbose_name='Код оператора'
    )

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('id',)

    def __str__(self):
        return str(self.text[:15])


class Client(models.Model):
    objects = models.Manager()
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='Мобильный телефон',
        validators=[
            RegexValidator(
                regex=r'7[0-9]{10}',
                message=('Формат ввода '
                         '7XXXXXXXXXX (X - цифра от 0 до 9)')
            )
        ]
    )
    operator = models.ForeignKey(
        'Operator',
        on_delete=models.CASCADE,
        related_name='clients_operator',
        verbose_name='Оператор'
    )
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        related_name='clients_tag',
        blank=True,
        null=True,
        verbose_name='Тэг'
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('phone_number',)

    def __str__(self):
        return '{}'.format(self.phone_number)


class Message(models.Model):
    objects = models.Manager()
    Not_sent = 'Не отправлено'
    Departure = 'Отправляется'
    Sent = 'Отправлено'

    Stat = (
        (Not_sent, 'Не отправлено'),
        (Departure, 'Отправляется'),
        (Sent, 'Отправлено')
    )

    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отправки сообщения'
    )
    status = models.CharField(verbose_name='Статус',
                              default=Not_sent,
                              choices=Stat,
                              max_length=33)

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='id_mailing',
        blank=True,
        verbose_name='Рассылка'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='id_client',
        blank=True,
        verbose_name='Клиент'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('mailing',)

    def __str__(self):
        return str(self.mailing)
