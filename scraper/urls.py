from django.urls import path
from .views import scrape_google_home

urlpatterns = [
    path('scrape/', scrape_google_home, name='scrape_example'),
]
