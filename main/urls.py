from main.views import proxy_image
from django.urls import path

app_name = 'main'
urlpatterns = [
    # ... other paths
    path('proxy-image/', proxy_image, name='proxy_image'),
]