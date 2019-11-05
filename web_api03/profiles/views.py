import json
from django.shortcuts import render
from rest_framework.reverse import reverse

from profiles.models import *
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *


class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profiles-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class PostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class AddressesList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'addresses-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


class CommentsList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comments-list'


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'profiles': reverse(ProfilesList.name, request=request),
                'post': reverse(PostsList.name, request=request),
                'comments': reverse(CommentsList.name, request=request),
                'address': reverse(AddressesList.name, request=request),
            }
        )

# class ImportJson():
#     dump_data = open('db.json', 'r')
#     as_json = json.load(dump_data)
#
#     for post in as_json['posts']:
#         profile = Profile.objects.get(id=post['userId'])
#
#         Post.objects.create(title=post['title'],
#                             body=post['body'],
#                             userId=profile)
#
#     for comment in as_json['comments']:
#         post = Post.objects.get(id=comment['postId'])
#
#         Comment.objects.create(name=comment['name'],
#                                email=comment['email'],
#                                body=comment['body'],
#                                postId=post)
