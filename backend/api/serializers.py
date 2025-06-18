from rest_framework import serializers
from .models import User, Video, Like, Follow, Earning

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'avatar']

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'user', 'title', 'file', 'thumbnail', 'description', 'created_at', 'views']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = '__all__'
