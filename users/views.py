from django.shortcuts import render
from rest_framework import views
from .models import Project,Team,Client
from .serializer import ProjectSerializer,TeamSerializer,ClientSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView




class UserCreateView(views.APIView):
    def post(self, request):
        print(request.POST)


# Tacket-16 

class ProjectCreateListAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'


class ProjectRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'


class ClientCreateListAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'


class ClientRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'


class TeamCreateListAPIView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'


class TeamRetriveUpdatedeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'



