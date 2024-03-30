from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/<str:quote_author>', views.author, name='author'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addquote/', views.addquote, name='addquote'),
]