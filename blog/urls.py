from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('change/<slug:post_slug>', views.change, name='change'),
    path('help', views.helper, name='help'),
    path('wort/<slug:post_slug>', views.wort, name='wort')
]
