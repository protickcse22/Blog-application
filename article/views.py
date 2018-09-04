from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .import forms



class ArticleView(ListView):
    template_name='article/home.html'

    model=Article

    def get_queryset(self):
        queryset=super().get_queryset

        return queryset

def articleDetails(request,slug):

    articles=Article.objects.get(slug=slug)

    return render(request,'article/article_details.html',{'article_detail': articles })
    

@login_required(login_url ="/accounts/login")
def createArticleView(request):
    if request.method=='POST':
        form = forms.CreateArticleform(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect ('article:articlelist')
    else:
        form=forms.CreateArticleform()
    return render(request,'article/create_article.html',{'form':form})


