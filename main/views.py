from django.shortcuts import render
import requests
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

from authentication.models import Product

# Create your views here.
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = strip_tags(data.get("title", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        price = data.get("price", 0)
        user = request.user

        new_product = Product(
            name=title,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json(request):
    jersey_list = Product.objects.all()
    data = []
    
    for jersey in jersey_list:
        # Handle created_at field that might not exist in model
        try:
            created_at = jersey.created_at.isoformat() if jersey.created_at else '2024-01-01T00:00:00'
        except AttributeError:
            created_at = '2024-01-01T00:00:00'
            
        data.append({
            'id': str(jersey.id),
            'name': jersey.name,
            'title': jersey.name,  # Keep title for backward compatibility
            'description': jersey.description,
            'price': float(jersey.price) if jersey.price else 0.0,
            'category': jersey.category,
            'thumbnail': jersey.thumbnail,
            'created_at': created_at,
            'is_featured': jersey.is_featured,
            'user_id': jersey.user_id,
            'user_username': jersey.user.username if jersey.user_id else None,
        })

    return JsonResponse(data, safe=False)

def show_json_mine(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)

    jersey_list = Product.objects.filter(user=request.user)
    data = []
    
    for jersey in jersey_list:
        # Handle created_at field that might not exist in model
        try:
            created_at = jersey.created_at.isoformat() if jersey.created_at else '2024-01-01T00:00:00'
        except AttributeError:
            created_at = '2024-01-01T00:00:00'

        if jersey.user_id != request.user.id:
            continue
            
        data.append({
            'id': str(jersey.id),
            'name': jersey.name,
            'title': jersey.name,  # Keep title for backward compatibility
            'description': jersey.description,
            'price': float(jersey.price) if jersey.price else 0.0,
            'category': jersey.category,
            'thumbnail': jersey.thumbnail,
            'created_at': created_at,
            'is_featured': jersey.is_featured,
            'user_id': jersey.user_id,
            'user_username': jersey.user.username if jersey.user_id else None,
        })

    return JsonResponse(data, safe=False)

def show_json_by_id(request, jersey_id):
    try:
        jersey = Product.objects.select_related('user').get(pk=jersey_id)
        data = {
            'id': str(jersey.id),
            'title': jersey.name,
            'description': jersey.description,
            'category': jersey.category,
            'thumbnail': jersey.thumbnail,
            'created_at': jersey.created_at,
            'is_featured': jersey.is_featured,
            'user_id': jersey.user_id,
            'user_username': jersey.user.username if jersey.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)