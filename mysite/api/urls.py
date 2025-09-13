from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', views.BlogPostRetriveUpdateDestroy.as_view(), name='blogpost-detail'),
    path('blogposts/search/', views.BlogPostL.as_view(), name='blogpost-list-search'),
]