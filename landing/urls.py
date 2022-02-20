from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.urls import path, re_path
from lessons.models import *
from .views import *
urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^main/$', News.as_view(), name='news'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    path(r'lesson/<int:lesson_id>/theory/', views.theory, name='theory'),
    path(r'lesson/<int:lesson_id>/newwords/', views.newwords, name='newwords'),
    path(r'lesson/<int:lesson_id>/practice/', views.practice, name='practice'),
    url(r'^register/$', views.registerPage, name='register'),
    path('account/profile', views.profilePage, name="profile"),
    path('account/profile/edit', views.editprofilePage, name="editprofile"),
    path('account/profile/password_edit', PasswordsChangeView.as_view(), name="password_edit"),
    path('password_success', views.password_success, name="password_success"),
    url(r'^intro/1$', views.intro, name='intro'),
    url(r'^intro/2$', views.intro2, name='intro2'),
    url(r'^intro/3$', views.intro3, name='intro3'),
]