from rest_framework import serializers
from polls.models import *


class ChoiceSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вариантов ответа
    """

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вывода вопросов
    """

    class Meta:
        model = Question
        fields = ('id', 'poll_id', 'text', 'question_type')


class QuestionDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для записи вопросов
    """
    choices = ChoiceSerializer(many=True, required=False)
    poll_id = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = ('id', 'poll_id', 'text', 'question_type', 'choices')


class PollDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для записи опросов
    """
    class Meta:
        model = Poll
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для вывода опросов
    """
    class Meta:
        model = Poll
        fields = ('title', 'description')


class AnswerTextSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для текстовых ответов
    """
    user_id = serializers.StringRelatedField(read_only=True)
    question_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('user_id', 'question_id', 'self_text')


class AnswerOneChoiceSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для ответов с одним вариантом
    """
    user_id = serializers.StringRelatedField(read_only=True)
    question_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('one_choice', 'user_id', 'question_id')


class AnswerManyChoiceSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для ответов с несколькими вариантами
    """
    user_id = serializers.StringRelatedField(read_only=True)
    question_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('many_choices', 'user_id', 'question_id')


