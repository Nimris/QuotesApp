from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('add-tag/', views.add_tag, name='add_tag'),
    path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('tag/delete/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('author/delete/<int:author_id>/', views.delete_author, name='delete_author'),
]
