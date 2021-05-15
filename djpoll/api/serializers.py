from rest_framework import serializers
from .models import Poll, Question, Answer


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            'pk',
            'title',
            'text',
            'date_start',
            'date_end')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'pk',
            'text',
            'question_type',
            'poll',)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'question',
            'title',)
