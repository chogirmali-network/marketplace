from rest_framework import serializers

from mediafiles.models import Video, Category, VideoRanking,Badge,Image


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
        read_only_fields = ('id',)


class VideoRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoRanking
        fields = ('video', 'user', 'rank')
        read_only_fields = ('id',)


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ('title', 'code', 'priority', 'badge')
        read_only_fields = ('id',)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = ('image', 'width', 'height', 'size')
        read_only_fields = ('id',)
