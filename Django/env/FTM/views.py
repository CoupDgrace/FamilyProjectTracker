from django.shortcuts import render
from django.http import HttpResponse
from .forms import MembersForm
from .forms import TasksForm
from .forms import TaskNotesForm


# Create your views here.
# Home Page
def home(request):
#    return HttpResponse("Hello, Django!")
#def hello_there(request):
    return render (
        request,
        'FTM/HTML/BanksBoardIndex.html'
    )


# # # A few forms # # #

# Members Form

def Members(request):
    memForm = MembersForm()
    return render(request,'FTM/HTML/membersForm.html',{'form': form})