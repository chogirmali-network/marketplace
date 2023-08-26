from rest_framework import serializers

from backend.apps.mediafiles.models import Video, Category


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.caption = validated_data.get('caption', instance.caption)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.video = validated_data.get('video', instance.video)
        instance.banner = validated_data.get('banner', instance.banner)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('title', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.save()
        return instance


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )
        read_only_fields = ('id', )

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
