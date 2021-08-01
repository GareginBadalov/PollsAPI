from django.urls import path
from polls.views import *

app_name = 'polls'
urlpatterns = [
    path('poll/create/', PollCreateView.as_view()),
    path('', PollListView.as_view()),
    path('poll/<int:pk>/', PollDetailView.as_view()),
    path('question/create/', QuestionCreateView.as_view()),
    path('choice/create/', ChoiceCreateView.as_view()),
    path('question/all/', QuestionListView.as_view()),
    path('question/<int:pk>/', QuestionDetailView.as_view()),
    path('polls/active/', ActivePollListView.as_view()),
    path('answer/<int:question_pk>/', AnswerCreateView.as_view()),
    path('poll/finished/', FinishedPollsListView.as_view()),

]
