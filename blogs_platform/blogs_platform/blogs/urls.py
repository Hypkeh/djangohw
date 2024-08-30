from django.urls import path
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    
    path('login/', views.login_view, name='login_view'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),

    path('blogs/', views.BlogList.as_view(), name='blog_list'),
    path('blogs/create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blogs/delete/<int:pk>/', views.BlogDelete.as_view(), name='blog_delete'),
    path('blogs/update/<int:pk>/', views.BlogUpdate.as_view(), name='blog_update'),
    path('blogs/detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),

    path('messages/', views.MessagesList.as_view(), name='message_list'),
    path('messages/create/', views.MessagesCreate.as_view(), name='message_create'),
    path('messages/delete/<int:pk>/', views.MessagesDelete.as_view(), name='message_delete'),
    path('messages/update/<int:pk>/', views.MessagesUpdate.as_view(), name='message_update'),
    path('messages/detail/<int:pk>/', views.MessagesDetail.as_view(), name='message_detail'),
    
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comments/delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
    path('comments/update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/detail/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]