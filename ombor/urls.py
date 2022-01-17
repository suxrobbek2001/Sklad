from django.contrib import admin
from django.urls import path, include
from omborapp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', include('omborapp.urls')),
    path('stats/', include('statisticaapp.urls')),
    path('', IndexView.as_view(), name='login'),



]
