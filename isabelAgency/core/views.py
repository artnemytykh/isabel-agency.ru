from django.shortcuts import render

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.urls import reverse

from .models import App

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['Name']
        number = request.POST['Number']
        email = request.POST['Email']
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'redirect_url': reverse("core:index"), 'error': 'Ненастоящий e-mail адресс'})
        else:
            company = request.POST['Company']
            try:
                website = request.POST['Website']
                role = request.POST['Role']
                application = App(name=name, number=number, email=email, website=website, company=company, role=role)
            except:
                application = App(name=name, number=number, email=email, company=company)
            application.save()
            return JsonResponse({'redirect_url': reverse("core:index"), 'success': 'Ваша заявка принята!'})
    return render(request, 'core/index.html')