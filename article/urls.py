
from django.urls import path
from . import views

app_name='article'

urlpatterns = [
    path('',views.ArticleView.as_view(),name='articlelist'),

    path('create_article/',views.createArticleView,name='create_article'),

    path('<slug:slug>/',views.articleDetails,name='detail')

]