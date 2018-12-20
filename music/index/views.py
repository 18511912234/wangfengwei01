from django.shortcuts import render

# Create your views here.
from.models import *
def indexView(request):
    search_song=Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:8]
    label_list=Label.objects.all()
    play_hot_song=Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:10]
    daily_recommendation=Song.objects.order_by('-song_release').all()[:3]
    search_ranking=search_song[:6]
    down_ranking=Dynamic.objects.select_related('song').order_by('-dynamic_down').all()[:6]
    all_ranking=[search_ranking,down_ranking]
    return render(request,'index.html',locals())

def page_not_found(request):
    return render(request, 'error404.html', status=404)