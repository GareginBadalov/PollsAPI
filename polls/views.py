from django.utils.timezone import now
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from polls.serializers import AnswerTextSerializer, QuestionDetailSerializer, PollListSerializer, PollDetailSerializer, \
    QuestionSerializer, AnswerOneChoiceSerializer, AnswerManyChoiceSerializer, ChoiceSerializer
from polls.models import *


class ChoiceCreateView(generics.CreateAPIView):
    """
    Ручка для создания вариантов ответа
    """
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAdminUser,)


class ChoiceUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Ручка для создания вариантов ответа
    """
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class FinishedPollsListView(generics.ListAPIView):
    """
    Ручка для получения завершенных опросов
    """
    serializer_class = PollListSerializer

    def get_queryset(self):
        answers = Answer.objects.filter(user_id=self.request.user).values('question_id')
        questions = Question.objects.filter(id__in=answers).values('poll_id')
        queryset = Poll.objects.filter(id__in=questions)
        return queryset
    permission_classes = (permissions.IsAdminUser,)


class PollListView(generics.ListAPIView):
    """
    Ручка для получения всех опросов
    """
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class ActivePollListView(generics.ListAPIView):
    """
    Ручка для получения активных опросов
    """
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.filter(time_finish__gte=now())
    permission_classes = (permissions.IsAuthenticated,)


class PollCreateView(generics.CreateAPIView):
    """
    Ручка для создания опросов
    """
    serializer_class = PollDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Ручка для получения информации об опросе
    """
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionListView(generics.ListAPIView):
    """
    Ручка для списка вопросов
    """
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionCreateView(generics.CreateAPIView):
    """
    Ручка для создания вопросов
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Ручка для получения вопроса
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class AnswerCreateView(generics.CreateAPIView):
    """
    Ручка для ответов на вопросы
    """
    serializer_class = AnswerTextSerializer
    queryset = Answer.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(
            user_id=self.request.user,
            question_id=get_object_or_404(
                Question,
                pk=self.kwargs['question_pk'],
            )
        )

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
        )
        if question.question_type == "One_choice":
            return AnswerOneChoiceSerializer
        elif question.question_type == "Many_choices":
            return AnswerManyChoiceSerializer
        else:
            return AnswerTextSerializer



