from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def scrape_google_home(request):
    url = "https://www.google.com"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all images with alt text (e.g., Google logo)
    images = [img['alt'] for img in soup.find_all('img') if img.get('alt')]

    return JsonResponse({'images_with_alt': images})

