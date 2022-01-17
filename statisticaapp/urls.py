from django.urls import path
from statisticaapp.views import StatsView


urlpatterns = [
    path('', StatsView.as_view(), name='stats'),


]