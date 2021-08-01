# Generated by Django 2.2.10 on 2021-07-31 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210731_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='many_choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='many_choices',
            field=models.ManyToManyField(blank=True, to='polls.Choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='one_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_one_choice', to='polls.Choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='self_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.TextField(choices=[('Text', 'Ответ текстом'), ('One_choice', 'Ответ с выбором одного варианта'), ('Many_choices', 'Ответ с выбором нескольких вариантов')], max_length=12, verbose_name='Тип вопроса'),
        ),
    ]
