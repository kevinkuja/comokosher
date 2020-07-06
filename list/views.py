from django.shortcuts import render, get_object_or_404

from .models import Shop

def index(request):
    shops = Shop.objects.order_by('-created_at')
    context = {'shops': shops}
    return render(request, 'list/index.html', context)

def detail(request, shop):
    shop = get_object_or_404(Shop, short_name=shop)
    return render(request, 'list/detail.html', {'shop': shop})