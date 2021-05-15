from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from .models import Question, Poll, Answer
from . import serializers

# Получение всех опросов
@api_view(['GET'])
def api_polls_list(request):
    if request.method == 'GET':
        current_date = datetime.now().date()
        polls = Poll.objects.filter(
            date_start__gte=current_date,
            date_end__gte=current_date)
        serializer = serializers.PollsSerializer(polls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Получение конкретного опроса и отправка ответа на него
@api_view(['GET', 'POST'])
def api_polls(request, id):
    if request.method == 'GET':
        questions = Question.objects.filter(poll=id)
        serializer = serializers.QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Получение ответов на вопросы опросов
@api_view(['GET'])
def api_answers(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = serializers.AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
