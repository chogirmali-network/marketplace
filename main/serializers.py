from rest_framework import serializers
from .models import Question,Answer,Notification

class QuestionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
    
class AnswerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
class NotificationsSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'