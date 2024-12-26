from django.http import HttpResponse, JsonResponse
from .models import ArticlePost, Category, Comment
from .forms import ArticlePostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect


def article_list_html(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        article_posts = ArticlePost.objects.filter(category=category)
    else:
        article_posts = ArticlePost.objects.all()

    categories = Category.objects.all()  # For rendering category buttons
    return render(request, 'articles/listed_articles.html', {'article_posts': article_posts, 'categories': categories})

def create_article(request):
    if request.method == 'POST':
        form = ArticlePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list_html')
    else:
        form = ArticlePostForm()

    categories = Category.objects.all()  # Pull categories from the database
    return render(request, 'articles/create_article.html', {'form': form, 'categories': categories})

def article_detail(request, pk):
    article = get_object_or_404(ArticlePost, pk=pk)
    comments = Comment.objects.filter(article_id=pk)
    return render(request, 'articles/article_details.html', {'article_details': article, 'comments': comments})

'''
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments})
'''

def create_comment(request, pk):
    article = get_object_or_404(ArticlePost, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  # Associate the comment with the article
            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'articles/comment_form.html', {'form': form, 'article': article})