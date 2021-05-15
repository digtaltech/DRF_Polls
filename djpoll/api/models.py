from django.db import models

from django.utils.timezone import now


class Poll(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(max_length=200, verbose_name="Описание")
    date_start = models.DateField(verbose_name="Дата старта", default=now)
    date_end = models.DateField(verbose_name="Дата окончания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question_type = (
        ('MULTIPLE', 'Несколько вариантов ответа'),
        ('SINGLE', 'Один вариант ответа'),
        ('TEXT', 'Текст'),
    )
    text = models.TextField(max_length=200, verbose_name="Текст Вопроса")
    question_type = models.CharField(max_length=100,
                                     verbose_name="Тип вопроса",
                                     null=False,
                                     choices=question_type,
                                     default=None,
                                     blank=False)
    poll = models.ForeignKey(
        Poll, on_delete=models.PROTECT, related_name='question')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name='answer')
    title = models.CharField(max_length=200, verbose_name="Ответ")
    username = models.ForeignKey(
        'auth.User', related_name='answers', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
