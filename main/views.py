from rest_framework.viewsets import ModelViewSet
from .serializers import QuestionSerailizer, AnswerSerailizer, NotificationsSerailizer
from .models import Question, Answer, Notification
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerailizer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerailizer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
class NotificationsViewSet(ModelViewSet):
    serializer_class = NotificationsSerailizer
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]