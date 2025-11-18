from main.views import proxy_image, create_product_flutter, show_json, show_json_by_id, show_json_mine
from django.urls import path

app_name = 'main'
urlpatterns = [
    # ... other paths
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json/', show_json, name='show_json'),
    path('json/<uuid:jersey_id>/', show_json_by_id, name='show_json_by_id'),
    path('json/my-products/', show_json_mine, name='show_json_mine'),
]