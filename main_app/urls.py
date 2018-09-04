
from django.urls import path
from .import views
from article import views as arview

urlpatterns = [
    path('',arview.ArticleView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about')

]