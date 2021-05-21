from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# Home Page
def home(request):
    nTicks = Tasks.objects.filter(assignedMember=1)
    backTicks = Tasks.objects.filter(taskStatus='backlog')
    return render (
        request,
        'FTM/HTML/BanksBoardIndex.html',
        {'nTicks': nTicks, 'backTicks':backTicks},
    )   


# # # A few forms # # #

# Members Form
'''
def Members(request):
    memForm = MembersForm()
    return render(request,'FTM/HTML/membersForm.html',{'form':form})

    '''