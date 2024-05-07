from django.db import models


class Question(models.Model):
    CHOISES = [
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3', 'option3'),
        ('option4', 'option4'),
    ]
    question = models.CharField(max_length=50, unique=True, verbose_name='question')
    option1 = models.CharField(max_length=50, verbose_name='option1')
    option2 = models.CharField(max_length=50, verbose_name='option2')
    option3 = models.CharField(max_length=50,verbose_name='option3')
    option4 = models.CharField(max_length=50,verbose_name='option4')
    answer = models.CharField(max_length=7, choices=CHOISES, verbose_name='answer', help_text='choose the correct answer')
    status = models.BooleanField(default=False, verbose_name='status')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class UserResult(models.Model):
    fullname = models.CharField(max_length=20)
    totall = models.PositiveSmallIntegerField(default=0, verbose_name='all questions')
    score = models.PositiveSmallIntegerField(default=0, verbose_name='result')
    percent = models.FloatField(max_length=5, verbose_name='percentage')
    correct = models.PositiveSmallIntegerField(default=0)
    wrong = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'resuilt'
        verbose_name_plural = 'resuilts'