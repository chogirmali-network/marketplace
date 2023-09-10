from rest_framework import serializers

from mediafiles.models import Video, Category, VideoRanking,Badge,Image


class VideoSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

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
        fields = ('title',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class VideoRankingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = VideoRanking
        fields = ('video', 'user', 'rank')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.video = validated_data.get('video', instance.title)
        instance.user = validated_data.get('user', instance.title)
        instance.rank = validated_data.get('rank', instance.title)
        instance.save()
        return instance


class BadgeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Badge
        fields = ('title', 'code', 'priority', 'badge')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.title)
        instance.priority = validated_data.get('priority', instance.title)
        instance.badge = validated_data.get('badge', instance.title)
        instance.save()
        return instance


class ImageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Badge
        fields = ('image', 'width', 'height', 'size')
        read_only_fields = ('id',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.title)
        instance.width = validated_data.get('width', instance.title)
        instance.height = validated_data.get('height', instance.title)
        instance.size = validated_data.get('size', instance.title)
        instance.save()
        return instance
