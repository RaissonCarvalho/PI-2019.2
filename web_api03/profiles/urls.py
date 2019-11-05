from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfilesList.as_view(), name=views.ProfilesList.name),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('posts/', views.PostsList.as_view(), name=views.PostsList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments/', views.CommentsList.as_view(), name=views.CommentsList.name),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    path('addresses/', views.AddressesList.as_view(), name=views.AddressesList.name),
    path('addresses/<int:pk>', views.AddressDetail.as_view(), name=views.AddressDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]