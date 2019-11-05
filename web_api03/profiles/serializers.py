from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = (
            'url',
            'street',
            'suite',
            'city',
            'zipcode',
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='street')

    class Meta:
        model = Profile
        fields = (
            'url',
            'id',
            'name',
            'email',
            'address',
        )



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    postId = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')

    class Meta:
        model = Comment
        fields = ('url',
                  'name',
                  'email',
                  'body',
                  'postId',
        )



class PostSerializer(serializers.HyperlinkedModelSerializer):
    userId = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='id')

    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'body',
            'userId',
        )