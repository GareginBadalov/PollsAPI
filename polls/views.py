from django.utils.timezone import now
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from polls.serializers import AnswerTextSerializer, QuestionDetailSerializer, PollListSerializer, PollDetailSerializer, \
    QuestionSerializer, AnswerOneChoiceSerializer, AnswerManyChoiceSerializer, ChoiceSerializer
from polls.models import *


class ChoiceCreateView(generics.CreateAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAdminUser,)


class FinishedPollsListView(generics.ListAPIView):
    serializer_class = PollListSerializer

    def get_queryset(self):
        answers = Answer.objects.filter(user_id=self.request.user).values('question_id')
        questions = Question.objects.filter(id__in=answers).values('poll_id')
        queryset = Poll.objects.filter(id__in=questions)
        return queryset
    permission_classes = (permissions.IsAdminUser,)


class PollListView(generics.ListAPIView):
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class ActivePollListView(generics.ListAPIView):
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.filter(time_finish__gte=now())
    permission_classes = (permissions.IsAuthenticated,)


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class AnswerCreateView(generics.CreateAPIView):
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



