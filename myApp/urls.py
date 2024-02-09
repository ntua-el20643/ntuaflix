from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("login",views.login, name="login"),
    path("name", views.names, name="name"),
    path('name/<str:nconst>', views.name_details, name='name details'),
    path("title", views.titles, name="titles"),
    path("title/<str:tconst>",views.title_details, name="title details"),
    path("upload",views.upload, name="upload"),
    path("searchtitle", views.search_titles, name='search_title'),
    path("searchname",views.search_names, name='search_name'),
    path("bygenre",views.bygenre, name='bygenre')
]