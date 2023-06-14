from django.shortcuts import render
from rest_framework import views

class UserCreateView(views.APIView):
    def post(self, request):
        print(request.POST)
