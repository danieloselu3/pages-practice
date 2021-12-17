from django.urls import path

from .views import HomePageView, AboutPageView

app_name = 'pages'      # include app name to avoid name space collitions
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]