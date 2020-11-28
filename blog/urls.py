from django.contrib import admin
from django.urls import path,include
from .views import HomeView,DetailsPost,AddPostView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('detailpost/<int:pk>',DetailsPost.as_view(), name="detailspost"),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add_post/',AddPostView.as_view(), name="add_post"),

]
