from django.shortcuts import render
from django.http import HttpResponse
from votingContact.models import Queries

# Create your views here.
def contact(request):
    return render(request, 'contact.html')

def query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Query = Queries.objects.create(name=name, email=email, message=message)
        Query.save()
        query_recorded = 'Query recorded'
        return render(request, 'contact.html',{'message':query_recorded})