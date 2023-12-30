from django.urls import path, include
from . import views

urlpatterns = [
    path('page-<int:page>', views.news_home, name = 'news_home'),
    path('add_article', views.add_article, name="add_article"),
    path('<int:pk>', views.news_detail_view, name="detail_view"),
    path('<int:pk>/update', views.article_edit, name="news-update"),
    path('<int:pk>/delete', views.article_delete, name="news-delete"),
    path('<int:pk>/delete/delete', views.article_delete_delete, name="news-delete-delete"),
    path('<int:pk>/delete/cancel', views.article_delete_cancel, name="news-delete-cancel")
]
