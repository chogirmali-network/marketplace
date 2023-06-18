from rest_framework import serializers
from .models import *


class VideoLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLessonsModel
        fields = '__all__'
        read_only_fields = ('id', 'upload_date',)

    def create(self, validated_data):
        return VideoLessonsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.caption = validated_data.get('caption', instance.caption)
        instance.video = validated_data.get('video', instance.video)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.upload_date = validated_data.get('upload_date', instance.upload_date)
        instance.author = validated_data.get('author', instance.author)
        instance.course_cost = validated_data.get('course_cost', instance.course_cost)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.save()
        return instance


class VideoCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCategories
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return VideoCategories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        read_only_fields = ('id', 'send_time')

    def create(self, validated_data):
        return Messages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.is_seen = validated_data.get('is_seen', instance.is_seen)
        instance.seen_time = validated_data.get('seen_time', instance.seen_time)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Chats.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.save()
        return instance
