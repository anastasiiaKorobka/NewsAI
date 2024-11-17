from django.urls import path
from .views import home_view


urlpatterns = [
    path('', home_view, name="home"),
    # path('articles/', articles_list, name='articles_list'),
]
