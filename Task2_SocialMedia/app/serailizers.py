from rest_framework import serializers
from .models import Profile,Post,Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'bio',' followers', 'following']
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'caption', 'created_at', 'likes']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'comment', 'created_at']