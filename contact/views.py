from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Здесь можно добавить логику обработки формы, например, отправку email
        return HttpResponse("Спасибо за ваше сообщение!")
    return render(request, 'contact/contact.html')
