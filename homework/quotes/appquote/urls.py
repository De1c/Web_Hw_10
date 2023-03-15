from django.urls import path

from . import views

app_name = 'appquote'

urlpatterns = [
    path('', views.main, name='main'),
    path('addtag/', views.addtag, name='addtag'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addquote/', views.addqoute, name='addquote'),
    path("author/<str:fullname>", views.author_page, name="author"),
    path("tag/<str:tag>", views.tag_page, name="tag")
]