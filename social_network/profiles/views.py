import json
from rest_framework.reverse import reverse
from profiles.models import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from .permissions import *


class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profiles-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsProfileOrReadOnly,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly,)


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          PostIsOwnerOrReadOnly,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          PostIsOwnerOrReadOnly,)


class AddressesList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'addresses-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


class CommentsList(generics.ListCreateAPIView):
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

# class import_data():
#     dump_data = open('db.json', 'r')
#     as_json = json.load(dump_data)
#
#     for user in as_json['users']:
#         # address = Address.objects.create(street=user['address']['street'],
#         #                                  suite=user['address']['suite'],
#         #                                  city=user['address']['city'],
#         #                                  zipcode=user['address']['zipcode'])
#         # first_name, last_name = user['name'].split(" ")
#         # new_user = User.objects.create_user(first_name=first_name,
#         #                                     last_name=last_name,
#         #                                     username=user['username'],
#         #                                     email=user['email'],
#         #                                     password="123456")
#         Profile.objects.create(id=user['id'],
#                                name=user['name'],
#                                email=user['email'],)
#                                user=new_user,
#                                 address=address)
#
#     for post in as_json['posts']:
#         profile = Profile.objects.get(id=post['user_id'])
#         Post.objects.create(id=post['id'],
#                             title=post['title'],
#                             body=post['body'],
#                             userId=post['userId'])
#
#     for comment in as_json['comments']:
#         post = Post.objects.get(id=comment['post_id'])
#         Comment.objects.create(id=comment['id'],
#                                name=comment['name'],
#                                email=comment['email'],
#                                body=comment['body'],
#                                post=post)