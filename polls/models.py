from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    text = models.TextField('Текст Вопроса', )
    QUESTION_TYPES = (("Text", "Ответ текстом"),
                      ("One_choice", "Ответ с выбором одного варианта"),
                      ("Many_choices", "Ответ с выбором нескольких вариантов"))
    question_type = models.TextField('Тип вопроса', choices=QUESTION_TYPES, max_length=12)
    poll_id = models.ForeignKey('Poll', on_delete=models.CASCADE, )

    def __str__(self):
        return self.text


class Poll(models.Model):
    title = models.TextField('Название опроса', )
    description = models.TextField("Описание опроса", )
    time_create = models.DateTimeField('Дата создания опроса', auto_now_add=True)
    time_finish = models.DateTimeField('Дата завершения опроса')

    def __str__(self):
        return self.title


class Choice(models.Model):
    text = models.TextField(verbose_name='Вариант ответа')
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    # choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    many_choices = models.ManyToManyField(Choice, blank=True)
    one_choice = models.ForeignKey(Choice,
                                   null=True,
                                   on_delete=models.CASCADE,
                                   related_name="answers_one_choice",
                                   blank=True)
    self_text = models.TextField(null=True, blank=True)


