
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.models import User



class UserListView(ListView):
    model = User
    template_name = 'events/user_list.html'
    context_object_name = 'users'


class GalleryView(TemplateView):
    template_name = 'events/gallery.html'

events = [
{'id': 1, 'title': 'Концерт классической музыки', 'date':
'12.01.2025 19:00', 'description': 'Концерт с участием известных исполнителей.', 'location': 'Концертный зал', 'organizer': 'Иван Иванов'},
{'id': 2, 'title': 'Выставка современного искусства', 'date':
'02.02.2025 10:00', 'description': 'Выставка работ современных художников.',
'location': 'Галерея искусств', 'organizer': 'Петр Петров'},
{'id': 3, 'title': 'Театральная постановка', 'date': '08.03.2025 18:30', 'description': 'Постановка классического произведения.', 'location':
'Драматический театр', 'organizer': 'Светлана Смирнова'},
]
def event_detail(request, event_id):
    event = next((item for item in events if item['id'] == event_id), None)
    if event:
        return render(request, 'events/event_detail.html', {'event': event})
    else:
        return render(request, 'events/event_not_found.html')
    
def event_list(request):
    return render(request, 'events/event_list.html', {'events': events})

def home(request):
    return render(request, 'events/home.html')
def services(request):
    services_list = [
'Организация мероприятий',
'Аренда оборудования',
'Кейтеринг',
'Развлекательные программы',
]
    return render(request, 'events/services.html', {'services':
services_list})

team_members = [
{'name': 'Иван Иванов', 'position': 'Директор'},
{'name': 'Петр Петров', 'position': 'Менеджер проектов'},
{'name': 'Светлана Смирнова', 'position': 'Координатор мероприятий'},
]
def team(request):
    return render(request, 'events/team.html', {'team': team_members})
def gallery(request):
    return render(request, 'events/gallery.html')
def contact_us(request):
    return render(request, 'events/contact_us.html')

def about(request):
    return render(request, 'events/about.html', {'team': team_members})