from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class VideoLessonCreateDetailUpdateDelete(APIView):

    def get(self, req, pk=None):
        if pk:
            instance = get_object_or_404(VideoLessonsModel, pk=pk)
            ser = VideoLessonSerializer(instance)
        else:
            cats = VideoLessonsModel.objects.all()
            ser = VideoLessonSerializer(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, req):
        ser = VideoLessonSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def patch(self, req, pk):
        instance = get_object_or_404(VideoLessonsModel, pk=pk)
        ser = VideoLessonSerializer(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def put(self, req, pk):
        instance = get_object_or_404(VideoLessonsModel, pk=pk)
        ser = VideoLessonSerializer(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        ins = get_object_or_404(VideoLessonsModel, pk=pk)
        ins.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class VideoCategoriesCreateDetailUpdateDelete(APIView):

    def get(self, req, pk=None):
        if pk:
            instance = get_object_or_404(VideoCategories, pk=pk)
            ser = VideoCategoriesSerializer(instance)
        else:
            cats = VideoCategories.objects.all()
            ser = VideoCategoriesSerializer(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, req):
        ser = VideoCategoriesSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def patch(self, req, pk):
        instance = get_object_or_404(VideoCategories, pk=pk)
        ser = VideoCategoriesSerializer(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def put(self, req, pk):
        instance = get_object_or_404(VideoCategories, pk=pk)
        ser = VideoCategoriesSerializer(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        ins = get_object_or_404(VideoCategories, pk=pk)
        ins.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class CategoryCreateDetailUpdateDelete(APIView):

    def get(self, req, pk=None):
        if pk:
            instance = get_object_or_404(Category, pk=pk)
            ser = CategorySerializer(instance)
        else:
            cats = Category.objects.all()
            ser = CategorySerializer(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, req):
        ser = CategorySerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def patch(self, req, pk):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializer(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def put(self, req, pk):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializer(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        ins = get_object_or_404(Category, pk=pk)
        ins.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class MessagesCreateDetailUpdateDelete(APIView):

    def get(self, req, pk=None):
        if pk:
            instance = get_object_or_404(Messages, pk=pk)
            ser = MessagesSerializer(instance)
        else:
            cats = Messages.objects.all()
            ser = MessagesSerializer(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, req):
        ser = MessagesSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def patch(self, req, pk):
        instance = get_object_or_404(Messages, pk=pk)
        ser = MessagesSerializer(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def put(self, req, pk):
        ins = get_object_or_404(Messages, pk=pk)
        ser = MessagesSerializer(ins, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        ins = get_object_or_404(Messages, pk=pk)
        ins.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class ChatsCreateDetailUpdateDelete(APIView):

    def get(self, req, pk=None):
        if pk:
            instance = get_object_or_404(Chats, pk=pk)
            ser = ChatsSerializer(instance)
        else:
            cats = Chats.objects.all()
            ser = ChatsSerializer(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, req):
        ser = ChatsSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def patch(self, req, pk):
        instance = get_object_or_404(Chats, pk=pk)
        ser = ChatsSerializer(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def put(self, req, pk):
        instance = get_object_or_404(Chats, pk=pk)
        ser = ChatsSerializer(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        ins = get_object_or_404(Chats, pk=pk)
        ins.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)

