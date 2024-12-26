from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.article_list_html, name='article_list_html'),
    path('category/<int:category_id>/', views.article_list_html, name='article_list_by_category'),
    path('create/', views.create_article, name='create_article'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('<int:pk>/comment/', views.create_comment, name='create_comment'),
    #path('article/<int:article_id>/', views.article_detail, name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
