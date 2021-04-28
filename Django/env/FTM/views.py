from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
#    return HttpResponse("Hello, Django!")
#def hello_there(request):
    return render (
        request,
        'FTM/HTML/BanksBoardIndex.html'
    )
